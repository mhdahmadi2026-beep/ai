# Realtime و صوت زنده

مستندات Realtime OpenAI sessionهای صوتی زنده را از APIهای صوتی request-based جدا می‌کند. از این راهنما برای طراحی voice agent، ترجمه زنده و رونویسی streaming استفاده کنید، اما پیاده‌سازی AvalAI را تا وقتی Realtime صریحا برای حساب شما فعال نشده روی routeهای پشتیبانی‌شده نگه دارید.

!> ویژگی پیاده‌سازی نشده!
این قابلیت در حال حاضر در حال توسعه است و هنوز در AvalAI در دسترس نیست. ما انتشار آن را از طریق کانال‌های رسمی خود اعلام خواهیم کرد. منتظر به‌روزرسانی‌های ما باشید!

> این راهنما با اقتباس از [نمای کلی Realtime و صوت در OpenAI](https://developers.openai.com/api/docs/guides/realtime)، [WebRTC](https://developers.openai.com/api/docs/guides/realtime-webrtc)، [WebSocket](https://developers.openai.com/api/docs/guides/realtime-websocket) و [Realtime transcription](https://developers.openai.com/api/docs/guides/realtime-transcription) تهیه شده و endpoint، کلید API، مدل‌ها و نکته‌های دسترسی برای AvalAI تطبیق داده شده است.

!> sessionهای زنده Realtime در حال حاضر به‌عنوان route پشتیبانی‌شده AvalAI در `data/models.json` دیده نمی‌شوند. routeها و model IDهای Realtime در OpenAI را تا زمان اعلام رسمی AvalAI و اضافه شدن model دقیق به داده مدل‌های پشتیبانی‌شده، فقط مرجع معماری بدانید.

!> مثال‌های فعال AvalAI باید از endpointهای صوتی request-based و مدل‌های صوتی Chat Completions استفاده کنند، مگر اینکه route مربوط به Realtime برای حساب انتخابی اعلام شده باشد. پیش از مستندسازی یا استقرار model IDهای live-session، `/v1/models` و صفحه provider را بررسی کنید.

## انتخاب معماری صوتی مناسب

| هدف | مسیر AvalAI | دلیل |
| --- | --- | --- |
| تولید گفتار از متن نهایی | `/v1/audio/speech` | ساده، قابل cache و مناسب برای روایت یا پخش پاسخ دستیار. |
| رونویسی فایل‌های آپلودی | `/v1/audio/transcriptions` | مناسب برای جلسه، زیرنویس، تحلیل و پردازش پس از تماس. |
| reasoning روی گفتار همراه ابزارها | رونویسی → `/v1/responses` → TTS | قابلیت‌های Responses مثل ابزار، state، خروجی ساختاریافته و reasoning را حفظ می‌کند. |
| چت صوتی یک‌مرحله‌ای | `/v1/chat/completions` با `gpt-audio-*` | مناسب برای گفت‌وگوهای کوتاه با ورودی/خروجی صوتی مستقیم. |
| مکالمه زنده مرورگر یا تلفن | معماری Realtime، اگر فعال باشد | برای barge-in، تأخیر کم در اولین صوت، eventهای زنده و turnهای پیوسته لازم است. |
| فقط رونویسی زنده | Realtime transcription، اگر فعال باشد | قبل از کامل شدن utterance، transcript delta پخش می‌کند. |
| ترجمه زنده گفتار | Realtime translation، اگر فعال باشد | از session اختصاصی translation استفاده می‌کند که صوت/متن ترجمه‌شده را پیوسته stream می‌کند. |

## gate مدل‌های صوتی فعلی AvalAI

پیش از انتشار یک مثال runnable برای صوت یا Realtime، پشتیبانی را با `data/models.json` یا پاسخ زنده `/v1/models` بررسی کنید. مجموعه فعلی پشتیبانی‌شده request-oriented است: مدل‌های چت صوتی مثل `gpt-audio`، `gpt-audio-1.5` و `gpt-audio-mini`؛ مدل‌های رونویسی مثل `gpt-transcribe` و `gpt-live-transcribe`؛ و مدل‌های گفتارساز مثل `gpt-audio-1.5`، `gpt-audio` و `gpt-audio-mini`.

از مستندات Realtime OpenAI برای طراحی سیستم‌های کم‌تأخیر آینده استفاده کنید، اما snippetهای runnable در AvalAI را روی مدل‌های پشتیبانی‌شده نگه دارید مگر اینکه همه این بررسی‌ها پاس شوند:

- model ID دقیق Realtime در `data/models.json` وجود داشته باشد یا از `/v1/models` برگردد.
- route در AvalAI اعلام شده باشد، از جمله اینکه WebRTC، WebSocket، SIP یا client secret ساخته‌شده سمت سرور می‌خواهد.
- نام eventها و fieldهای session با route AvalAI تطبیق داشته باشد، نه فقط با نمونه‌های بتای قدیمی OpenAI.
- fallback request-based برای رونویسی → Responses → TTS وجود داشته باشد.

## fallback پشتیبانی‌شده: pipeline صوتی Responses-first

وقتی sessionهای Realtime زنده در دسترس نیستند، از این الگوی production-friendly استفاده کنید. تأخیر آن مثل WebRTC نیست، اما قابل حمل است و اجازه می‌دهد از ابزارها و state در Responses استفاده کنید.

```language-selector
python=:import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("question.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="gpt-transcribe",
        file=audio_file,
        response_format="text",
    )

answer = client.responses.create(
    model="gpt-5.6-luna",
    instructions="به عنوان دستیار صوتی کوتاه‌گو برای توسعه‌دهندگان AvalAI پاسخ بده.",
    input=transcript,
)

speech_path = Path("answer.mp3")
speech = client.audio.speech.create(
    model="gpt-audio-1.5",
    voice="alloy",
    input=answer.output_text,
)
speech.stream_to_file(speech_path)

print(answer.output_text)
print(f"Saved {speech_path}")

javascript=:import fs from "node:fs/promises";
import { createReadStream } from "node:fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const transcript = await client.audio.transcriptions.create({
  model: "gpt-transcribe",
  file: createReadStream("question.mp3"),
  response_format: "text",
});

const answer = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "به عنوان دستیار صوتی کوتاه‌گو برای توسعه‌دهندگان AvalAI پاسخ بده.",
  input: transcript,
});

const speech = await client.audio.speech.create({
  model: "gpt-audio-1.5",
  voice: "alloy",
  input: answer.output_text,
});

await fs.writeFile("answer.mp3", Buffer.from(await speech.arrayBuffer()));
console.log(answer.output_text);

bash=:curl https://api.avalai.ir/v1/audio/transcriptions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F file="@question.mp3" \
  -F model="gpt-transcribe" \
  -F response_format="text"

```

## مفاهیم session در Realtime

وقتی route مربوط به live session فعال باشد، طراحی را حول این مفاهیم Realtime در OpenAI انجام دهید:

- **نوع session:** برای پاسخ دستیار از voice-agent session، برای interpreter صوتی از translation session، و برای متن زنده بدون پاسخ مدل از transcription session استفاده کنید.
- **روش اتصال:** برای capture و playback صوت در مرورگر/موبایل از WebRTC استفاده کنید؛ برای pipelineهای media سمت سرور از WebSocket استفاده کنید؛ فقط وقتی route صریحا در دسترس است، برای طراحی voice agent تلفنی از SIP استفاده کنید.
- **credentialهای موقت:** clientهای مرورگر و موبایل باید client secret کوتاه‌مدت را از سرور شما بگیرند؛ معمولا با flow سمت سرور `POST /v1/realtime/client_secrets` وقتی route فعال باشد. API key بلندمدت را هرگز در کد client قرار ندهید.
- **eventها:** sessionهای زنده eventهای تایپ‌شده client/server ردوبدل می‌کنند. برنامه باید audio delta، transcript delta، tool call، interruption، error و completion eventها را مدیریت کند.
- **شناسه‌های ایمنی:** هنگام ایجاد یا اتصال session، یک شناسه پایدار و حفظ‌کننده حریم خصوصی برای کاربر نهایی bind کنید تا پایش سوءاستفاده به جای کل برنامه روی همان کاربر هدف‌گذاری شود. OpenAI برای Realtime از header به نام `OpenAI-Safety-Identifier` استفاده می‌کند؛ رفتار معادل در route AvalAI را پیش از launch تأیید کنید.
- **flow اختصاصی translation:** sessionهای translation پیوسته هستند و lifecycle معمول turnهای assistant را ندارند. برای translation sessionها `response.create` صدا نزنید؛ audio را stream کنید و audio/transcript delta ترجمه‌شده را مصرف کنید.
- **تنظیم Realtime transcription:** مسیر `gpt-realtime-whisper` در OpenAI سطح‌های delay برای tradeoff بین latency و accuracy دارد. ابتدا latency هدف را تعیین کنید، سپس با میکروفون واقعی، صوت تلفنی، accent، نویز و واژگان دامنه تست کنید؛ نه فقط clipهای synthetic تمیز.
- **شکل GA interface:** integrationهای جدیدتر Realtime در OpenAI header بتا را حذف می‌کنند، client secret موقت را سمت سرور می‌سازند و از نام eventهای جدید مثل `response.output_audio.delta`، `response.output_text.delta` و `response.output_audio_transcript.delta` استفاده می‌کنند. نمونه‌های دوران beta را template پیاده‌سازی جدید در نظر نگیرید؛ آن‌ها را برای migration بررسی کنید.

## نقشه endpointهای Realtime

این شکل‌های GA در OpenAI را مرجع معماری بدانید، سپس پیش از انتشار مثال runnable، پشتیبانی route در AvalAI و `/v1/models` را بررسی کنید:

- **sessionهای voice agent:** sessionهای مکالمه استاندارد به `/v1/realtime` وصل می‌شوند. flowهای WebRTC مرورگر می‌توانند از `/v1/realtime/calls` شروع شوند، و flowهای credential موقت مرورگر/موبایل از `/v1/realtime/client_secrets` استفاده می‌کنند که سرور شما می‌سازد.
- **sessionهای translation:** translation اختصاصی از `/v1/realtime/translations` استفاده می‌کند و OpenAI برای این مسیر `gpt-realtime-translate` را مستند کرده است. تا وقتی این model ID در داده مدل‌های AvalAI و اعلام route دیده نشده، آن را فقط context برنامه‌ریزی بدانید.
- **sessionهای transcription:** OpenAI برای transcript deltaهای streaming مسیر `gpt-realtime-whisper` را مستند کرده است. در AvalAI تا وقتی route رونویسی realtime فعال نشده، از `/v1/audio/transcriptions` به‌صورت request-based استفاده کنید.
- **کنترل server-side با sideband:** ایجاد session WebRTC می‌تواند header نوع `Location` با یک `call_id` برگرداند. سرور قابل اعتماد می‌تواند با همان `call_id` یک WebSocket sideband به همان session باز کند، eventها را monitor کند، `session.update` بفرستد و tool callها را بدون افشای منطق کسب‌وکار به مرورگر پاسخ دهد.
- **شناسه‌های ایمنی:** `OpenAI-Safety-Identifier` یا معادل AvalAI همان route را هنگام ساخت client secret یا realtime call از backend قابل اعتماد بفرستید، نه از کد مرورگر.

## رویدادهای Realtime Transcription

برای live caption بدون پاسخ گفتاری دستیار، طراحی را حول session مخصوص transcription انجام دهید. در شکل فعلی OpenAI، `session.type` روی `transcription` تنظیم می‌شود، audio با `input_audio_buffer.append` stream می‌شود و وقتی turn detection غیرفعال یا در دسترس نیست، با `input_audio_buffer.commit` به‌صورت دستی commit می‌شود. تا وقتی AvalAI route متناظر را اعلام نکرده، این بخش را فقط مرجع معماری بدانید.

```json
{
  "type": "session.update",
  "session": {
    "type": "transcription",
    "audio": {
      "input": {
        "format": {
          "type": "audio/pcm",
          "rate": 24000
        },
        "transcription": {
          "model": "gpt-realtime-whisper",
          "language": "fa",
          "delay": "low"
        },
        "turn_detection": null
      }
    }
  }
}
```

هنگام رسیدن متن جزئی، event نوع `conversation.item.input_audio_transcription.delta` را گوش کنید و وقتی transcript نهایی همان آیتم آماده شد، event نوع `conversation.item.input_audio_transcription.completed` را پردازش کنید. eventهای تکمیل از turnهای مختلف ممکن است خارج از ترتیب نمایش برسند؛ بنابراین deltaها و متن نهایی را با `item_id` تطبیق دهید، نه فقط با ترتیب دریافت event.

```javascript
ws.on("message", (data) => {
  const event = JSON.parse(data);

  if (event.type === "conversation.item.input_audio_transcription.delta") {
    updateCaption(event.item_id, event.delta);
  }

  if (event.type === "conversation.item.input_audio_transcription.completed") {
    finalizeCaption(event.item_id, event.transcript);
  }
});
```

مستندات `gpt-realtime-whisper` در OpenAI سطح‌های `audio.input.transcription.delay` شامل `minimal`، `low`، `medium`، `high` و `xhigh` را معرفی می‌کند. مقدارهای پایین‌تر latency caption را کم می‌کنند؛ مقدارهای بالاتر context صوتی بیشتری به مدل می‌دهند و می‌توانند نرخ خطای کلمه را بهتر کنند. پیش از انتخاب default production، این تنظیمات را با میکروفون واقعی، صوت تلفنی، accent، نویز، code-switching و واژگان دامنه خود benchmark کنید.

## WebRTC، WebSocket و SIP

| Transport | چه زمانی استفاده شود | نکته پیاده‌سازی |
| --- | --- | --- |
| WebRTC | مرورگر یا موبایل مستقیما صوت را capture/play می‌کند | عملکرد رسانه‌ای بهتر؛ ایجاد session را در سرور نگه دارید و از credential موقت استفاده کنید. |
| WebSocket | backend شما صوت خام را از سیستم تماس، worker یا media pipeline می‌گیرد | پایین‌ترین سطح؛ JSON eventها و قطعه‌های صوت base64 را خودتان ارسال و دریافت می‌کنید. همچنین وقتی session WebRTC/SIP یک `call_id` ارائه می‌کند، برای کانال کنترل sideband از آن استفاده کنید. |
| SIP | شماره تلفن یا SIP trunk باید به voice agent وصل شود | معماری مخصوص telephony است؛ flow OpenAI شامل webhook تماس ورودی، کنترل accept/reject/hangup و WebSocket برای مانیتور کردن call است. تا وقتی AvalAI همان routeهای تماس را ارائه نکرده، آن را فقط مرجع معماری بدانید. |
| pipeline request-based | به صوت زنده زیر یک ثانیه نیاز ندارید | ساده‌تر، قابل logتر و پشتیبانی‌شده با endpointهای استاندارد AvalAI. |

## نکته‌های مدیریت event

اگر برای صوت Realtime سمت سرور از WebSocket استفاده می‌کنید، byteهای خروجی در eventهای incremental audio-delta می‌آیند. eventهایی مثل `response.output_audio.done` و `response.done` کامل شدن turn را تأیید می‌کنند، اما خود byteهای صوت را حمل نمی‌کنند. chunkهای `response.output_audio.delta` را هنگام رسیدن buffer یا forward کنید و اگر route پشتیبانی می‌کند format صوت را در سطح session (`session.audio.output.format`) یا در سطح پاسخ (`response.audio.output.format`) تنظیم کنید.

برای playback در مرورگر، تا حد امکان WebRTC را به WebSocket ترجیح دهید. WebRTC برای رسانه client-device در شبکه‌های ناپایدار مقاوم‌تر است، در حالی که WebSocket برای pipelineهای backend مناسب‌تر است که از قبل transport صوت خام را در اختیار دارند.

برای session اختصاصی translation، audio منبع را پیوسته بفرستید، حتی سکوت‌های کوتاه بین عبارت‌ها، و هم deltaهای transcript منبع و هم ترجمه‌شده را مصرف کنید. وقتی stream منبع در translation WebSocket تمام شد، `session.close` بفرستید و تا دریافت `session.closed` eventها را بخوانید تا صوت ترجمه‌شده نهایی از دست نرود.

وقتی route مربوط به Realtime فعال شد، برای eventهای مهم client یک `event_id` بفرستید و آن را همراه هر event نوع `error` لاگ کنید. برخلاف پاسخ‌های HTTP معمولی، خطاهای Realtime می‌توانند async برسند؛ بنابراین `event_id` همان چیزی است که client یا server شما با آن خطا را به action ارسال‌شده وصل می‌کند.

```javascript
const event = {
  event_id: crypto.randomUUID(),
  type: "session.update",
  session: {
    type: "realtime",
    instructions: "کوتاه پاسخ بده و پیش از انجام actionهای حساب کاربری اجازه بگیر.",
  },
};

pendingEvents.set(event.event_id, "session.update");
ws.send(JSON.stringify(event));

ws.on("message", (data) => {
  const serverEvent = JSON.parse(data);

  if (serverEvent.type === "error") {
    const action = pendingEvents.get(serverEvent.event_id) || "unknown event";
    console.error(`Realtime ${action} failed`, serverEvent);
  }
});
```

### چک‌لیست eventهای مکالمه Realtime

وقتی در آینده route مربوط به Realtime در AvalAI فعال شد، به‌جای فرض کردن هر turn به‌عنوان یک request/response ساده، state machine خود را بر اساس eventهای سرور بسازید:

| مرحله | eventهای مهم | اقدام برنامه |
| --- | --- | --- |
| باز شدن session | `session.created` و سپس `session.updated` بعد از `session.update` | session ID را ذخیره کنید، تنظیمات echoشده را بررسی کنید و مدل، voice، حالت VAD، user ID و tenant را log کنید. |
| شروع گفتار کاربر | `input_audio_buffer.speech_started` | playback دستیار را متوقف یا کم‌صدا کنید و turn فعلی کاربر را در حالت recording بگذارید. |
| پایان گفتار کاربر | `input_audio_buffer.speech_stopped` و `input_audio_buffer.committed` | audio buffer را نهایی کنید، transcript pending بسازید و تصمیم بگیرید response خودکار ساخته شود یا نه. |
| رسیدن transcript | `conversation.item.input_audio_transcription.delta` و `.completed` | متن partial و نهایی را با `item_id` تطبیق دهید؛ به ترتیب رسیدن eventها بین turnها تکیه نکنید. |
| stream شدن پاسخ دستیار | `response.output_audio.delta`، `response.output_text.delta`، `response.output_audio_transcript.delta` | audio deltaها را فورا پخش یا buffer کنید، caption را به‌روز کنید و متن partial را از متن نهایی متمایز نشان دهید. |
| ظاهر شدن tool call | `response.function_call_arguments.delta` و سپس `response.done` با آیتم `function_call` | argumentها را validate کنید، toolها را روی سرور مطمئن اجرا کنید، `function_call_output` بفرستید و response بعدی را trigger کنید. |
| پایان turn | `response.output_audio.done`، `response.output_text.done`، `response.done` | transcript نهایی، usage، latency، خروجی ابزارهای انتخاب‌شده و آخرین conversation item ID پایدار را ذخیره کنید. |

## تشخیص نوبت، وقفه و کنترل هزینه

مستندات Realtime OpenAI چند کنترل سطح session دارد که در مثال‌های کوتاه به‌راحتی نادیده گرفته می‌شوند. برای routeهای Realtime آینده AvalAI، این موارد را ورودی طراحی بدانید:

- **تشخیص نوبت:** `server_vad` صوت را بر اساس سکوت بخش‌بندی می‌کند، اما `semantic_vad` صبر می‌کند تا مدل تشخیص دهد کاربر جمله‌اش را تمام کرده است. `threshold`، `prefix_padding_ms` و `silence_duration_ms` را با صوت واقعی production تنظیم کنید. threshold بالاتر در محیط‌های پرنویز کمک می‌کند، اما ممکن است گوینده‌های آرام را از دست بدهد.
- **commit دستی:** در sessionهای transcription با `gpt-realtime-whisper`، `turn_detection` را حذف کنید یا `null` بگذارید و وقتی utterance آماده شد، eventهای commit مربوط به audio buffer را صریح بفرستید.
- **وقفه‌ها:** وقتی کاربر وسط گفتار تولیدشده صحبت می‌کند، ثبت کنید چه مقدار از audio دستیار واقعا پخش شده است. برای بخش پخش‌نشده، event `conversation.item.truncate` بفرستید تا state مکالمه شامل کلماتی نباشد که کاربر هرگز نشنیده است.
- **به‌روزرسانی session:** برای instructions، formatهای صوت، VAD و تنظیمات truncation از `session.update` استفاده کنید. بعضی ویژگی‌ها، مثل voice خروجی انتخاب‌شده، ممکن است بعد از اینکه مدل یک بار audio تولید کرد قابل تغییر نباشند.
- **مدت session:** برای reconnect و انتقال state برنامه داشته باشید؛ sessionهای Realtime در مرجع OpenAI نامحدود نیستند.
- **Truncation زمینه:** sessionهای طولانی در نهایت از سقف context عبور می‌کنند. OpenAI حذف خودکار آیتم‌های قدیمی‌تر، `retention_ratio`، token limit بعد از instructions و غیرفعال کردن truncation همراه با خطای صریح را مستند کرده است. پیش از launch زنده، تعیین کنید کدام رفتار برای محصول شما امن‌تر است.
- **Prompt caching و rate limit:** instructions، تعریف ابزارها، voice خروجی و تنظیمات audio را ثابت نگه دارید تا cache بهتر حفظ شود. در صورت پشتیبانی، eventهای `rate_limits.updated` را گوش کنید و backoff مناسب در UI نشان دهید.
- **کاهش نویز:** اگر route از input audio noise reduction پشتیبانی می‌کند، آن را بر اساس نوع میکروفون و محیط تست کنید. کاهش نویز می‌تواند کیفیت VAD و transcript را بهتر کند، اما باید با زبان، accent و واژگان دامنه هدف ارزیابی شود.

## چک‌لیست production

- با صوت request-based شروع کنید، مگر اینکه turn-taking زنده واقعا محصول را بهتر کند.
- با میکروفون واقعی، صدای تلفنی، accentها، نویز پس‌زمینه و واژگان دامنه benchmark بگیرید.
- پیش از ارائه گفتار زنده به مشتری، VAD، truncation هنگام interruption و رفتار reconnect را تنظیم کنید.
- eventهای rate limit در Realtime را monitor کنید و برای sessionهای طولانی budget بگذارید؛ تغییر تنظیمات session می‌تواند prompt cache را کاهش دهد.
- transcriptها را برای audit/search نگه دارید؛ صوت تولیدشده را فقط وقتی برای playback یا compliance لازم است ذخیره کنید.
- برای رونویسی زنده، تأخیر را در برابر دقت تنظیم کنید و default را فقط از روی صوت تمیز و synthetic انتخاب نکنید.
- برای ترجمه زنده، تا حد امکان trackهای گوینده‌ها را جدا نگه دارید و برای هر زبان مقصد یا جهت مکالمه یک translation session جدا بسازید.
- وقتی صدا با هوش مصنوعی تولید شده، disclosure قابل مشاهده به کاربر بدهید.
- اگر workflow صوتی می‌تواند action انجام دهد، ابزارها را least-privilege طراحی کنید؛ برای خرید، تغییر حساب، ارسال ایمیل و حذف داده approval بگیرید.
- fallback از Realtime به رونویسی → Responses → TTS نگه دارید تا اگر live session شکست خورد محصول همچنان قابل استفاده باشد.

## مرتبط

- [API صوتی](fa/api-reference/audio.md)
- [پردازش صوتی](fa/guides/audio-processing.md)
- [تبدیل گفتار به متن](fa/guides/speech-to-text.md)
- [تبدیل متن به گفتار](fa/guides/text-to-speech.md)
- [ساخت برنامه‌های گفت‌وگومحور با مدل‌های صوتی](fa/examples/building_conversational_apps_with_audio_models.md)
- [API پاسخ‌ها](fa/api-reference/responses.md)
