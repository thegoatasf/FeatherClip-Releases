"""Publish verified installer artifacts; never fetch or publish application source."""
import hashlib
import json
import pathlib
import re
import subprocess
import urllib.parse
import urllib.request
import zipfile

manifest = json.loads(pathlib.Path("release.json").read_text())
version = manifest["version"]
if not re.fullmatch(r"\d+\.\d+\.\d+", version):
    raise ValueError("Invalid release version")
expected_names = {"FeatherClip-Mac-AppleSilicon.dmg", "FeatherClip-Windows-Setup.exe"}
artifacts = manifest["artifacts"]
if len(artifacts) != 2 or {a["file"] for a in artifacts} != expected_names:
    raise ValueError("Release must contain both installers")
output = pathlib.Path("dist")
output.mkdir(exist_ok=True)
checksums = []
for artifact in artifacts:
    url = urllib.parse.urlsplit(artifact["url"])
    if url.scheme != "https" or not url.hostname or not url.hostname.endswith(".oaiusercontent.com") or url.username:
        raise ValueError("Unexpected artifact download host")
    if not re.fullmatch(r"[0-9a-f]{64}", artifact["sha256"]):
        raise ValueError("Invalid artifact checksum")
    archive = output / (artifact["file"] + ".zip")
    digest = hashlib.sha256()
    size = 0
    with urllib.request.urlopen(artifact["url"], timeout=60) as response, archive.open("wb") as target:
        while chunk := response.read(1024 * 1024):
            size += len(chunk)
            if size > 1024 * 1024 * 1024:
                raise ValueError("Artifact exceeds download limit")
            digest.update(chunk)
            target.write(chunk)
    if digest.hexdigest() != artifact["sha256"]:
        raise ValueError("Artifact hash mismatch")
    with zipfile.ZipFile(archive) as bundle:
        members = [item for item in bundle.infolist() if not item.is_dir()]
        if len(members) != 1 or members[0].filename != artifact["file"] or members[0].file_size > 1024 * 1024 * 1024:
            raise ValueError("Unexpected artifact contents")
        digest = hashlib.sha256()
        with bundle.open(members[0]) as source, (output / artifact["file"]).open("wb") as target:
            while chunk := source.read(1024 * 1024):
                digest.update(chunk)
                target.write(chunk)
        checksums.append(digest.hexdigest() + "  " + artifact["file"])
    archive.unlink()
(output / "SHA256SUMS.txt").write_text("\n".join(sorted(checksums)) + "\n")
tag = "v" + version
repo = "thegoatasf/FeatherClip-Releases"
# Draft first: clients never see a release containing only one installer.
subprocess.run(["gh", "release", "create", tag, "--repo", repo, "--draft", "--title", "Feather Clip " + manifest.get("display_version", version),
                "--notes-file", "RELEASE-NOTES.md", *[str(output / name) for name in sorted(expected_names)],
                str(output / "SHA256SUMS.txt")], check=True)
subprocess.run(["gh", "release", "edit", tag, "--repo", repo, "--draft=false", "--latest"], check=True)

# Explicit release-manifest opt-in: remove superseded public downloads only after
# the new release is published and contains both installers plus checksums.
if manifest.get("prune_older_releases") is True:
    published = json.loads(subprocess.check_output(["gh", "api", f"repos/{repo}/releases/tags/{tag}"], text=True))
    if published["draft"] or {a["name"] for a in published["assets"]} != expected_names | {"SHA256SUMS.txt"}:
        raise ValueError("Refusing release cleanup before complete publication")
    current_version = tuple(map(int, version.split(".")))
    removed = []
    while True:
        releases = json.loads(subprocess.check_output(["gh", "api", f"repos/{repo}/releases?per_page=100"], text=True))
        older = [r for r in releases if re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", r["tag_name"]) and tuple(map(int, r["tag_name"][1:].split("."))) < current_version]
        if not older:
            break
        for release in older:
            subprocess.run(["gh", "api", "--method", "DELETE", f"repos/{repo}/releases/{release['id']}"], check=True)
            subprocess.run(["gh", "api", "--method", "DELETE", f"repos/{repo}/git/refs/tags/{release['tag_name']}"], check=True)
            removed.append(release["tag_name"])
    print("Removed superseded public releases:", ", ".join(removed))

