## Feather Clip Beta 1.0.1 Hotfix

- Windows: smaller live audio packets prevent periodic video stalls and repeated catch-up frames during high-FPS recording.
- Windows: allow longer for the update helper to start on busy systems while keeping the app open until it is ready.
- Windows: removed the minimum source interval that could skip capture updates on high-refresh displays.

The app still displays Beta 1.0.1. Internal build 2.21.3 makes this hotfix available through the updater. Windows and Mac Apple Silicon installers are included; these capture fixes apply to Windows.

Actual capture cadence depends on the source, display and system load. This update addresses the measured audio-related stalls; it does not guarantee a locked 120 or 240 unique frames per second in every game.
