# livekit-plugins-sonex

LiveKit Agents plugin for **SonexLabs Text-to-Speech**.

This package allows LiveKit Agents to synthesize speech using SonexLabs' TTS API through the standard LiveKit plugin interface.

---

## Features

- Native LiveKit Agents integration
- Async HTTP client
- High-quality SonexLabs voices
- Supports LiveKit AgentSession
- Simple pip installation

---

## Installation

```bash
pip install livekit-plugins-sonex
```

For local development:

```bash
git clone https://github.com/sonexlabs/livekit-plugins-sonex.git
cd livekit-plugins-sonex

pip install -e .
```

---

## Authentication

The plugin requires a SonexLabs API key.

You can either pass it directly:

```python
from livekit.plugins import sonex

tts = sonex.TTS(
    api_key="vsk_xxxxxxxxx",
    voice_id="YOUR_VOICE_ID",
)
```

or configure it as an environment variable.

Linux/macOS

```bash
export SONEX_API_KEY=vsk_xxxxxxxxx
```

Windows PowerShell

```powershell
$env:SONEX_API_KEY="vsk_xxxxxxxxx"
```

---

## Usage

```python
from livekit.agents import AgentSession
from livekit.plugins import sonex

session = AgentSession(
    tts=sonex.TTS(
        voice_id="YOUR_VOICE_ID",
    ),
)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| `api_key` | Sonex API key (optional if `SONEX_API_KEY` is set) |
| `voice_id` | Sonex voice ID |
| `language` | Optional language code (e.g. `en`, `hi`). If omitted, Sonex auto-detects the language. |
| `speed` | Speech rate multiplier (default: `1.0`) |
| `sample_rate` | Output sample rate (default: `24000` Hz) |
| `base_url` | SonexLabs API base URL (optional) |
| `http_session` | Optional existing `aiohttp.ClientSession` |

---

## Requirements

- Python 3.10+
- livekit-agents

---

## License

Apache-2.0

