# Feather Clip 2.18.0

- Added an offline update log on Windows and Mac. It opens once per installed version and can be reopened from Settings > General > View update log.
- Mac now accepts any whole-number frame rate from 5 to 240 FPS instead of a preset dropdown. Invalid drafts keep the last valid setting.
- Motion blur now has a 0-100% strength slider on Windows and Mac, shown only when motion blur is enabled.
- 0% is sharp, 36% preserves the subtle default, and 100% produces a strong two-frame blend with longer trails. Capture remains capped at 120 FPS with blur enabled.
- Blur strength persists in settings and profiles. Older profiles keep the subtle default.
- Future installer builds require a changelog entry for their version.

Validated custom FPS limits, update-log display policy, native GPU 0%/100% blur output, old profile compatibility, settings persistence, Mac click targets, and installer/update handoff on both platforms.

Includes Windows setup and Apple Silicon macOS 15+ DMG. Saved clips and settings are preserved.
