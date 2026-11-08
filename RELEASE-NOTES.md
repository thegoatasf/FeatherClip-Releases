## Feather Clip 2.13.1

- Check for updates immediately on each fresh app launch, with no 15-second delay.
- Windows checks before recording startup; Mac checks continue after the initial window closes.
- No repeated automatic checks when reopening a window in the same session.
- Checks run asynchronously and stay quiet when up to date or offline. Downloading still requires your confirmation.

Manual check: right-click the Windows tray icon > Check for updates. On Mac, use the Feather Clip app menu or menu-bar icon > Check for updates.

### Included from 2.13.0

- Optional two-frame motion blur on Windows and Mac, off by default.
- Frame-rate settings up to 240 FPS; actual capture depends on your display and encoder.
- New-user video bitrate defaults to 5,000 kbps; existing saved bitrate values are preserved.
- Refreshed indigo/slate Windows panels and library header, plus a clearer Mac capture-status panel and Video settings group.
- Existing capture, audio, library, editing, sharing and update controls are retained.

Windows: Settings > Capture > Video. Mac: sidebar > Video; stop capture before editing video options. Motion blur adds processing and blends adjacent frames rather than estimating object motion.

Install using the setup EXE or drag the Mac app from the DMG into Applications. Existing 2.12.0 apps can use Check for updates. Saved clips and settings are preserved.

Preview installers remain unsigned/unnotarized. Automated tests do not guarantee 240 FPS performance on every device or verify live capture on the newest macOS.
