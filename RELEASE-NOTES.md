# Feather Clip 2.14.0

- Smoother button press/release and hover effects on Windows and Mac, plus Windows panel fades. Reduced-motion preferences are respected.
- Fixed a Windows capture catch-up loop that could repeatedly encode an old frame. Capture now reacquires fresh frames while catching up.
- Brief encoder slowdowns no longer immediately trigger overload recovery. Saving while capture is substantially behind shows a clear catch-up message.
- Windows keeps retrying after temporary capture failures instead of giving up after three attempts when automatic recovery is enabled. Mac now retries stream errors too. Stop clipping cancels recovery.
- Capture helpers, encoder probes, thumbnails and exports are tied to the Windows app's lifetime, so FFmpeg is cleaned up when FeatherClip exits or is forcibly ended. Task Manager still controls its visual grouping; one combined usage row is not guaranteed.
- Existing features, saved preferences, motion blur, up-to-240 FPS settings, and launch-time update checks remain available.

Install with FeatherClip-Windows-Setup.exe or FeatherClip-Mac-AppleSilicon.dmg (Apple Silicon, macOS 15+). Existing installations can use Check for updates.

Both installer builds and automated checks passed. Windows live capture, forced encoder recovery, fresh-frame catch-up and helper cleanup were tested locally. Interactive Mac capture/reconnection has not been verified on a physical Mac in this session. Recovery may reset unsaved buffered footage; saved clips remain intact. Installers retain the existing signing/notarization limitations.
