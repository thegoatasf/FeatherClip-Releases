# Feather Clip 2.14.1

- Motion blur now caps recording at 120 FPS on Windows and Mac. Turn blur off for up to 240 FPS. Your saved FPS preference is preserved.
- Windows motion blur uses up to four filter workers to improve throughput instead of forcing all blending through one worker.
- Automatic capture restart is OFF by default, including upgrades from the old default-on setting. Enable Restart interrupted recording only if you want automatic retries.
- Turning retries off cancels a pending Windows reconnect. Recovery does not automatically save clips.
- The app no longer calls an initial FPS cap “Clipping resumed.”

The complete Windows HDR/NVIDIA capture pipeline passed a 45-second 1080p120 motion-blur test with moving synthetic frames. Gaming load can still reduce available capture performance. Both installers passed automated build/install/media checks; interactive Mac capture has not been verified on a physical Mac in this session.

Use Check for updates or install the Windows EXE / Apple Silicon macOS 15+ DMG. Saved clips and other preferences are preserved. Existing signing/notarization limitations remain.
