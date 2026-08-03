"""
Standalone test for livekit-plugins-sonex.

Calls the actual plugin class (not the raw HTTP API directly) to confirm
the whole plugin path works: TTS.synthesize() -> ChunkedStream -> real audio
back from SonexLabs.

Since this runs as a standalone script rather than inside a real LiveKit
agent worker, we create our own aiohttp.ClientSession and pass it directly
to the plugin — the plugin's shared http_context session is only available
inside an actual agent worker job context.

Usage:
    $env:SONEX_API_KEY = "vsk_..."
    python test_plugin.py
"""

import asyncio
import wave

import aiohttp

from livekit.plugins import sonex


async def main():
    async with aiohttp.ClientSession() as session:
        tts = sonex.TTS(
            voice_id="721y9crx9v",  # Alok — replace with your real voice ID if different
            http_session=session,
        )

        print(f"Provider: {tts.provider}, Model: {tts.model}, Sample rate: {tts.sample_rate}")

        stream = tts.synthesize("Hello, this is a test of the SonexLabs LiveKit plugin.")

        frame = await stream.collect()
        print(f"Got audio frame: {frame.sample_rate} Hz, {frame.num_channels} channel(s), "
              f"{len(frame.data)} bytes")

        with wave.open("plugin_test_output.wav", "wb") as f:
            f.setnchannels(frame.num_channels)
            f.setsampwidth(2)  # 16-bit PCM
            f.setframerate(frame.sample_rate)
            f.writeframes(bytes(frame.data))

        print("Saved to plugin_test_output.wav — play it to confirm clear speech.")


asyncio.run(main())