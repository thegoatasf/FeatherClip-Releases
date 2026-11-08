# Feather Clip 2.15.0

## Settings profiles
Save named settings presets, load them later, replace a saved preset, or delete one. Windows: Settings > Profiles. Mac: Settings profiles in the sidebar. Presets are saved locally and do not change when you edit your current settings afterward. Loading capture settings can restart active recording and reset its unsaved buffer; saved clips are preserved.

## Pinned clips
Use Pin clip / Unpin clip in the clip options menu (Windows) or right-click menu (Mac). Pinned clips stay at the top. Windows storage cleanup never automatically deletes them, and in-app renaming preserves their pin. Deleting a pinned clip yourself requires confirmation. If protected clips exceed the storage quota, they remain protected.

No account or server is needed. Sharing is unchanged.

Both production builds and automated tests passed, including profile persistence and snapshot isolation, pin rename/cleanup protection, existing capture checks and automatic updater handoff. Interactive Mac use remains unverified on a physical Mac in this session; existing signing/notarization limitations remain.
