# Feather Clip 2.16.0

- Reduced motion-blur ghosting: native Windows and Mac capture keep the current frame dominant and reduce old-frame blending around sharp changes.
- Windows blur runs in the GPU capture shader, avoiding the extra CPU video conversion. Compatibility capture uses a lighter 80/20 blend.
- Added a bottom-left live readout such as `120 FPS - current: 119`, measured from encoder throughput and refreshed every second.
- The counter expires during stalls and resets between recordings. Static Mac desktops may supply fewer frames.
- Motion blur remains optional and capped at 120 FPS; blur off supports up to 240 FPS.

Validation: native blur pixel/timing tests on Windows and Mac, Windows 1080p120 HDR/NVIDIA moving-source benchmark (45 seconds, average 120 FPS), settings/profile/pin checks, and installer/update handoff tests on both platforms.

Windows installer and Apple Silicon macOS 15+ DMG are included. Existing clips and settings are preserved.
