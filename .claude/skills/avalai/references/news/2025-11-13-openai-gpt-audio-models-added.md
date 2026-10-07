# News 2025-11-13-openai-gpt-audio-models-added: دسترسی به داده‌های صوتی
URL: `https://docs.avalai.ir/fa/news/2025-11-13-openai-gpt-audio-models-added`
**تاریخ:** 1404-08-22 / (2025-11-13)

# مدل‌های صوتی OpenAI اکنون در دسترس است

**تاریخ:** 1404-08-22 / (2025-11-13)

## خلاصه

اولین مدل‌های صوتی عمومی شرکت OpenAI با نام های `gpt-audio` و `gpt-audio-mini`، اکنون در AvalAI در دسترس هستند. این مدل‌ها از ورودی و خروجی صوتی و متنی از طریق Chat Completions API پشتیبانی می‌کنند و امکان ایجاد برنامه‌های مکالمه‌ای با قابلیت‌های صوتی بومی را فراهم می‌آورند. این مدل‌ها از function calling پشتیبانی کرده و قیمت‌گذاری انعطاف‌پذیری برای توکن‌های متنی و صوتی ارائه می‌دهند.


## نمونه درخواست/پاسخ API

### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio",
    "messages": [
      {
        "role": "user",
        "content": "سلام! امروز چطور می‌توانید به من کمک کنید؟"
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "alloy"
    }
  }'
```

### نمونه پاسخ

```json
{
  "id": "chatcmpl-AaBbCcDdEeFfGg",
  "created": 1763042146,
  "model": "gpt-audio-2025-08-28",
  "object": "chat.completion",
  "system_fingerprint": "fp_abc123",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": null,
        "role": "assistant",
        "audio": {
          "id": "audio_abc123xyz",
          "data": "SUQzBAAAAA...[کوتاه‌شده - داده‌های صوتی mp3 رمزگذاری‌شده base64]",
          "expires_at": 1763045747,
          "transcript": "سلام! من اینجا هستم تا در طیف گسترده‌ای از وظایف به شما کمک کنم. می‌توانم به سوالات پاسخ دهم، اطلاعات ارائه کنم، ایده‌های خلاقانه ارائه دهم، در حل مسائل کمک کنم و موارد دیگر. امروز می‌خواهید در چه زمینه‌ای کمک بگیرید؟"
        },
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 75,
    "prompt_tokens": 12,
    "total_tokens": 87,
    "completion_tokens_details": {
      "accepted_prediction_tokens": 0,
      "audio_tokens": 58,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": 0,
      "text_tokens": 17
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0,
      "text_tokens": 12,
      "image_tokens": 0
    }
  },
  "estimated_cost": {
    "unit": "0.0037200000",
    "irt": 422.64,
    "exchange_rate": 113650
  }
}
```

### ذخیره صوت در یک فایل

صدای بازگشتی به‌صورت Base64 در مسیر `choices[0].message.audio.data` قرار می‌گیرد؛ بنابراین یک دستور یک‌باره در ترمینال می‌تواند آن را به یک فایل MP3 تبدیل کند.

**macOS — zsh** (به `jq` نیاز دارد):

```zsh
curl -sS "https://api.avalai.ir/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio",
    "messages": [{"role": "user", "content": "hi"}],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "alloy"
    }
  }' \
  | jq -r '.choices[0].message.audio.data' \
  | base64 -D > output.mp3

afplay output.mp3
```

**لینوکس — bash/zsh** (به `jq` نیاز دارد):

```bash
curl -sS "https://api.avalai.ir/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio",
    "messages": [{"role": "user", "content": "hi"}],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "alloy"
    }
  }' \
  | jq -r '.choices[0].message.audio.data' \
  | base64 --decode >output.mp3

ffplay -nodisp -autoexit output.mp3
```

**ویندوز — PowerShell**:

```powershell
$response = curl.exe -sS "https://api.avalai.ir/v1/chat/completions" `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:AVALAI_API_KEY" `
  -d '{
    "model": "gpt-audio",
    "messages": [{"role": "user", "content": "hi"}],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "alloy"
    }
  }' | ConvertFrom-Json

[IO.File]::WriteAllBytes(
  (Join-Path $PWD "output.mp3"),
  [Convert]::FromBase64String($response.choices[0].message.audio.data)
)

