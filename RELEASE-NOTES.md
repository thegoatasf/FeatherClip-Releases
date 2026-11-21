## Feather Clip Beta 1.0.1

- Redesigned Windows and Mac workspace with top navigation, roomier clip previews, search, pinned filtering and a persistent recording status bar. Existing capture, audio, profiles, shortcuts, pins, trimming, sharing and update controls remain available.
- Exported copies automatically open in the editor.
- Optional f0e Blur / RIFE render engine, with 60/120/240 FPS output. Install the official Blur app and CLI once, then link them in the editor. RIFE interpolation can be disabled when unsupported by your GPU. The built-in engine remains available without extra installation. f0e Blur is a separate GPL-3.0 application: https://github.com/f0e/blur
- Fixed the FFmpeg input-option error found in the capture log. Audio queue overflow preserves timing with silence instead of terminating capture; persistent encoder/device failures are still reported.
- Precise Windows frame pacing and a fresh-frame counter distinguish real captured frames from encoded duplicates. Mac real-time encoding disables frame reordering. Actual 240 FPS requires enough fresh frames from the source and sufficient hardware performance.
- Faster SAVEDLY preparation for untrimmed clips, reusable recent links on both platforms, and optional smaller 720p uploads. Network/service speed still limits transfers.
- Update notes show the releases missed since the last acknowledged version. New installs show the current release only.

Internal update build: 2.21.0. Saved clips and settings are preserved. Older public releases are removed after this release is verified and published.

### Optional f0e Blur setup

- **Windows:** install the official Blur release, open it once, then select **Motion blur on export > f0e Blur > Locate Blur CLI** in FeatherClip and choose `blur-cli.exe` from its installation folder.
- **Mac:** install the official Apple Silicon Blur app and extract the separate `blur-cli-macOS-Release-arm64.tar.gz` download. Open Blur once, then choose **Set up Blur** in FeatherClip and select the app and extracted CLI. Keep the Blur app installed at that location.
- RIFE is optional and hardware-dependent. The Mac integration was tested with the official CLI in frame-blending mode; RIFE could not run on the cloud runner's virtual GPU and still needs validation on a physical Mac. Built-in blur works without installing Blur.

