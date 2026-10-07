# سرویس‌های ویرایش تصویر Stability AI (منسوخ‌شده)

سرویس‌های تخصصی قدیمی ویرایش تصویر Stability AI در حال حاضر در `data/models.json` فهرست نشده‌اند؛ بنابراین مثال‌های قبلی `stability.stable-image-*` مسیر پشتیبانی‌شده AvalAI نیستند. این صفحه فقط به‌عنوان یادداشت مهاجرت برای لینک‌های قدیمی باقی مانده است.

## مسیرهای ویرایش پشتیبانی‌شده

- برای ویرایش با mask، تصویر مرجع، حفظ layout و تغییرات high-fidelity از [`gpt-image-2`](fa/examples/generate_images_with_gpt_image.md#استفاده-از-ماسک-برای-ویرایش-دقیق) استفاده کنید.
- برای ویرایش تصویر BytePlus، در صورت تناسب با اپلیکیشن، از [`seedream-5-0-260128`](fa/examples/generate_images_with_seedream_4.md) یا `seedream-4-5-251128` استفاده کنید.
- برای workflowهای ویرایش تصویر Alibaba از `qwen-image-edit-plus` یا `qwen-image-edit` استفاده کنید.
- پیش از production، [`v1/images/edits`](fa/api-reference/images.md#ویرایش-تصویر-image-editing) را بررسی کنید، چون قابلیت‌های ویرایش به مدل و route وابسته‌اند.

## مثال جایگزین ویرایش

```language-selector
python=:import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("room.png", "rb") as image_file, open("mask.png", "rb") as mask_file:
    response = client.images.edit(
        model="gpt-image-2",
        image=image_file,
        mask=mask_file,
        prompt="Keep the room unchanged, but replace the masked object with a small indoor tree.",
        size="1024x1024",
    )

with open("edited-room.png", "wb") as output_file:
    output_file.write(base64.b64decode(response.data[0].b64_json))

javascript=:import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.edit({
  model: "gpt-image-2",
  image: fs.createReadStream("room.png"),
  mask: fs.createReadStream("mask.png"),
  prompt:
    "Keep the room unchanged, but replace the masked object with a small indoor tree.",
  size: "1024x1024",
});

fs.writeFileSync(
  "edited-room.png",
  Buffer.from(response.data[0].b64_json, "base64")
);




---
hasH1: true
---

# اخبار و به‌روزرسانی‌ها

به بخش اخبار و به‌روزرسانی‌ها خوش آمدید! در اینجا آخرین تحولات، تغییرات و اطلاعیه‌های مربوط به AvalAI را خواهید یافت.

- [۱۴۰۵-۰۷-۰۸: مدل‌های Gemini 3.8 Flash و Flash-Lite TTS در دسترس‌اند](fa/news/2026-09-30-gemini-3-8-tts-models-added.md)
- [۱۴۰۵-۰۷-۰۸: مدل‌های جدید: GPT-6.1 Sol و Claude Sonnet 5.5](fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added.md)
- [۱۴۰۵-۰۷-۰۲: افزودن مدل پرچم‌دار جدید: Claude Opus 5.5](fa/news/2026-09-24-claude-opus-5-5-added.md)
- [۱۴۰۵-۰۷-۰۲: مدل‌های جدید: GPT-6 Sol، GPT-6 Luna و Grok 4.7](fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added.md)
- [۱۴۰۵-۰۶-۲۰: مدل‌های جدید: GPT Image 2.5، DeepSeek V4.1 Flash و Grok 4.6](fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added.md)
- [۱۴۰۵-۰۶-۱۴: افزودن مدل پرچم‌دار جدید: GPT-6 Astra](fa/news/2026-09-05-gpt-6-astra-added.md)
- [۱۴۰۵-۰۶-۱۳: منسوخ شدن گروهی از مدل‌ها و راهنمای مهاجرت](fa/news/2026-09-04-model-deprecations-and-migration-guide.md)
- [۱۴۰۵-۰۶-۱۲: افزودن مدل جدید: Gemini 3.8 Flash](fa/news/2026-09-03-gemini-3-8-flash-added.md)
- [۱۴۰۵-۰۶-۱۱: افزودن مدل پرچم‌دار جدید: Claude Fable 5.1](fa/news/2026-09-02-claude-fable-5-1-added.md)
- [۱۴۰۵-۰۶-۰۷: افزودن مدل‌های جدید: Qwen3.8-27B و Qwen3.8-Flash](fa/news/2026-08-29-qwen3-8-27b-and-qwen3-8-flash-added.md)
- [۱۴۰۵-۰۶-۰۴: افزودن مدل پرچم‌دار جدید: GLM-5.3-Flash](fa/news/2026-08-26-glm-5-3-flash-added.md)
- [۱۴۰۵-۰۵-۲۷: افزودن مدل پرچم‌دار جدید: GLM-5.3](fa/news/2026-08-18-glm-5-3-added.md)
- [۱۴۰۵-۰۵-۲۵: تغییر هدر شناسه درخواست: جایگزینی `x-request-id` با `avalai-request-id`](fa/news/2026-08-16-avalai-request-id-header-migration.md)
- [۱۴۰۵-۰۵-۲۴: مدل وزن‌باز Qwen3.8 و مدل‌های Qwen Image 3 اضافه شدند](fa/news/2026-08-15-qwen3-8-open-weight-and-qwen-image-3-added.md)
- [۱۴۰۵-۰۵-۲۳: قیمت‌گذاری ثابت DeepSeek V4 و ارتقای خودکار V4-Pro-0813](fa/news/2026-08-14-deepseek-v4-fixed-off-peak-pricing.md)
- [۱۴۰۵-۰۵-۲۳: افزودن مدل پرچم‌دار جدید: Gemini 3.7 Flash](fa/news/2026-08-14-gemini-3-7-flash-added.md)
- [۱۴۰۵-۰۵-۲۲: مدل‌های جدید Fireworks.ai و مسیریابی بهتر cache](fa/news/2026-08-13-fireworks-models-cache-aware-routing.md)
- [۱۴۰۵-۰۵-۱۲: افزودن Qwen3.8-Max و ارتقای DeepSeek-V4-Flash](fa/news/2026-08-03-qwen3-8-max-deepseek-v4-flash-upgrade.md)
- [۱۴۰۵-۰۵-۰۵: افزودن مدل پرچم‌دار جدید: Claude Opus 5](fa/news/2026-07-27-claude-opus-5-added.md)
- [۱۴۰۵-۰۴-۳۰: مدل‌های جدید اضافه شدند: Gemini 3.6 Flash و Gemini 3.5 Flash-Lite](fa/news/2026-07-21-gemini-3-6-flash-and-3-5-flash-lite-added.md)
- [۱۴۰۵-۰۴-۲۶: مدل‌های جدید: Kimi K3 و Mistral OCR 4](fa/news/2026-07-17-kimi-k3-mistral-ocr-4-added.md)
- [۱۴۰۵-۰۴-۱۹: مدل‌های جدید: خانواده GPT-5.6 و Grok 4.5](fa/news/2026-07-10-gpt-5-6-grok-4-5-models-added.md)
- [۱۴۰۵-۰۴-۱۰: مدل جدید اضافه شد: Gemini 3.1 Flash Lite Image (Nano Banana 2 Lite)](fa/news/2026-07-01-gemini-3-1-flash-lite-image-added.md)
- [۱۴۰۵-۰۴-۱۰: افزودن مدل پرچم‌دار جدید: Claude Sonnet 5](fa/news/2026-07-01-claude-sonnet-5-added.md)
- [۱۴۰۵-۰۳-۲۸: مدل‌های جدید اضافه شدند: GLM-5.2، Kimi K2.7 Code و ارائه‌دهنده جدید Fireworks.ai با Nemotron-3-Ultra](fa/news/2026-06-18-new-models-glm-kimi-fireworks-nemotron.md)
- [۱۴۰۵-۰۳-۱۷: افزودن مدل پرچم‌دار جدید: MiniMax M3](fa/news/2026-06-07-minimax-m3-added.md)
- [۱۴۰۵-۰۳-۱۵: مدل‌های جدید اضافه شدند: Gemini 3 Pro Image، Gemini 3.1 Flash Image پایدار و Qwen3-Max](fa/news/2026-06-05-gemini-image-stable-and-qwen3-max-added.md)
- [۱۴۰۵-۰۳-۰۷: افزودن مدل پرچم‌دار جدید: Claude Opus 4.8](fa/news/2026-05-28-claude-opus-4-8-added.md)
- [۱۴۰۵-۰۳-۰۱: افزودن مدل پرچم‌دار جدید: Qwen3.7-Max](fa/news/2026-05-22-qwen3-7-max-added.md)
- [۱۴۰۵-۰۲-۲۹: مدل پرچم‌دار Gemini 3.5 Flash اضافه شد و Gemini 3.1 Flash-Lite پایدار منتشر شد](fa/news/2026-05-19-gemini-3-5-flash-and-gemini-3-1-flash-lite-stable-added.md)
- [۱۴۰۵-۰۲-۱۱: افزودن مدل جدید: Grok-4.3](fa/news/2026-05-01-grok-4-3-model-added.md)
- [۱۴۰۵-۰۲-۰۵: افزودن مدل پرچم‌دار جدید: GPT-5.5](fa/news/2026-04-25-gpt-5-5-model-added.md)
- [۱۴۰۵-۰۲-۰۴: افزودن مدل‌های پرچم‌دار جدید: DeepSeek-V4-Flash و DeepSeek-V4-Pro](fa/news/2026-04-24-deepseek-v4-models-added.md)
- [۱۴۰۵-۰۲-۰۳: مدل‌های جدید اضافه شدند: Grok 4.20 پایدار، GPT-Image-2، سری Qwen3.6، Kimi K2.6 و Gemini Embedding 2](fa/news/2026-04-23-new-models-grok-gpt-image-qwen-kimi-gemini-embedding.md)
- [۱۴۰۵-۰۱-۲۸: مدل جدید اضافه شد: Claude Opus 4.7](fa/news/2026-04-17-claude-opus-4-7-added.md)
- [۱۴۰۵-۰۱-۲۳: مدل‌های جدید اضافه شدند: GLM-5.1، GLM-5v-Turbo، Nemotron-3-120B، Gemma 4، Qwen3.6-Plus و Qwen-Image-2.0](fa/news/2026-04-12-new-models-zai-cloudflare-google-alibaba.md)
- [۱۴۰۴-۱۲-۲۷: مدل‌های جدید اضافه شدند: Grok 4.20 Beta، GLM-5-Turbo، GPT-5.4 Mini/Nano و MiniMax M2.7](fa/news/2026-03-18-new-models-grok-glm-gpt-minimax.md)
- [۱۴۰۴-۱۲-۱۹: مدل‌های جدید اضافه شدند: سری GPT-5.4 و Gemini 3.1 Flash-Lite Preview](fa/news/2026-03-10-new-openai-gemini-models-added.md)
- [۱۴۰۴-۱۲-۰۸: مدل جدید اضافه شد: Gemini 3.1 Flash Image Preview (Nano Banana 2)](fa/news/2026-02-27-gemini-3-1-flash-image-preview-added.md)
- [۱۴۰۴-۱۲-۰۶: مدل‌های جدید اضافه شدند: GPT-5.3-Codex، GPT-Audio-1.5، Qwen3.5 Flash، Qwen3-Coder-Next و Seedream 5.0](fa/news/2026-02-25-new-models-openai-alibaba-byteplus.md)
- [۱۴۰۴-۱۲-۰۱: مدل جدید اضافه شد: Gemini 3.1 Pro Preview](fa/news/2026-02-19-gemini-3-1-pro-preview-added.md)
- [۱۴۰۴-۱۱-۳۰: مدل جدید اضافه شد: Claude Sonnet 4.6](fa/news/2026-02-19-claude-sonnet-4-6-added.md)
- [۱۴۰۴-۱۱-۲۸: مدل‌های جدید اضافه شدند: Qwen3.5 Plus، Qwen3.5-397B و MiniMax M2.5](fa/news/2026-02-17-new-models-qwen35-minimax-m25.md)
- [۱۴۰۴-۱۱-۲۶: مدل‌های جدید اضافه شدند: GLM-5، Gen-4.5 و Seedream 4.5](fa/news/2026-02-14-new-models-glm5-gen45-seedream45.md)
- [۱۴۰۴-۱۱-۱۷: مدل جدید اضافه شد: Claude Opus 4.6](fa/news/2026-02-06-claude-opus-4-6-added.md)
- [۱۴۰۴-۱۱-۱۶: مدل‌های جدید: Eleven v3، Kimi k2.5 و به‌روزرسانی‌های Qwen3](fa/news/2026-02-05-new-models-elevenlabs-kimi-alibaba.md)
- [۱۴۰۴-۱۱-۱۴: ارائه‌دهنده جدید: مدل‌های گفتاری ElevenLabs و ۱۲ مدل جدید هوش مصنوعی Cloudflare](fa/news/2026-02-03-elevenlabs-provider-cloudflare-models-added.md)
- [۱۴۰۴-۱۱-۰۹: مدل‌های جدید: GLM-4.7-Flash و GLM-4.7-FlashX از Z.AI و GPT-5.2-Codex از OpenAI](fa/news/2026-01-29-new-zai-openai-models-added.md)
- [۱۴۰۴-۱۰-۱۱: راه‌اندازی آزمایشی API فایل‌ها: مدیریت فایل سازگار با OpenAI](fa/news/2026-01-01-files-api-beta-launched.md)
- [۱۴۰۴-۱۰-۰۷: افزودن پشتیبانی از ارائه‌دهنده MiniMax: مدل‌های استدلال M2.1 اکنون در دسترس](fa/news/2025-12-28-minimax-provider-support-added.md)
- [۱۴۰۴-۱۰-۰۲: بسته‌های اعتباری Alibaba اکنون در دسترس: ۲۰ تا ۳۰ درصد تخفیف در مدل‌های Qwen](fa/news/2025-12-23-alibaba-credit-packages-launched.md)
- [۱۴۰۴-۱۰-۰۲: مدل‌های جدید اضافه شدند: GLM-4.7 از Z.AI و مدل‌های Qwen3-VL، تصویر و ترجمه از Alibaba](fa/news/2025-12-23-new-zai-alibaba-models-added.md)
- [۱۴۰۴-۰۹-۲۶: افزودن مدل جدید: Gemini 3 Flash Preview](fa/news/2025-12-17-gemini-3-flash-preview-added.md)
- [۱۴۰۴-۰۹-۲۶: مدل‌های جدید اضافه شدند: GPT-Image-1.5، FLUX.2 Pro و DeepSeek-V3.2 روی Azure AI](fa/news/2025-12-17-new-image-generation-and-deepseek-models.md)
- [۱۴۰۴-۰۹-۲۴: انتشار مدل‌های پایدار Veo 3.1: مهاجرت از نسخه‌های پیش‌نمایش](fa/news/2025-12-15-veo-3-1-stable-models-released.md)
- [۱۴۰۴-۰۹-۲۴: راه‌اندازی سطح سرویس Flex: ۵۰٪ کاهش قیمت برای مدل‌های منتخب OpenAI](fa/news/2025-12-15-flex-service-tier-launched.md)
- [۱۴۰۳-۰۹-۲۳: افزودن مدل‌های جدید Cohere: Rerank v4 و Azure Embed v4](fa/news/2025-12-14-cohere-rerank-v4-embed-v4-azure-added.md)
- [۱۴۰۴-۰۹-۲۰: افزودن مدل‌های جدید: GPT-5.2 و GPT-5.2 Pro](fa/news/2025-12-11-gpt-5-2-models-added.md)
- [۱۴۰۴-۰۹-۱۵: افزودن مدل‌های جدید: GPT-5.1-Codex-Max و Mistral Large 3](fa/news/2025-12-06-gpt-5-1-codex-max-mistral-large-3-added.md)
- [۱۴۰۴-۰۹-۱۰: افزودن مدل جدید: GPT-5.1 Chat و ارتقاء DeepSeek-V3.2](fa/news/2025-12-01-gpt-5-1-chat-deepseek-v3-2-upgrade.md)
- [۱۴۰۴-۰۹-۰۷: مدل‌های پایه Claude با مسیریابی هوشمند: محدودیت‌های نرخ بالاتر](fa/news/2025-11-28-claude-base-models-smart-routing.md)
- [۱۴۰۴-۰۹-۰۶: راه‌اندازی User API: ردیابی دقیق هزینه و تحلیل استفاده](fa/news/2025-11-27-user-api-launched.md)
- [۱۴۰۴-۰۹-۰۴: افزودن مدل جدید: Claude Opus 4.5](fa/news/2025-11-25-claude-opus-4-5-added.md)
- [۱۴۰۴-۰۹-۰۱: افزودن پشتیبانی از پلتفرم Nvidia NIM: مدل‌های Open Weight متمرکز بر تحقیق](fa/news/2025-11-22-nvidia-nim-platform-support-added.md)
- [۱۴۰۴-۰۹-۰۱: افزودن مدل‌های جدید X.AI: Grok-4.1 Fast Reasoning و Non-Reasoning](fa/news/2025-11-22-grok-4-1-models-added.md)
- [۱۴۰۴-۰۸-۳۰: اضافه شدن Gemini 3 Pro Image Preview و پشتیبانی از ارائه‌دهنده groq](fa/news/2025-11-20-gemini-3-pro-image-groq-provider-added.md)
- [۱۴۰۴-۰۸-۲۸: افزودن پشتیبانی از ارائه‌دهنده RunwayML: تولید ویدیو، ویرایش تصویر و مدل‌های TTS](fa/news/2025-11-19-runwayml-provider-support-added.md)
- [۱۴۰۴-۰۸-۲۷: مدل‌های پیشرفته جدید: Gemini 3 Pro Preview و Kimi K2 Thinking](fa/news/2025-11-18-new-models-gemini-3-pro-kimi-k2-thinking.md)
- [۱۴۰۴-۰۸-۲۷: افزودن مدل‌های تولید ویدیوی Veo 3.1](fa/news/2025-11-18-veo-3-1-video-models-added.md)
- [۱۴۰۴-۰۸-۲۵: افزودن مدل‌های تولید ویدیوی سری Sora-2 و مدل‌های پیشرفته GPT-5.1 Codex](fa/news/2025-11-16-sora-video-models-and-gpt-codex-added.md)
- [۱۴۰۴-۰۸-۲۳: افزودن مدل GPT-5.1](fa/news/2025-11-14-gpt-5-1-model-added.md)
- [۱۴۰۴-۰۸-۲۲: مدل‌های صوتی GPT OpenAI اکنون در دسترس است](fa/news/2025-11-13-openai-gpt-audio-models-added.md)
- [۱۴۰۴-۰۸-۲۰: ارائه‌دهنده Moonshot.ai و مدل‌های Embedding Alibaba اکنون در دسترس هستند](fa/news/2025-11-10-moonshot-ai-alibaba-embeddings-added.md)
- [۱۴۰۴-۰۸-۰۶: Gemini Robotics-ER 1.5 Preview: اولین مدل هوش مصنوعی Gemini برای رباتیک](fa/news/2025-10-28-gemini-robotics-er-model-added.md)
- [۱۴۰۴-۰۸-۰۴: مدل‌های Perplexity Sonar اکنون در دسترس هستند](fa/news/2025-10-26-perplexity-sonar-models-added.md)
- [۱۴۰۴-۰۸-۰۴: API جستجوی وب: 8 ابزار جستجو از ارائه‌دهندگان پیشرو](fa/news/2025-10-26-search-api-launched.md)
- [۱۴۰۴-۰۷-۲۸: افزودن مدل‌های پیشرفته TTS و رونویسی](fa/news/2025-10-20-advanced-tts-and-transcription-models-added.md)
- [۱۴۰۴-۰۷-۲۴: افزودن مدل‌های جدید: Claude Haiku 4.5 و Cohere Embed v4](fa/news/2025-10-15-claude-haiku-4-5-cohere-embed-v4-added.md)
- [۱۴۰۴-۰۷-۲۰: بهبود عملکرد API](fa/news/2025-10-12-api-performance-improvements.md)
- [۱۴۰۴-۰۷-۱۷: انتشار نسخه پایدار Gemini 2.5 Flash Image](fa/news/2025-10-09-gemini-2-5-flash-image-stable-release.md)
- [۱۴۰۴-۰۷-۱۶: افزودن مدل جدید: GPT Image 1 Mini](fa/news/2025-10-08-gpt-image-1-mini-support.md)
- [۱۴۰۴-۰۷-۱۴: مدل GPT-5 Pro اکنون در دسترس است](fa/news/2025-10-06-gpt-5-pro-model-added.md)
- [۱۴۰۴-۰۷-۱۲: افزودن مدل جدید: GLM-4.6 از Z.AI و ارتقاء DeepSeek-V3.2](fa/news/2025-10-04-glm-4-6-and-deepseek-v3-2-updates.md)
- [۱۴۰۴-۰۷-۰۹: Seedream 4.0: مدل پیشرفته تولید تصویر اکنون در دسترس است](fa/news/2025-10-01-seedream-4-0-sota-image-generation-model-added.md)
- [۱۴۰۴-۰۷-۰۷: افزودن مدل جدید: Claude 4.5 Sonnet](fa/news/2025-09-29-claude-4-5-sonnet-model-added.md)
- [۱۴۰۴-۰۷-۰۷: سرویس‌های تخصصی ویرایش تصویر Stability AI اکنون در دسترس](fa/news/2025-09-29-stability-ai-image-editing-services.md)
- [۱۴۰۴-۰۷-۰۶: مدل‌های جدید هوش مصنوعی اضافه شد: GPT-5 Codex، Gemini Flash Latest و Qwen3-Max](fa/news/2025-09-28-new-ai-models-added.md)
- [۱۴۰۴-۰۷-۰۵: اعلان منسوخ شدن مدل‌های سری گوگل جمینای 1.5](fa/news/2025-09-27-google-gemini-models-deprecation.md)
- [۱۴۰۴-۰۷-۰۱: مدل‌های جدید X.AI و Alibaba Qwen، به‌روزرسانی DeepSeek-V3.1-Terminus و بهبود تولید تصویر](fa/news/2025-09-23-new-alibaba-qwen-models-deepseek-v31-terminus-update.md)
- [۱۴۰۴-۰۶-۲۸: گسترش API بومی Gemini: پشتیبانی از تعبیه‌سازی و بهبود عملکرد](fa/news/2025-09-18-gemini-native-api-embedding-support-performance-improvements.md)
- [۱۴۰۴-۰۶-۲۴: به‌روزرسانی‌های مهم: مدل‌های DeepSeek-V3.1، Grok Code Fast 1، و بهبود عملکرد استریمینگ](fa/news/2025-09-14-deepseek-v3-1-grok-code-fast-1-streaming-improvements.md)
- [۱۴۰۴-۰۶-۱۸: مدل جدید اضافه شد: Qwen3-Max-Preview با عملکرد بهبود یافته و بهبود پایداری سرویس](fa/news/2025-09-09-qwen3-max-preview-added.md)
- [۱۴۰۴-۰۶-۱۱: مدل‌های جدید هوش مصنوعی Cloudflare در AvalAI](fa/news/2025-09-01-cloudflare-ai-models-added.md)
- [۱۴۰۴-۰۶-۰۵: قابلیت‌های جدید تولید و ویرایش تصویر: Gemini 2.5 Flash Image Preview و گسترش پشتیبانی Edit Endpoint](fa/news/2025-08-26-gemini-2-5-flash-image-preview-and-image-edit-endpoint-expansion.md)
- [۱۴۰۴-۰۶-۰۳: مدل‌های جدید اضافه شد: Imagen 4.0 پایدار، DeepSeek-V3.1، و مدل‌های FLUX](fa/news/2025-08-24-stable-imagen-deepseek-flux-models.md)
- [۱۴۰۴-۰۵-۲۱: مدل‌های جدید اضافه شد: اولین مدل‌های متن‌باز OpenAI و بهبودهای عملکرد API](fa/news/2025-08-12-new-openai-open-source-models.md)
- [۱۴۰۴-۰۵-۱۸: مدل‌های پیشرفته جدید اضافه شد: سری GPT-5 و Claude Opus 4.1](fa/news/2025-08-08-gpt5-opus41-models-added.md)
- [۱۴۰۴-۰۵-۰۹: پشتیبانی کامل از مدل‌های Alibaba اکنون در دسترس است](fa/news/2025-07-31-alibaba-dashscope-support-added.md)
- [۱۴۰۴-۰۴-۳۱: پشتیبانی بومی از API Gemini اکنون در دسترس است](fa/news/2025-07-22-native-gemini-api-support-now-available.md)
- [۱۴۰۴-۰۴-۲۳: افزودن مدل جدید X.AI: Grok-4](fa/news/2025-07-14-grok-4-model-added.md)
- [۱۴۰۴-۰۴-۱۷: افزودن مدل‌های تحقیقاتی جدید OpenAI و Google Imagen 4.0](fa/news/2025-07-08-new-openai-google-models.md)
- [۱۴۰۴-۰۴-۱۶: بسته‌های اعتباری اکنون در دسترس: تا ۷۰٪ صرفه‌جویی در استفاده از مدل‌های هوش مصنوعی](fa/news/2025-07-07-credit-packages-launched.md)
- [۱۴۰۴-۰۴-۰۸: مدل‌های پایدار سری Gemini 2.5 منتشر شدند: نام‌های جدید مدل‌ها در دسترس](fa/news/2025-06-28-gemini-2-5-stable-models-released.md)
- [۱۴۰۴-۰۳-۲۵: گسترش دسترسی API از طریق سه دامنه جدید](fa/news/2025-06-15-expanded-api-access-domains.md)
- [۱۴۰۴-۰۳-۱۹: پشتیبانی SDK Anthropic از چندین ارائه دهنده و افزودن مدل‌های جدید](fa/news/2025-06-09-anthropic-sdk-multi-provider-support.md)
- [۱۴۰۴-۰۳-۱۳: پشتیبانی از SDK رسمی Anthropic به AvalAI اضافه شد](fa/news/2025-06-03-anthropic-sdk-support-added.md)
- [۱۴۰۴-۰۳-۰۹: مدل‌های جدید اضافه شدند: مدل‌های تبدیل متن به گفتار Gemini و Mistral Small](fa/news/2025-05-29-new-tts-models-added.md)
- [۱۴۰۴-۰۳-۰۵: مدل‌های جدید هوش مصنوعی اضافه شدند: Codestral، Gemma 3 و Imagen 4.0](fa/news/2025-05-25-new-ai-models-added.md)
- [۱۴۰۴-۰۳-۰۳: افزودن مدل‌های Claude 4 به AvalAI](fa/news/2025-05-24-claude-4-models-added.md)
- [۱۴۰۴-۰۳-۰۱: به‌روزرسانی‌های داشبورد و مدل Gemini 2.5 Flash](fa/news/2025-05-22-dashboard-updates-and-gemini-flash.md)
- [۱۴۰۴-۰۲-۲۶: افزودن مدل جدید: Mistral OCR Latest](fa/news/2025-05-15-mistral-ocr-latest-added.md)
- [۱۴۰۴-۰۲-۲۵: افزودن مدل‌های o1-pro و o3 به سطوح دسترسی AvalAI](fa/news/2025-05-14-new-models-added-to-tiers.md)
- [۱۴۰۴-۰۲-۲۴: افزودن مدل جدید Alibaba Qwen3، ابزار جستجوی وب و نقطه پایانی Rerank به AvalAI](fa/news/2025-05-13-new-features.md)
- [۱۴۰۴-۰۲-۱۴: بروزرسانی دیکشنری پاسخ (Response) و افزودن مدل‌های جدید OpenAI، Stability](fa/news/2025-05-04-gpt-4o-mini-tts-added.md)
- [۱۴۰۴-۰۲-۰۶: افزودن مدل‌های جدید OpenAI - مدل GPT Image 1](fa/news/2025-04-26-gpt-image-1-support.md)
- [۱۴۰۴-۰۲-۰۵: افزودن مدل‌های جدید Anthropic، OpenAI و Google](fa/news/2025-04-25-new-models-added.md)
- [۱۴۰۴-۰۱-۲۳: افزودن مدل‌های Grok، GPT-4o، Llama-4 و Qwen](fa/news/2025-04-12-new-models-added.md)



```
