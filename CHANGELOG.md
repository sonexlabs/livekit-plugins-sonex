# Changelog

All notable changes to `livekit-plugins-sonex` are documented here.

## [0.2.2] - 2026-08-09
### Changed
- Removed all language-code examples (`"en"`, `"hi"`, etc.) from docs — `language` is optional and defaults to auto-detect.

## [0.2.1] - 2026-08-09
### Fixed
- Replaced a fabricated `voice_id` example with a real ID from `GET /v1/voices`.
- Dropped BCP-47 jargon from language parameter docs.
- Clarified `sample_rate` is not sent to the API — Panini returns audio at its native rate; the value is used for LiveKit-side reporting only.

## [0.2.0] - 2026-08-09
### Changed
- Switched to the `/v1/speech/stream` endpoint for lower time-to-first-audio.
- Reuse LiveKit Agents' shared `aiohttp.ClientSession` instead of opening a new connection per request.

## [0.1.0] - 2026-08-01
### Added
- Initial release of the SonexLabs TTS plugin for LiveKit Agents.
