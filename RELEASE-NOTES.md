# Feather Clip 2.17.0

Mac interaction and layout update:
- Fixed-size button hit targets cover the full padded area; hover and press feedback no longer scales the target.
- Controls accept window-activation clicks.
- Clip rows use explicit single-click buttons across their full width.
- Windows-style dark layout with a fixed Clips/Settings sidebar, recording card, clip library, and bottom-left live FPS display.
- Video editing opens in a dedicated panel so playback and trim controls do not crowd the library at smaller window sizes.
- Capture, audio, profiles, pins, trimming, sharing and updates remain available. Active exports prevent dismissing the editor.

Validation: native Mac window mouse-event tests passed at the button center and all four padded edges. Mac encoding, trimming, profiles/pins and automatic-update tests passed. Windows installer and update tests passed.

The friend's exact display/cursor setup has not been reproduced. Please retest the reported clicking issue after updating.

Includes the Apple Silicon macOS 15+ DMG and Windows installer. Saved clips and settings are preserved.
