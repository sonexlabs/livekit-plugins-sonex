# SonexLabs plugin for LiveKit Agents

[![PyPI](https://img.shields.io/pypi/v/livekit-plugins-sonex)](https://pypi.org/project/livekit-plugins-sonex/)
[![Python](https://img.shields.io/pypi/pyversions/livekit-plugins-sonex)](https://pypi.org/project/livekit-plugins-sonex/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

Support for real-time voice synthesis with [SonexLabs](https://www.sonexlabs.com)' Panini TTS engine in [LiveKit Agents](https://github.com/livekit/agents).

See [docs.sonexlabs.com](https://docs.sonexlabs.com) for full API reference.

## Installation

```bash
pip install livekit-plugins-sonex
```

## Pre-requisites

You'll need an API key from SonexLabs. It can be set as an environment variable:

```bash
export SONEX_API_KEY=vsk_xxxxxxxxx
```

## Usage

```python
from livekit.agents import AgentSession
from livekit.plugins import sonex

session = AgentSession(
    tts=sonex.TTS(
        voice_id="YOUR_VOICE_ID",
    ),
    # ... llm, stt, vad, turn_handling, etc.
)
```

Or pass the API key directly instead of using the environment variable:

```python
tts = sonex.TTS(
    api_key="vsk_xxxxxxxxx",
    voice_id="YOUR_VOICE_ID",
)
```

## Streaming and connection reuse

Synthesis requests are sent to SonexLabs' `/v1/speech/stream` endpoint, so audio is delivered as chunked HTTP as soon as it's generated rather than after the full utterance completes, reducing time-to-first-audio. When no explicit `http_session` is supplied, the plugin uses LiveKit Agents' shared, process-wide `aiohttp.ClientSession`, so connections are pooled and reused across requests instead of being re-established on every call.

## Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `api_key` | `str` | — | SonexLabs API key. Falls back to `SONEX_API_KEY` if not set. |
| `voice_id` | `str` | — | **Required.** Voice ID from `GET /v1/voices`. |
| `language` | `str` | auto-detect | Language code (e.g. `en`, `hi`). Leave unset to auto-detect. |
| `speed` | `float` | `1.0` | Speech rate multiplier. |
| `sample_rate` | `int` | `24000` | Output sample rate in Hz. Not sent to the API — Panini always returns audio at its native rate; this value is used for LiveKit-side reporting only. |
| `base_url` | `str` | `https://api.sonexlabs.com` | SonexLabs API base URL. |
| `http_session` | `aiohttp.ClientSession` | shared session | Optional existing session to reuse. |

## Requirements

- Python >= 3.10
- livekit-agents >= 1.6.7

## Local development

```bash
git clone https://github.com/sonexlabs/livekit-plugins-sonex.git
cd livekit-plugins-sonex
pip install -e .
```

## License

Apache-2.0 — see [LICENSE](LICENSE).