Start-Process .\output.mp3
```

این‌ها دستورهای یک‌باره ترمینال هستند و نیازی نیست چیزی به `.zshrc`، `.bashrc` یا پروفایل PowerShell اضافه شود.

---

## نمونه‌های استفاده از SDK

### تولید پایه متن و صدا

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio",
    "messages": [
      {
        "role": "user",
        "content": "درباره هوش مصنوعی برایم بگو."
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "nova"
    }
  }'

python=:from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("AVALAI_API_KEY"), base_url="https://api.avalai.ir/v1"
)

completion = client.chat.completions.create(
    model="gpt-audio",
    messages=[{"role": "user", "content": "درباره هوش مصنوعی برایم بگو."}],
    modalities=["text", "audio"],
    audio={"format": "mp3", "voice": "nova"},
)

# دسترسی به داده‌های صوتی
audio_data = completion.choices[0].message.audio.data
transcript = completion.choices[0].message.audio.transcript

print(f"متن رونویسی: {transcript}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
    model: "gpt-audio",
    messages: [
        {
            role: "user",
            content: "درباره هوش مصنوعی برایم بگو.",
        },
    ],
    modalities: ["text", "audio"],
    audio: {
        format: "mp3",
        voice: "nova",
    },
});

// دسترسی به داده‌های صوتی
const audioData = completion.choices[0].message.audio.data;
const transcript = completion.choices[0].message.audio.transcript;

console.log(`متن رونویسی: ${transcript}`);

go=:package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	completion, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
		Model: openai.F("gpt-audio"),
		Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
			openai.UserMessage("درباره هوش مصنوعی برایم بگو."),
		}),
		Modalities: openai.F([]openai.ChatCompletionModality{
			openai.ChatCompletionModalityText,
			openai.ChatCompletionModalityAudio,
		}),
		Audio: openai.F(openai.ChatCompletionAudioParam{
			Format: openai.F(openai.ChatCompletionAudioFormatMp3),
			Voice:  openai.F(openai.ChatCompletionAudioVoiceNova),
		}),
	})

	if err != nil {
		panic(err)
	}

	fmt.Printf("متن رونویسی: %s\n", completion.Choices[0].Message.Audio.Transcript)
}

php=:<?php

require 'vendor/autoload.php';

use OpenAI\Client;

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$response = $client->chat()->create([
    'model' => 'gpt-audio',
    'messages' => [
        [
            'role' => 'user',
            'content' => 'درباره هوش مصنوعی برایم بگو.',
        ],
    ],
    'modalities' => ['text', 'audio'],
    'audio' => [
        'format' => 'mp3',
        'voice' => 'nova',
    ],
]);

$audioData = $response['choices'][0]['message']['audio']['data'];
$transcript = $response['choices'][0]['message']['audio']['transcript'];

echo "متن رونویسی: " . $transcript . "\n";

```

### استفاده از gpt-audio-mini برای پردازش مقرون به صرفه

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio-mini",
    "messages": [
      {
        "role": "user",
        "content": "هوای امروز چطور است؟"
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "alloy"
    }
  }'

python=:from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("AVALAI_API_KEY"), base_url="https://api.avalai.ir/v1"
)

completion = client.chat.completions.create(
    model="gpt-audio-mini",
    messages=[{"role": "user", "content": "هوای امروز چطور است؟"}],
    modalities=["text", "audio"],
    audio={"format": "mp3", "voice": "alloy"},
)

print(completion.choices[0].message.audio.transcript)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
    model: "gpt-audio-mini",
    messages: [
        {
            role: "user",
            content: "هوای امروز چطور است؟",
        },
    ],
    modalities: ["text", "audio"],
    audio: {
        format: "mp3",
        voice: "alloy",
    },
});

console.log(completion.choices[0].message.audio.transcript);

go=:package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	completion, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
		Model: openai.F("gpt-audio-mini"),
		Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
			openai.UserMessage("هوای امروز چطور است؟"),
		}),
		Modalities: openai.F([]openai.ChatCompletionModality{
			openai.ChatCompletionModalityText,
			openai.ChatCompletionModalityAudio,
		}),
		Audio: openai.F(openai.ChatCompletionAudioParam{
			Format: openai.F(openai.ChatCompletionAudioFormatMp3),
			Voice:  openai.F(openai.ChatCompletionAudioVoiceAlloy),
		}),
	})

	if err != nil {
		panic(err)
	}

	fmt.Println(completion.Choices[0].Message.Audio.Transcript)
}

