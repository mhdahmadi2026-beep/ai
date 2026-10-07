# Starter: Persian voice assistant (STT → LLM → TTS)

`pip install openai sounddevice soundfile numpy` · env: `AVALAI_API_KEY`, `AVALAI_STT_MODEL`, `AVALAI_MODEL`, `AVALAI_TTS_MODEL` — **verify all ids live**: legacy STT/TTS ids (whisper-1, gpt-4o-*transcribe*, tts-1…) are being retired (`10b-deprecations-complete.md`).
```python
import os, io, wave, numpy as np, sounddevice as sd, soundfile as sf
from openai import OpenAI
c = OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1", timeout=120)
SR = 16000

def record(seconds=6):
    a = sd.rec(int(seconds * SR), samplerate=SR, channels=1, dtype="int16"); sd.wait()
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(a.tobytes())
    buf.seek(0); buf.name = "in.wav"; return buf

def stt(buf) -> str:
    return c.audio.transcriptions.create(model=os.environ["AVALAI_STT_MODEL"], file=buf, language="fa").text

def think(history):
    r = c.chat.completions.create(model=os.environ["AVALAI_MODEL"], max_completion_tokens=300, messages=[
        {"role": "system", "content": "دستیار صوتی فارسی. حداکثر دو جمله‌ی کوتاه و محاوره‌ای. بدون فهرست و نشانه‌گذاری اضافی."}, *history])
    return r.choices[0].message.content or ""

def tts(text: str):
    r = c.audio.speech.create(model=os.environ["AVALAI_TTS_MODEL"], voice="alloy", input=text, response_format="wav")
    data, sr = sf.read(io.BytesIO(r.content)); sd.play(data, sr); sd.wait()

history = []
while True:
    input("Enter → speak (6s)…")
    q = stt(record()); print("you:", q)
    if not q.strip(): continue
    history.append({"role": "user", "content": q}); a = think(history[-10:]); history.append({"role": "assistant", "content": a})
    print("bot:", a); tts(a)
```
Notes: Gemini TTS (`gemini-3.8-*-tts`) needs `voice={"name":"Zephyr","languageCode":"fa-IR"}` on `/v1/audio/speech` (see `news/2026-09-30-gemini-3-8-tts-models-added.md`); Realtime API is NOT provided → this pipeline is the pattern (latency ≈ STT + LLM + TTS; stream LLM tokens and TTS sentence-by-sentence to cut it). Add VAD (webrtcvad) instead of fixed 6 s; barge-in = stop playback on new speech; consent + privacy for recorded audio. Deeper: `examples/voice-conversational-apps.md`, `examples/processing-audio-chat-completions.md`.
