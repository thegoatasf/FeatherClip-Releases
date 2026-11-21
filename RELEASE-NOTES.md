## Feather Clip Beta 1.0.1 Hotfix

- Sunset palette, Library/Settings icons, FEATHER branding and fewer editor instructions.
- Faster f0e Blur defaults: Fast (4x), Balanced (6x), or Maximum (10x). High-FPS sources reuse their existing frames when sufficient; full-clip Blur exports skip an extra encode. Actual export speed depends on your GPU, drive and settings.
- Blur defaults to 50%. Existing saved capture settings are preserved.
- Scrub and adjust trims during export. The running export uses the selection captured when you pressed Save. Cancel is available in the editor.
- Cut selection removes that section and joins the remaining footage into a new copy, preserving the original.
- Copy link uploads and copies automatically with inline status. Smaller uploads is now in Settings, and recent links copy again without reuploading.
- Fresh FPS is now labeled Captured FPS on Windows.

The displayed version remains Beta 1.0.1. This hotfix uses internal build 2.21.1 so existing installations can detect it. Existing versions check on launch but cannot be forced remotely to install.

Both Windows and Mac Apple Silicon installers are included. Optional f0e Blur still requires one-time setup in the editor. Mac RIFE depends on physical GPU support; frame blending remains available with interpolation disabled.