php=:<?php

require 'vendor/autoload.php';

use OpenAI\Client;

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$response = $client->chat()->create([
    'model' => 'gpt-audio-mini',
    'messages' => [
        [
            'role' => 'user',
            'content' => 'هوای امروز چطور است؟',
        ],
    ],
    'modalities' => ['text', 'audio'],
    'audio' => [
        'format' => 'mp3',
        'voice' => 'alloy',
    ],
]);

echo $response['choices'][0]['message']['audio']['transcript'] . "\n";

```

### فراخوانی تابع با مدل‌های صوتی

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio",
    "messages": [
      {
        "role": "user",
        "content": "هوای سانفرانسیسکو چطور است؟"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "دریافت اطلاعات هوای فعلی برای یک مکان",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "نام شهر"
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'

python=:from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("AVALAI_API_KEY"), base_url="https://api.avalai.ir/v1"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "دریافت اطلاعات هوای فعلی برای یک مکان",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "نام شهر"}
                },
                "required": ["location"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="gpt-audio",
    messages=[{"role": "user", "content": "هوای سانفرانسیسکو چطور است؟"}],
    tools=tools,
    tool_choice="auto",
)

print(response.choices[0].message.tool_calls)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const tools = [
    {
        type: "function",
        function: {
            name: "get_weather",
            description: "دریافت اطلاعات هوای فعلی برای یک مکان",
            parameters: {
                type: "object",
                properties: {
                    location: {
                        type: "string",
                        description: "نام شهر"
                    }
                },
                required: ["location"]
            }
        }
    }
];

const response = await client.chat.completions.create({
    model: "gpt-audio",
    messages: [
        {
            role: "user",
            content: "هوای سانفرانسیسکو چطور است؟"
        }
    ],
    tools: tools,
    tool_choice: "auto"
});

console.log(response.choices[0].message.tool_calls);

go=:package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	completion, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
		Model: openai.F("gpt-audio"),
		Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
			openai.UserMessage("هوای سانفرانسیسکو چطور است؟"),
		}),
		Tools: openai.F([]openai.ChatCompletionToolParam{
			{
				Type: openai.F(openai.ChatCompletionToolTypeFunction),
				Function: openai.F(openai.FunctionDefinitionParam{
					Name:        openai.String("get_weather"),
					Description: openai.String("دریافت اطلاعات هوای فعلی برای یک مکان"),
					Parameters: openai.F(openai.FunctionParameters{
						"type": "object",
						"properties": map[string]interface{}{
							"location": map[string]interface{}{
								"type":        "string",
								"description": "نام شهر",
							},
						},
						"required": []string{"location"},
					}),
				}),
			},
		}),
		ToolChoice: openai.F[openai.ChatCompletionToolChoiceOptionUnionParam](
			openai.ChatCompletionToolChoiceOptionAuto,
		),
	})

	if err != nil {
		panic(err)
	}

	fmt.Printf("%+v\n", completion.Choices[0].Message.ToolCalls)
}

php=:<?php

require 'vendor/autoload.php';

use OpenAI\Client;

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$response = $client->chat()->create([
    'model' => 'gpt-audio',
    'messages' => [
        [
            'role' => 'user',
            'content' => 'هوای سانفرانسیسکو چطور است؟',
        ],
    ],
    'tools' => [
        [
            'type' => 'function',
 => [
                'name' => 'get_weather',
                'description' => 'دریافت اطلاعات هوای فعلی برای یک مکان',
                'parameters' => [
                    'type' => 'object',
                    'properties' => [
                        'location' => [
                            'type' => 'string',
                            'description' => 'نام شهر',
                        ],
                    ],
                    'required' => ['location'],
                ],
            ],
        ],
    ],
    'tool_choice' => 'auto',
]);

print_r($response['choices'][0]['message']['tool_calls']);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [راهنمای پردازش صوتی](fa/guides/audio-processing.md)
- [مثال ساخت برنامه‌های گفتگو محور با مدل‌های صوتی](fa/examples/building_conversational_apps_with_audio_models.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
