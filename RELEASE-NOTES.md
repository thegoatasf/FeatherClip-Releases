## Feather Clip 2.19.0

- Grid/list clip library views on Windows and Mac; Mac now shows cached video thumbnails.
- Optional motion blur in the editor: save a blurred copy at up to 60 FPS. Best with 120-240 FPS recordings. Preview remains the original; open the saved copy to preview or share the effect. Turn live blur off to avoid its capture-time processing.
- Mac uses encoder-friendly YUV capture when live blur is off. Game-FPS improvement depends on hardware and needs real-device measurement.
- Opening Feather Clip again on Windows reveals the existing tray app.
- Windows pauses recording on lock, clears the unsaved buffer, and starts fresh after unlock if clipping was enabled. No clips are saved automatically.
- New original clip-save sound, optional on both platforms.
- SAVEDLY remains the sharing provider. Streamable and friends/DM features are not included.

Update from Settings > General > Check for updates, or use the tray/menu-bar update command. Saved clips and settings are preserved.

Windows and Apple Silicon Mac installers remain unsigned/not notarized. Native build/export tests passed; physical Mac gaming performance and secure-desktop lock/unlock need real-device validation.
