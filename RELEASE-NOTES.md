# Feather Clip 2.14.2

Choose Update and restart and FeatherClip now handles the handoff automatically:

- Download and verify the release.
- Finish active saves, trim exports and uploads, and preserve settings.
- Close FeatherClip automatically.
- Install the new version and reopen it.

Windows shows installation progress and does not reboot the PC. Mac stages and replaces the installed app automatically instead of requiring DMG drag-and-drop, keeping the previous app as a hidden backup. Mac must be installed in a writable application folder, not running from a DMG.

Saved clips and preferences are preserved. The unsaved rolling buffer resets when the app closes; it is not exported into extra clips. Automatic recovery remains opt-in, motion blur stays capped at 120 FPS, and blur-off retains up to 240 FPS.

Both installer builds and automated checks passed, including Windows installation/relaunch and Mac DMG staging/bundle replacement. Mac interactive reopening/security prompts remain unverified on a physical Mac; existing signing/notarization limitations remain.

Important: your currently installed older updater may need one final manual close/replacement to install 2.14.2. Future updates use the new automatic handoff.
