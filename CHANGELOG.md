# Changelog

All notable changes to `livekit-plugins-sonex` are documented here.

## [0.2.1 – 0.2.2] - 2026-08-09
### Changed
- Simplified voice and language configuration examples throughout the docs.
- General documentation polish and clarity improvements.

## [0.2.0] - 2026-08-09
### Changed
- Switched to the `/v1/speech/stream` endpoint for lower time-to-first-audio.
- Reuse LiveKit Agents' shared `aiohttp.ClientSession` instead of opening a new connection per request.

## [0.1.0] - 2026-08-01
### Added
- Initial release of the SonexLabs TTS plugin for LiveKit Agents.
