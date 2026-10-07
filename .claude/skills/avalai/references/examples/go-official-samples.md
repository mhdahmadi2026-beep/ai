# Go samples extracted verbatim from the AvalAI docs (113 blocks)

Grouped by source page. These are the docs' own samples — several are **known broken or stale** (wrong constructor names, stale model ids, fictional helpers). Treat as intent, then use `examples/multi-language-clients.md` + `examples/laravel-complete-guide.md` for vetted code. Always replace model ids after `scripts/avalai_live.py check`.

## API تنظیم دقیق (Fine-tuning)
_source: source-archive/API-تنظیم-دقیق-Fine-tuning-1258de.md_

### ایجاد یک کار تنظیم دقیق
```go
// مثال Go: ایجاد یک کار تنظیم دقیق از طریق AvalAI
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY") // یا با کلید خود جایگزین کنید
	if apiKey == "" {
		fmt.Println("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}
	baseURL := "https://api.avalai.ir/v1" // از URL پایه AvalAI استفاده کنید

	config := openai.DefaultConfig(apiKey)
	config.BaseURL = baseURL
	client := openai.NewClientWithConfig(config)

	req := openai.FineTuningJobRequest{
		Model:          "fine-tunable-model-id",
		TrainingFile:   "file-abc123",
		ValidationFile: "file-def456", // اختیاری
		Hyperparameters: &openai.Hyperparameters{
			NEpochs: 4, // اختیاری، مقدار نمونه
		},
		// Suffix: "my-custom-model", // اختیاری
	}

	resp, err := client.CreateFineTuningJob(context.Background(), req)
	if err != nil {
		fmt.Printf("خطا در ایجاد کار تنظیم دقیق: %v\n", err)
		return
	}

	fmt.Printf("کار تنظیم دقیق ایجاد شد: %+v\n", resp)
}
```


## API تکمیل گفتگو (Chat Completions)
_source: source-archive/API-تکمیل-گفتگو-Chat-Completions-720a31.md_

### تکمیل گفتگوی پایه
```go
# مثال گو (Go)
package main

import (
"context"
"fmt"
openai "github.com/openai/openai-go"
)

func main() {
    client := openai.NewClient("AVALAI_API_KEY")
    client.BaseURL = "https://api.avalai.ir/v1"

    resp, err := client.CreateChatCompletion(
    context.Background(),
    openai.ChatCompletionRequest{
        Model: "gpt-5.6-sol",
        Messages: []openai.ChatCompletionMessage{
            {
                Role: openai.ChatMessageRoleSystem,
                Content: "You are a helpful assistant.",
            },
            {
                Role: openai.ChatMessageRoleUser,
                Content: "Hello!",
            },
        },
    },
    )

    if err != nil {
        fmt.Printf("ChatCompletion error: %v\n", err)
        return
    }

    fmt.Println(resp.Choices[0].Message.Content) // دسترسی صحیح به محتوای پاسخ
}
```

### تولید صوتی پایه
```go
package main

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
			openai.UserMessage("محاسبات کوانتومی را به زبان ساده توضیح بده."),
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

	fmt.Printf("Audio Data: %s\n", completion.Choices[0].Message.Audio.Data)
	fmt.Printf("Transcript: %s\n", completion.Choices[0].Message.Audio.Transcript)
}
```


## Responses در مقابل Chat Completions
_source: source-archive/Responses-در-مقابل-Chat-Completions-41c940.md_

### مثال تولید متن
```go
// Chat Completions API
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go/v3"
	"github.com/openai/openai-go/v3/option"
	"github.com/openai/openai-go/v3/responses"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	// Chat Completions API
	completion, err := client.Chat.Completions.New(
		context.Background(),
		openai.ChatCompletionNewParams{
			Model: openai.F(openai.ChatModel("gpt-5.6-luna")),
			Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
				openai.UserMessage("یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس."),
			}),
		},
	)
	if err != nil {
		panic(err)
	}
	fmt.Println(completion.Choices[0].Message.Content)

	// Responses API
	response, err := client.Responses.New(
		context.Background(),
		openai.ResponseNewParams{
			model: "gpt-5.6-luna",
			Input: responses.ResponseNewParamsInputUnion{
				OfString: openai.String("یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس."),
			},
		},
	)
	if err != nil {
		panic(err)
	}
	fmt.Println(response.OutputText())
}
```


## ابزار جستجوی وب
_source: source-archive/ابزار-جستجوی-وب-0b5010.md_

### مثال ابزار جستجوی وب
```go
package main

import (
	"context"
	"fmt"
	"github.com/openai/openai-go" // کلاینت Go OpenAI
	"github.com/openai/openai-go/option"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	client := openai.NewClient(
		option.WithAPIKey(apiKey),
		option.WithBaseURL("https://api.avalai.ir/v1"), // استفاده از نقطه پایانی سفارشی
	)

	resp, err := client.Responses.Create(
		context.Background(),
		openai.ResponsesCreateParams{
			model: "gpt-5.6-luna",
			Tools: []openai.ToolParamUnion{
				openai.ToolParam{
					Type: openai.F("web_search"),
				},
			},
			Input: "یک خبر مثبت از امروز چه بود؟",
		},
	)

	if err != nil {
		fmt.Printf("خطای ایجاد پاسخ: %v\n", err)
		return
	}

	fmt.Println(resp.OutputText)
}
```

### سفارشی‌سازی موقعیت مکانی کاربر
```go
package main

import (
	"context"
	"fmt"
	"github.com/openai/openai-go" // کلاینت Go OpenAI
	"github.com/openai/openai-go/option"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	client := openai.NewClient(
		option.WithAPIKey(apiKey),
		option.WithBaseURL("https://api.avalai.ir/v1"), // استفاده از نقطه پایانی سفارشی
	)

	resp, err := client.Responses.Create(
		context.Background(),
		openai.ResponsesCreateParams{
			model: "gpt-5.6-luna",
			Tools: []openai.ToolParamUnion{
				openai.ToolParam{
					Type: openai.F("web_search"),
					UserLocation: &openai.UserLocation{
						Type:    openai.F("approximate"),
						Country: openai.F("GB"),
						City:    openai.F("London"),
						Region:  openai.F("London"),
					},
				},
			},
			Input: "بهترین رستوران‌های اطراف میدان گرنری کدامند؟",
		},
	)

	if err != nil {
		fmt.Printf("خطای ایجاد پاسخ: %v\n", err)
		return
	}

	fmt.Println(resp.OutputText)
}
```

### سفارشی‌سازی اندازه زمینه جستجو
```go
package main

import (
	"context"
	"fmt"
	"github.com/openai/openai-go" // کلاینت Go OpenAI
	"github.com/openai/openai-go/option"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	client := openai.NewClient(
		option.WithAPIKey(apiKey),
		option.WithBaseURL("https://api.avalai.ir/v1"), // استفاده از نقطه پایانی سفارشی
	)

	resp, err := client.Responses.Create(
		context.Background(),
		openai.ResponsesCreateParams{
			model: "gpt-5.6-luna",
			Tools: []openai.ToolParamUnion{
				openai.ToolParam{
					Type:              openai.F("web_search"),
					SearchContextSize: openai.F("low"),
				},
			},
			Input: "کدام فیلم در سال ۲۰۲۵ برنده بهترین فیلم شد؟",
		},
	)

	if err != nil {
		fmt.Printf("خطای ایجاد پاسخ: %v\n", err)
		return
	}

	fmt.Println(resp.OutputText)
}
```


## ابزارها
_source: source-archive/ابزارها-673bf2.md_

### ابزارها
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	payload := map[string]any{
		"model": "gpt-5.6-luna",
		"tools": []map[string]string{{"type": "web_search"}},
		"input": "What was a positive news story from today?",
	}

	body, err := json.Marshal(payload)
	if err != nil {
		panic(err)
	}

	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/responses", bytes.NewBuffer(body))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	responseBody, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(responseBody))
}
```


## استفاده از API جستجوی v1/search
_source: source-archive/استفاده-از-API-جستجوی-v1-search-a402d1.md_

### روش 1: مشخص کردن ابزار در URL
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	requestBody, _ := json.Marshal(map[string]interface{}{
		"query":       "آخرین پیشرفت‌ها در محاسبات کوانتومی",
		"max_results": 5,
	})

	req, _ := http.NewRequest("POST",
		"https://api.avalai.ir/v1/search/perplexity-search",
		bytes.NewBuffer(requestBody))

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	fmt.Println(string(body))
}
```

### روش 2: مشخص کردن ابزار در بدنه درخواست
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

type SearchRequest struct {
	SearchToolName string `json:"search_tool_name"`
	Query          string `json:"query"`
	MaxResults     int    `json:"max_results"`
}

type SearchResult struct {
	Title   string `json:"title"`
	URL     string `json:"url"`
	Snippet string `json:"snippet"`
}

type SearchResponse struct {
	Results []SearchResult `json:"results"`
}

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	searchReq := SearchRequest{
		SearchToolName: "tavily-search",
		Query:          "تاثیر تغییرات اقلیمی بر یخ‌های قطبی",
		MaxResults:     10,
	}

	requestBody, _ := json.Marshal(searchReq)

	req, _ := http.NewRequest("POST",
		"https://api.avalai.ir/v1/search",
		bytes.NewBuffer(requestBody))

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)

	var searchResp SearchResponse
	json.Unmarshal(body, &searchResp)

	for _, result := range searchResp.Results {
		fmt.Printf("عنوان: %s\n", result.Title)
		fmt.Printf("URL: %s\n", result.URL)
		fmt.Printf("اسنیپت: %s\n", result.Snippet)
		fmt.Println("---")
	}
}
```


## استفاده از قابلیت‌های جستجوی وب در مدل‌های زبانی بزرگ (LLM)
_source: source-archive/استفاده-از-قابلیت-های-جستجوی-وب-در-مدل-های-زبانی-ب-760462.md_

### جستجوی داخلی با مدل‌های OpenAI
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gpt-4o-search-preview",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: "what's the news today?",
				},
			},
			ResponseFormat: &openai.ChatCompletionResponseFormat{
				Type: openai.ChatCompletionResponseFormatTypeText,
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	// چاپ پاسخ
	fmt.Println(resp.Choices[0].Message.Content)
}
```

### جستجو با مدل‌های OpenAI از طریق ابزار
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.CreateResponse(
		context.Background(),
		openai.ResponseRequest{
			model: "gpt-5.6-luna",
			Tools: []openai.Tool{
				{
					Type: "web_search",
				},
			},
			Input: "What was a positive news story from today?",
		},
	)

	if err != nil {
		fmt.Printf("Response error: %v\n", err)
		return
	}

	// چاپ متن خروجی
	fmt.Println(resp.OutputText)
}
```

### جستجو با مدل‌های Gemini
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gemini-2.5-flash",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: "You are a helpful assistant.",
				},
				{
					Role:    openai.ChatMessageRoleUser,
					Content: "whats the news?",
				},
			},
			Tools: []openai.Tool{
				{
					GoogleSearch: &openai.GoogleSearchTool{},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
$apiKey = getenv('AVALAI_API_KEY'); // Or replace with your actual key: 'aa-YOUR_API_KEY'

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

// Your custom base URL
$customBaseUrl = 'https://api.avalai.ir/v1';

// Create a custom client instance using the factory
$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();
	// چاپ پاسخ
	fmt.Println(resp.Choices[0].Message.Content)
}
```

### جستجوی اخبار روز
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gpt-4o-search-preview",
$apiKey = getenv('AVALAI_API_KEY'); // Or replace with your actual key: 'aa-YOUR_API_KEY'

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

// Your custom base URL
$customBaseUrl = 'https://api.avalai.ir/v1';

// Create a custom client instance using the factory
$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();		Role:    openai.ChatMessageRoleUser,
					Content: "What are the major headlines today?",
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	// چاپ پاسخ
	fmt.Println(resp.Choices[0].Message.Content)
}
```

### پاسخ به پرسش‌های مبتنی بر واقعیت
```go
package main

import (
	"context"
	"fmt"
$apiKey = getenv('AVALAI_API_KEY'); // Or replace with your actual key: 'aa-YOUR_API_KEY'

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

// Your custom base URL
$customBaseUrl = 'https://api.avalai.ir/v1';

// Create a custom client instance using the factory
$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();
func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gpt-4o-search-preview",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: "Who won the most recent Nobel Prize in Physics and what was their contribution?",
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
$apiKey = getenv('AVALAI_API_KEY'); // Or replace with your actual key: 'aa-YOUR_API_KEY'

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

// Your custom base URL
$customBaseUrl = 'https://api.avalai.ir/v1';

// Create a custom client instance using the factory
$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();
	// چاپ پاسخ
	fmt.Println(resp.Choices[0].Message.Content)
}
```

### پارامترهای جستجو برای مدل‌های Gemini
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gemini-2.5-flash",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: "What are the latest developments in quantum computing?",
				},
			},
			Tools: []openai.Tool{
$apiKey = getenv('AVALAI_API_KEY'); // Or replace with your actual key: 'aa-YOUR_API_KEY'

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

// Your custom base URL
$customBaseUrl = 'https://api.avalai.ir/v1';

// Create a custom client instance using the factory
$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();			DetailLevel: "high",
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	// چاپ پاسخ
	fmt.Println(resp.Choices[0].Message.Content)
}
```

### نحوه پردازش ارجاعات
```go
// برای API پاسخ‌ها
resp, err := client.CreateResponse(
	context.Background(),
	openai.ResponseRequest{
		model: "gpt-5.6-luna",
		Tools: []openai.Tool{
			{
				Type: "web_search",
			},
		},
		Input: "What was a positive news story from today?",
	},
)

if err != nil {
	fmt.Printf("Response error: %v\n", err)
	return
}

// استخراج استنادات
content := resp.OutputText
annotations := resp.Annotations

for _, annotation := range annotations {
	if annotation.Type == "url_citation" {
		url := annotation.URL
		title := annotation.Title
		start := annotation.StartIndex
		end := annotation.EndIndex

		// پردازش استناد بر اساس نیاز
		fmt.Printf("Citation: %s - %s\n", title, url)
	}
}
```


## بهترین شیوه‌های Production
_source: source-archive/بهترین-شیوه-های-Production-010cee.md_

### پاسخ‌های جریانی (Streaming)
```go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(
		os.Getenv("AVALAI_API_KEY"),
		openai.WithBaseURL("https://api.avalai.ir/v1"),
	)

	req := openai.ChatCompletionRequest{
		model: "gpt-5.6-luna",
		Messages: []openai.ChatCompletionMessage{
			{
				Role:    "user",
				Content: "داستانی درباره یک کاوشگر فضایی بنویس",
			},
		},
		Stream: true,
	}

	stream, err := client.CreateChatCompletionStream(context.Background(), req)
	if err != nil {
		fmt.Printf("Stream error: %v\n", err)
		os.Exit(1)
	}
	defer stream.Close()

	for {
		response, err := stream.Recv()
		if err != nil {
			break
		}
		if len(response.Choices) > 0 && response.Choices[0].Delta.Content != "" {
			fmt.Print(response.Choices[0].Delta.Content)
		}
	}
}
```

### پردازش ناهمزمان
```go
package main

import (
	"context"
	"fmt"
	"sync"

	"github.com/openai/openai-go"
)

func generateResponse(client *openai.Client, prompt string, wg *sync.WaitGroup, results map[int]string, index int) {
	defer wg.Done()

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    "user",
					Content: prompt,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}

	results[index] = resp.Choices[0].Message.Content
}

func main() {
	client := openai.NewClient(
		"AVALAI_API_KEY",
		openai.WithBaseURL("https://api.avalai.ir/v1"),
	)

	prompts := []string{"سلام", "حالت چطوره؟", "هوا چطوره؟"}
	results := make(map[int]string)

	var wg sync.WaitGroup
	for i, prompt := range prompts {
		wg.Add(1)
		go generateResponse(client, prompt, &wg, results, i)
	}

	wg.Wait()

	for i := 0; i < len(prompts); i++ {
		fmt.Printf("نتیجه %d: %s\n", i, results[i])
	}
}
```


## بهترین شیوه‌های RAG
_source: source-archive/بهترین-شیوه-های-RAG-061e85.md_

### بهترین شیوه‌ها
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go" // کتابخانه رسمی OpenAI Go
	"strings"
)

func classifyQuery(client *openai.Client, query string) (bool, error) {
	// تعیین می‌کند که آیا یک پرس و جو نیاز به بازیابی خارجی دارد
	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleSystem,
					Content: "You are a query classifier. Respond with 'RETRIEVE' if the query requires external knowledge, or 'SUFFICIENT' if the model's knowledge is enough.",
				},
				{
					Role:    openai.ChatMessageRoleUser,
					Content: query,
				},
			},
		},
	)

	if err != nil {
		return false, err
	}

	classification := resp.Choices[0].Message.Content
	return strings.Contains(classification, "RETRIEVE"), nil
}

func main() {
	client := openai.NewClient("YOUR_AVALAI_API_KEY")
	client.BaseURL = "https://api.avalai.ir/v1" // نقطه پایانی AvalAI API

	query := "What were the key announcements at AvalAI's 2025 developer conference?"
	needsRetrieval, err := classifyQuery(client, query)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	if needsRetrieval {
		// ادامه با جریان کاری RAG
		fmt.Println("درحال بازیابی اطلاعات خارجی...")
	} else {
		// استفاده از تکمیل استاندارد
		fmt.Println("درحال استفاده از دانش داخلی مدل...")
	}
}
```

### بهترین شیوه‌ها
```go
package main

import (
	"fmt"
	"strings"
	"unicode"

	"github.com/neurosnap/sentences" // کتابخانه برای تکه‌بندی جملات
)

// ChunkDocumentBySentences یک سند را بر اساس جملات با همپوشانی مشخص شده تکه‌بندی می‌کند
func ChunkDocumentBySentences(document string, maxChunkSize int, overlap int) []string {
	// راه‌اندازی tokenizer جمله
	tokenizer, err := sentences.NewSentenceTokenizer(nil)
	if err != nil {
		panic(err) // در یک برنامه واقعی، خطا را به شکل مناسب‌تری مدیریت کنید
	}

	// تقسیم سند به جملات
	sentenceObjects := tokenizer.Tokenize(document)
	var sentenceTexts []string
	for _, s := range sentenceObjects {
		sentenceTexts = append(sentenceTexts, s.Text)
	}

	chunks := []string{}
	currentChunk := []string{}
	currentSize := 0

	for _, sentence := range sentenceTexts {
		// تعداد تقریبی توکن (کلمات + علائم نگارشی)
		sentenceSize := len(strings.FieldsFunc(sentence, func(r rune) bool {
			return unicode.IsSpace(r)
		}))

		if currentSize+sentenceSize > maxChunkSize && len(currentChunk) > 0 {
			// ذخیره تکه فعلی
			chunks = append(chunks, strings.Join(currentChunk, " "))

			// حفظ جملات همپوشانی برای تکه بعدی
			if overlap > 0 {
				startIdx := len(currentChunk) - min(overlap, len(currentChunk))
				overlapSentences := currentChunk[startIdx:]
				currentChunk = overlapSentences

				// محاسبه مجدد اندازه فعلی
				currentSize = 0
				for _, s := range overlapSentences {
					currentSize += len(strings.FieldsFunc(s, func(r rune) bool {
						return unicode.IsSpace(r)
					}))
				}
			} else {
				currentChunk = []string{}
				currentSize = 0
			}
		}

		currentChunk = append(currentChunk, sentence)
		currentSize += sentenceSize
	}

	// اضافه کردن آخرین تکه اگر خالی نیست
	if len(currentChunk) > 0 {
		chunks = append(chunks, strings.Join(currentChunk, " "))
	}

	return chunks
}

// تابع کمکی برای min
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	document := `
AvalAI provides access to a wide range of language models through a unified API.
This makes it easy to experiment with different models and choose the best one for your use case.
The platform supports models from various providers including OpenAI, Anthropic, Google, and more.
Each model has different capabilities and pricing, so it's important to understand the tradeoffs.
AvalAI also provides tools for monitoring usage, managing costs, and ensuring compliance with usage policies.
`

	chunks := ChunkDocumentBySentences(document, 100, 1)
	for i, chunk := range chunks {
		fmt.Printf("تکه %d: %s\n", i+1, chunk)
	}
}
```

### بهترین شیوه‌ها
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go" // کتابخانه رسمی OpenAI Go
	"math"
	"os" // برای دسترسی به متغیرهای محیطی
)

// CreateEmbedding امبدینگ برای یک متن معین تولید می‌کند
func CreateEmbedding(client *openai.Client, text string) ([]float32, error) {
	resp, err := client.CreateEmbedding(
		context.Background(),
		openai.EmbeddingRequest{
			Model: "text-embedding-3-large",
			Input: []string{text}, // API انتظار یک آرایه از رشته‌ها را دارد
		},
	)

	if err != nil {
		return nil, err
	}

	return resp.Data[0].Embedding, nil
}

// CosineSimilarity شباهت کسینوسی بین دو بردار را محاسبه می‌کند
func CosineSimilarity(a, b []float32) float64 {
	var dotProduct float64
	var normA float64
	var normB float64

	for i := range a {
		dotProduct += float64(a[i] * b[i])
		normA += float64(a[i] * a[i])
		normB += float64(b[i] * b[i])
	}

	if normA == 0 || normB == 0 {
		return 0.0 // برای جلوگیری از تقسیم بر صفر
	}
	return dotProduct / (math.Sqrt(normA) * math.Sqrt(normB))
}

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}
	client := openai.NewClient(apiKey)
	client.BaseURL = "https://api.avalai.ir/v1" // نقطه پایانی AvalAI API

	// تکه‌های نمونه
	chunks := []string{
		"AvalAI provides access to a wide range of language models through a unified API.",
		"The platform supports models from various providers including OpenAI, Anthropic, Google, and more.",
		"Each model has different capabilities and pricing, so it's important to understand the tradeoffs.",
	}

	// ایجاد امبدینگ برای هر تکه
	var chunkEmbeddings [][]float32
	for _, chunk := range chunks {
		embedding, err := CreateEmbedding(client, chunk)
		if err != nil {
			fmt.Printf("خطا در ایجاد امبدینگ: %v\n", err)
			return
		}
		chunkEmbeddings = append(chunkEmbeddings, embedding)
	}

	if len(chunkEmbeddings) > 0 && len(chunkEmbeddings[0]) > 0 {
		fmt.Printf("تولید شد %d امبدینگ با ابعاد %d\n", len(chunkEmbeddings), len(chunkEmbeddings[0]))
	} else {
		fmt.Println("هیچ امبدینگی تولید نشد یا امبدینگ‌ها خالی هستند.")
		return
	}

	// ایجاد امبدینگ برای یک پرس و جو
	query := "Which AI models does AvalAI support?"
	queryEmbedding, err := CreateEmbedding(client, query)
	if err != nil {
		fmt.Printf("خطا در ایجاد امبدینگ پرس و جو: %v\n", err)
		return
	}

	// یافتن مشابه‌ترین تکه به پرس و جو
	var similarities []float64
	var maxSimilarity float64 = -1.0 // مقدار اولیه باید کمتر از هر شباهت ممکن باشد
	var mostSimilarIdx int = -1

	for i, embedding := range chunkEmbeddings {
		similarity := CosineSimilarity(queryEmbedding, embedding)
		similarities = append(similarities, similarity)

		if mostSimilarIdx == -1 || similarity > maxSimilarity {
			maxSimilarity = similarity
			mostSimilarIdx = i
		}
	}

	if mostSimilarIdx != -1 {
		fmt.Printf("مشابه‌ترین تکه: %s\n", chunks[mostSimilarIdx])
		fmt.Printf("امتیاز شباهت: %.4f\n", maxSimilarity)
	} else {
		fmt.Println("امکان یافتن مشابه‌ترین تکه وجود نداشت.")
	}
}
```

### بهترین شیوه‌ها
```go
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"time" // برای تاخیر

	"github.com/milvus-io/milvus-sdk-go/v2/client" // کتابخانه رسمی Milvus Go SDK
	"github.com/milvus-io/milvus-sdk-go/v2/entity"
	openai "github.com/openai/openai-go" // کتابخانه رسمی OpenAI Go
)

const (
	// پارامترهای کالکشن
	collectionName = "avalai_docs_rag_go"
	dimension      = 1536 // ابعاد برای text-embedding-3-large
	idField        = "id"
	textField      = "text"
	sourceField    = "source"
	pageField      = "page"
	embeddingField = "embedding"
	milvusHost     = "localhost"
	milvusPort     = "19530"
)

// تابع برای ایجاد امبدینگ‌ها
func createEmbedding(ctx context.Context, avalaiClient *openai.Client, textInput string) ([]float32, error) {
	resp, err := avalaiClient.CreateEmbedding(
		ctx,
		openai.EmbeddingRequest{
			Model: "text-embedding-3-large",
			Input: []string{textInput}, // API انتظار یک آرایه از رشته‌ها را دارد
		},
	)
	if err != nil {
		return nil, fmt.Errorf("خطا در ایجاد امبدینگ: %w", err)
	}
	if len(resp.Data) == 0 {
		return nil, fmt.Errorf("هیچ امبدینگی از API بازگردانده نشد برای متن: %s", textInput)
	}
	return resp.Data[0].Embedding, nil
}

func main() {
	ctx := context.Background()

	// اتصال به AvalAI
	avalaiAPIKey := os.Getenv("AVALAI_API_KEY")
	if avalaiAPIKey == "" {
		log.Fatal("متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
	}
	avalaiClient := openai.NewClient(avalaiAPIKey)
	avalaiClient.BaseURL = "https://api.avalai.ir/v1" // نقطه پایانی AvalAI API

	// اتصال به Milvus
	log.Printf("درحال اتصال به Milvus در %s:%s...\n", milvusHost, milvusPort)
	milvusClient, err := client.NewGrpcClient(ctx, fmt.Sprintf("%s:%s", milvusHost, milvusPort))
	if err != nil {
		log.Fatalf("خطا در اتصال به Milvus: %v", err)
	}
	defer milvusClient.Close()
	log.Println("اتصال به Milvus موفقیت‌آمیز بود.")

	// بررسی وجود کالکشن
	log.Printf("درحال بررسی کالکشن '%s'...\n", collectionName)
	hasCollection, err := milvusClient.HasCollection(ctx, collectionName)
	if err != nil {
		log.Fatalf("خطا در بررسی کالکشن: %v", err)
	}

	if !hasCollection {
		log.Printf("کالکشن '%s' وجود ندارد. در حال ایجاد...\n", collectionName)
		// تعریف اسکیمای کالکشن
		schema := &entity.Schema{
			CollectionName: collectionName,
			Description:    "کالکشن اسناد RAG برای AvalAI (Go)",
			Fields: []*entity.Field{
				{Name: idField, DataType: entity.FieldTypeInt64, IsPrimaryKey: true, AutoID: true},
				{Name: textField, DataType: entity.FieldTypeVarChar, MaxLength: 65535},
				{Name: sourceField, DataType: entity.FieldTypeVarChar, MaxLength: 255},
				{Name: pageField, DataType: entity.FieldTypeInt64},
				{Name: embeddingField, DataType: entity.FieldTypeFloatVector, TypeParams: map[string]string{"dim": fmt.Sprintf("%d", dimension)}},
			},
		}
		err = milvusClient.CreateCollection(ctx, schema, entity.DefaultShardNumber)
		if err != nil {
			log.Fatalf("خطا در ایجاد کالکشن: %v", err)
		}
		log.Printf("کالکشن '%s' با موفقیت ایجاد شد.\n", collectionName)

		// ایجاد شاخص
		log.Printf("درحال ایجاد شاخص برای فیلد '%s'...\n", embeddingField)
		idx, err := entity.NewIndexHNSW(entity.L2, 8, 64) // پارامترهای HNSW: M, efConstruction
		if err != nil {
			log.Fatalf("خطا در ایجاد پارامترهای شاخص: %v", err)
		}
		err = milvusClient.CreateIndex(ctx, collectionName, embeddingField, idx, false, client.WithIndexName("hnsw_idx"))
		if err != nil {
			log.Fatalf("خطا در ایجاد شاخص: %v", err)
		}
		log.Println("شاخص با موفقیت ایجاد شد.")
	} else {
		log.Printf("کالکشن '%s' از قبل وجود دارد.\n", collectionName)
	}

	// اسناد نمونه
	documents := []struct {
		Text   string
		Source string
		Page   int64
	}{
		{
			Text:   "AvalAI provides access to a wide range of language models through a unified API.",
			Source: "docs-go",
			Page:   1,
		},
		{
			Text:   "The platform supports models from various providers including OpenAI, Anthropic, Google, and more.",
			Source: "docs-go",
			Page:   1,
		},
		{
			Text:   "Each model has different capabilities and pricing, so it's important to understand the tradeoffs.",
			Source: "docs-go",
			Page:   2,
		},
	}

	// بارگذاری کالکشن قبل از وارد کردن یا جستجو
	err = milvusClient.LoadCollection(ctx, collectionName, false)
	if err != nil {
		log.Fatalf("خطا در بارگذاری کالکشن: %v", err)
	}
	log.Printf("کالکشن '%s' بارگذاری شد.\n", collectionName)

	// بررسی اینکه آیا اسناد قبلا اضافه شده‌اند (برای جلوگیری از تکرار)
	// این یک بررسی ساده است؛ برای تولید، یک سیستم مدیریت شناسه قوی‌تر لازم است
	var pks []entity.Column
	pks, err = milvusClient.Query(ctx, collectionName, []string{}, fmt.Sprintf("%s != \"\"", textField), []string{idField}, client.WithLimit(int64(len(documents))))
	if err != nil {
		log.Printf("خطا در کوئری برای بررسی اسناد موجود: %v\n", err)
		// ادامه می‌دهیم و سعی می‌کنیم اسناد را اضافه کنیم
	}

	if len(pks) == 0 || (len(pks) > 0 && pks[0].Len() < len(documents)) {
		log.Println("درحال وارد کردن داده‌ها...")
		// آماده‌سازی داده‌ها برای وارد کردن
		textsCol := make([]string, 0, len(documents))
		sourcesCol := make([]string, 0, len(documents))
		pagesCol := make([]int64, 0, len(documents))
		embeddingsCol := make([][]float32, 0, len(documents))

		for _, doc := range documents {
			embedding, err := createEmbedding(ctx, avalaiClient, doc.Text)
			if err != nil {
				log.Printf("خطا در ایجاد امبدینگ برای '%s': %v. از این سند صرف‌نظر می‌شود.\n", doc.Text, err)
				continue
			}
			textsCol = append(textsCol, doc.Text)
			sourcesCol = append(sourcesCol, doc.Source)
			pagesCol = append(pagesCol, doc.Page)
			embeddingsCol = append(embeddingsCol, embedding)
		}

		if len(textsCol) > 0 {
			textColumn := entity.NewColumnVarChar(textField, textsCol)
			sourceColumn := entity.NewColumnVarChar(sourceField, sourcesCol)
			pageColumn := entity.NewColumnInt64(pageField, pagesCol)
			embeddingColumn := entity.NewColumnFloatVector(embeddingField, dimension, embeddingsCol)

			_, err = milvusClient.Insert(ctx, collectionName, "", textColumn, sourceColumn, pageColumn, embeddingColumn)
			if err != nil {
				log.Fatalf("خطا در وارد کردن داده‌ها: %v", err)
			}
			log.Printf("%d سند با موفقیت وارد شد.\n", len(textsCol))

			// Milvus ممکن است برای flush کردن داده‌ها به کمی زمان نیاز داشته باشد
			log.Println("کمی صبر برای flush شدن داده‌ها...")
			time.Sleep(2 * time.Second)

		} else {
			log.Println("هیچ داده جدیدی برای وارد کردن وجود ندارد (احتمالا به دلیل خطای امبدینگ).")
		}
	} else {
		log.Println("به نظر می‌رسد اسناد قبلا وارد شده‌اند. از وارد کردن مجدد صرف‌نظر می‌شود.")
	}

	// دریافت تعداد موجودیت‌ها
	stats, err := milvusClient.GetCollectionStatistics(ctx, collectionName)
	if err != nil {
		log.Fatalf("خطا در دریافت آمار کالکشن: %v", err)
	}
	rowCount := 0
	for _, stat := range stats {
		if stat.Key == "row_count" {
			rowCount = int(stat.Value) // مقدار به صورت رشته‌ای است
			break
		}
	}
	log.Printf("تعداد کل موجودیت‌ها در کالکشن '%s': %d\n", collectionName, rowCount)

	// جستجو
	query := "Which AI models does AvalAI support?"
	queryEmbedding, err := createEmbedding(ctx, avalaiClient, query)
	if err != nil {
		log.Fatalf("خطا در ایجاد امبدینگ پرس و جو: %v", err)
	}

	log.Printf("\nدرحال جستجو برای پرس و جوی: '%s'\n", query)
	// پارامترهای جستجو
	sp, _ := entity.NewIndexHNSWSearchParams(32) // ef برای HNSW

	searchResult, err := milvusClient.Search(
		ctx,
		collectionName,
		[]string{}, // نام پارتیشن‌ها، اگر خالی باشد در کل کالکشن جستجو می‌کند
		"",         // عبارت بولی فیلتر، خالی برای بدون فیلتر
		[]string{textField, sourceField, pageField},         // فیلدهای خروجی
		[]entity.Vector{entity.FloatVector(queryEmbedding)}, // بردارهای پرس و جو
		embeddingField, // نام فیلد برداری برای جستجو
		entity.L2,      // نوع متریک
		2,              // تعداد نتایج برتر (topK)
		sp,             // پارامترهای جستجو
	)
	if err != nil {
		log.Fatalf("خطا در جستجو: %v", err)
	}

	log.Printf("تعداد نتایج یافت شده: %d\n", len(searchResult[0].IDs))
	for _, resultSet := range searchResult {
		for i := 0; i < resultSet.ResultCount; i++ {
			textFieldValue, _ := resultSet.Fields.Get(textField, i)
			sourceFieldValue, _ := resultSet.Fields.Get(sourceField, i)
			pageFieldValue, _ := resultSet.Fields.Get(pageField, i)

			fmt.Printf("متن: %s\n", textFieldValue)
			fmt.Printf("منبع: %s, صفحه: %d\n", sourceFieldValue, pageFieldValue)
			fmt.Printf("امتیاز (فاصله): %.4f\n\n", resultSet.Scores[i])
		}
	}
}
```

### بهترین شیوه‌ها
```go
package main

import (
	"context"
	"fmt"
	"log"
	"math"
	"os"
	"sort"
	"strings"

	"github.com/james-bowman/nlp" // کتابخانه برای TF-IDF
	"github.com/james-bowman/sparse" // برای ماتریس‌های پراکنده
	openai "github.com/openai/openai-go"
)

// HybridRetriever متدهای بازیابی متراکم و پراکنده را ترکیب می‌کند
type HybridRetriever struct {
	texts []string
	denseWeight float64
	sparseWeight float64

	// بازیابی متراکم
	embeddings [][]float32

	// بازیابی پراکنده
	vectorizer *nlp.CountVectorizer // برای تبدیل متن به شمارش کلمات
	transformer *nlp.TfidfTransformer // برای تبدیل شمارش کلمات به امتیازات TF-IDF
	docTermMatrix sparse.Matrix // ماتریس سند-عبارت TF-IDF

	avalaiClient *openai.Client
}

// NewHybridRetriever یک بازیاب ترکیبی جدید ایجاد می‌کند
func NewHybridRetriever(texts []string, avalaiClient *openai.Client, denseWeight float64) *HybridRetriever {
	return &HybridRetriever{
		texts: texts,
		denseWeight: denseWeight,
		sparseWeight: 1.0 - denseWeight,
		avalaiClient: avalaiClient,
	}
}

// Initialize بازیاب را آماده می‌کند
func (r *HybridRetriever) Initialize(ctx context.Context) error {
	log.Println("درحال راه‌اندازی بازیاب پراکنده (TF-IDF)...")
	// راه‌اندازی بازیابی پراکنده
	r.vectorizer = nlp.NewCountVectorizer(nlp.StopWords("en"), nlp.ToLower(true)) // اضافه کردن کلمات توقف و تبدیل به حروف کوچک
	r.transformer = nlp.NewTfidfTransformer()

	// ایجاد ماتریس سند-عبارت
	docTermCounts, err := r.vectorizer.FitTransform(r.texts...)
	if err != nil {
		return fmt.Errorf("خطا در برداری‌سازی متون: %w", err)
	}

	// اعمال تبدیل TF-IDF
	r.docTermMatrix, err = r.transformer.FitTransform(docTermCounts)
	if err != nil {
		return fmt.Errorf("خطا در تبدیل به TF-IDF: %w", err)
	}
	log.Println("بازیاب پراکنده با موفقیت راه‌اندازی شد.")

	// راه‌اندازی بازیابی متراکم با ایجاد امبدینگ‌ها
	log.Println("درحال ایجاد امبدینگ‌ها برای بازیابی متراکم...")
	r.embeddings = make([][]float32, len(r.texts))
	for i, text := range r.texts {
		embedding, errCr := r.createEmbedding(ctx, text)
		if errCr != nil {
			// در صورت خطا، می‌توانیم ادامه دهیم و فقط از بازیابی پراکنده استفاده کنیم یا خطا را برگردانیم
			log.Printf("هشدار: خطا در ایجاد امبدینگ برای متن %d ('%s'): %v. این متن در جستجوی متراکم نادیده گرفته می‌شود.", i, text[:30], errCr)
			// r.embeddings[i] = make([]float32, dimension) // یا یک بردار صفر قرار دهید
		} else {
			r.embeddings[i] = embedding
		}
	}
	log.Printf("%d امبدینگ برای بازیابی متراکم ایجاد شد.\n", len(r.embeddings))
	return nil
}

// createEmbedding امبدینگ برای یک متن معین تولید می‌کند
func (r *HybridRetriever) createEmbedding(ctx context.Context, text string) ([]float32, error) {
	resp, err := r.avalaiClient.CreateEmbedding(
		ctx,
		openai.EmbeddingRequest{
			Model: "text-embedding-3-large",
			Input: []string{text},
		},
	)
	if err != nil {
		return nil, err
	}
	if len(resp.Data) == 0 {
		return nil, fmt.Errorf("هیچ امبدینگی برای متن بازگردانده نشد: %s", text)
	}
	return resp.Data[0].Embedding, nil
}

// cosineSimilarity شباهت کسینوسی بین دو بردار را محاسبه می‌کند
func cosineSimilarity(a, b []float32) float64 {
	if len(a) == 0 || len(b) == 0 || len(a) != len(b) { // بررسی برای بردارهای خالی یا با ابعاد متفاوت
		return 0.0
	}
	var dotProduct, normA, normB float64
	for i := range a {
		dotProduct += float64(a[i] * b[i])
		normA += float64(a[i] * a[i])
		normB += float64(b[i] * b[i])
	}
	if normA == 0 || normB == 0 {
		return 0.0
	}
	return dotProduct / (math.Sqrt(normA) * math.Sqrt(normB))
}

type searchResult struct {
	Index int
	Score float64
}

// denseSearch بازیابی متراکم را با استفاده از شباهت برداری انجام می‌دهد
func (r *HybridRetriever) denseSearch(ctx context.Context, query string, topK int) ([]searchResult, error) {
	queryEmbedding, err := r.createEmbedding(ctx, query)
	if err != nil {
		return nil, fmt.Errorf("خطا در ایجاد امبدینگ پرس و جو: %w", err)
	}

	similarities := make([]searchResult, 0, len(r.embeddings))
	for i, docEmbedding := range r.embeddings {
		if docEmbedding == nil { // اگر امبدینگ برای سندی ایجاد نشده باشد
			continue
		}
		similarities = append(similarities, searchResult{
			Index: i,
			Score: cosineSimilarity(queryEmbedding, docEmbedding),
		})
	}

	sort.Slice(similarities, func(i, j int) bool {
		return similarities[i].Score > similarities[j].Score
	})

	if topK > len(similarities) {
		topK = len(similarities)
	}
	return similarities[:topK], nil
}

// sparseSearch بازیابی پراکنده را با استفاده از TF-IDF انجام می‌دهد
func (r *HybridRetriever) sparseSearch(query string, topK int) ([]searchResult, error) {
	queryVector, err := r.vectorizer.Transform(query)
	if err != nil {
		return nil, fmt.Errorf("خطا در برداری‌سازی پرس و جو: %w", err)
	}
	queryTfidf, err := r.transformer.Transform(queryVector)
	if err != nil {
		return nil, fmt.Errorf("خطا در تبدیل TF-IDF پرس و جو: %w", err)
	}

	similarities := make([]searchResult, r.docTermMatrix.Rows())
	for i := 0; i < r.docTermMatrix.Rows(); i++ {
		docVector := r.docTermMatrix.RowView(i)
		score := nlp.CosineSimilarity(queryTfidf, docVector) // nlp.CosineSimilarity امتیازات بین 0 و 1 را برمی‌گرداند
		if math.IsNaN(score) { // بررسی NaN
			score = 0.0
		}
		similarities[i] = searchResult{Index: i, Score: score}
	}

	sort.Slice(similarities, func(i, j int) bool {
		return similarities[i].Score > similarities[j].Score
	})

	if topK > len(similarities) {
		topK = len(similarities)
	}
	return similarities[:topK], nil
}

// Search جستجوی ترکیبی را با ترکیب بازیابی متراکم و پراکنده انجام می‌دهد
func (r *HybridRetriever) Search(ctx context.Context, query string, topK int) ([]map[string]interface{}, error) {
	denseResults, errDense := r.denseSearch(ctx, query, topK*2) // دریافت نتایج بیشتر
	if errDense != nil {
		log.Printf("هشدار: خطای بازیابی متراکم: %v. ادامه با بازیابی پراکنده...\n", errDense)
		denseResults = []searchResult{} // در صورت خطا، نتایج متراکم را خالی در نظر بگیرید
	}

	sparseResults, errSparse := r.sparseSearch(query, topK*2)
	if errSparse != nil {
		log.Printf("هشدار: خطای بازیابی پراکنده: %v. ادامه با بازیابی متراکم...\n", errSparse)
		sparseResults = []searchResult{} // در صورت خطا، نتایج پراکنده را خالی در نظر بگیرید
	}

	if errDense != nil && errSparse != nil {
		return nil, fmt.Errorf("هر دو بازیابی متراکم و پراکنده با خطا مواجه شدند. متراکم: %v، پراکنده: %v", errDense, errSparse)
	}


	// نرمال‌سازی امتیازات
	maxDenseScore := 0.0
	if len(denseResults) > 0 {
		for _, result := range denseResults {
			if result.Score > maxDenseScore { maxDenseScore = result.Score }
		}
	}
	if maxDenseScore == 0 && len(denseResults) > 0 { maxDenseScore = 1.0 } // اگر همه امتیازات 0 باشند، از تقسیم بر صفر جلوگیری کنید

	maxSparseScore := 0.0
	if len(sparseResults) > 0 {
		for _, result := range sparseResults {
			if result.Score > maxSparseScore { maxSparseScore = result.Score }
		}
	}
	if maxSparseScore == 0 && len(sparseResults) > 0 { maxSparseScore = 1.0 }


	normalizedDense := make(map[int]float64)
	for _, result := range denseResults {
		if maxDenseScore > 0 {
			normalizedDense[result.Index] = result.Score / maxDenseScore
		} else {
			normalizedDense[result.Index] = 0.0
		}
	}

	normalizedSparse := make(map[int]float64)
	for _, result := range sparseResults {
		if maxSparseScore > 0 {
			normalizedSparse[result.Index] = result.Score / maxSparseScore
		} else {
			normalizedSparse[result.Index] = 0.0
		}
	}

	// ترکیب امتیازات
	combinedScores := make(map[int]float64)
	allIndices := make(map[int]bool)
	for _, res := range denseResults { allIndices[res.Index] = true }
	for _, res := range sparseResults { allIndices[res.Index] = true }


	for idx := range allIndices {
		denseS := normalizedDense[idx] // اگر وجود نداشته باشد، 0.0 است
		sparseS := normalizedSparse[idx]
		combinedScores[idx] = (denseS * r.denseWeight) + (sparseS * r.sparseWeight)
	}

	type rankedResult struct {
		Index int
		Score float64
		DenseContribution float64
		SparseContribution float64
		OriginalDenseScore float64
		OriginalSparseScore float64
	}

	var finalRankedResults []rankedResult
	for idx, score := range combinedScores {
		denseCont := (normalizedDense[idx] * r.denseWeight)
		sparseCont := (normalizedSparse[idx] * r.sparseWeight)

		var origDense, origSparse float64
		for _, dr := range denseResults { if dr.Index == idx { origDense = dr.Score; break } }
		for _, sr := range sparseResults { if sr.Index == idx { origSparse = sr.Score; break } }

		finalRankedResults = append(finalRankedResults, rankedResult{
			Index: idx,
			Score: score,
			DenseContribution: denseCont,
			SparseContribution: sparseCont,
			OriginalDenseScore: origDense,
			OriginalSparseScore: origSparse,
		})
	}

	sort.Slice(finalRankedResults, func(i, j int) bool {
		return finalRankedResults[i].Score > finalRankedResults[j].Score
	})

	if topK > len(finalRankedResults) {
		topK = len(finalRankedResults)
	}

	outputResults := make([]map[string]interface{}, topK)
	for i := 0; i < topK; i++ {
		res := finalRankedResults[i]
		outputResults[i] = map[string]interface{}{
			"text": r.texts[res.Index],
			"score": res.Score,
			"dense_contribution": res.DenseContribution,
```

### بهترین شیوه‌ها
```go
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"strings" // برای strings.Builder

	openai "github.com/openai/openai-go"
)

// GenerateRagResponse پاسخی را بر اساس اسناد بازیابی شده تولید می‌کند
func GenerateRagResponse(ctx context.Context, client *openai.Client, query string, retrievedDocuments []map[string]interface{}, model string) (string, error) {
	if len(retrievedDocuments) == 0 {
		log.Println("هیچ سند مرتبطی برای تولید پاسخ یافت نشد. تلاش برای پاسخ بدون زمینه اضافی...")
		plainResponse, err := client.CreateChatCompletion(
			ctx,
			openai.ChatCompletionRequest{
				Model: model,
				Messages: []openai.ChatCompletionMessage{
					{Role: openai.ChatMessageRoleSystem, Content: "You are a helpful assistant."},
					{Role: openai.ChatMessageRoleUser, Content: query},
				},
			},
		)
		if err != nil {
			return "", fmt.Errorf("خطا در ایجاد پاسخ ساده: %w", err)
		}
		return plainResponse.Choices[0].Message.Content, nil
	}

	// فرمت‌بندی زمینه بازیابی شده با استنادات
	var formattedContext strings.Builder

	for i, doc := range retrievedDocuments {
		text, okText := doc["text"].(string)
		if !okText {
			text = "محتوای سند در دسترس نیست"
		}

		metadata, okMeta := doc["metadata"].(map[string]interface{})
		if !okMeta {
			metadata = make(map[string]interface{}) // ایجاد یک مپ خالی اگر وجود ندارد
		}


		source, okSource := metadata["source"].(string)
		if !okSource {
			source = "نامشخص"
		}
		sourceInfo := fmt.Sprintf("[%d] منبع: %s", i+1, source)

		if page, okPage := metadata["page"]; okPage {
			sourceInfo += fmt.Sprintf("، صفحه: %v", page)
		}

		formattedContext.WriteString(fmt.Sprintf("%s\n%s\n\n", text, sourceInfo))
	}

	// ایجاد پرامپت سیستم
	systemPrompt := `شما یک دستیار مفید هستید که به سوالات بر اساس زمینه ارائه شده پاسخ می‌دهید.
	این قوانین را دنبال کنید:
	1. فقط بر اساس زمینه ارائه شده پاسخ دهید.
	2. اگر زمینه حاوی پاسخ نیست، بگویید "اطلاعات کافی برای پاسخ به این سوال ندارم".
	3. هنگام ارجاع به اطلاعات از زمینه، استنادات [1]، [2] و غیره را لحاظ کنید.
	4. مختصر و مفید باشید.
	5. پاسخ خود را به روشی واضح و خوانا فرمت‌بندی کنید.`

	// ایجاد پرامپت کاربر
	userPrompt := fmt.Sprintf(`زمینه:
	%s

	سوال: %s`, formattedContext.String(), query)

	// تولید پاسخ
	resp, err := client.CreateChatCompletion(
		ctx,
		openai.ChatCompletionRequest{
			Model: model,
			Messages: []openai.ChatCompletionMessage{
				{
```


## بینایی (ورودی تصویر)
_source: source-archive/بینایی-ورودی-تصویر-392b6b.md_

### استفاده از API تکمیل گفتگو
```go
// مثال Go با استفاده از تکمیل گفتگو با URL تصویر
package main

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

	imageURL := "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

	resp, err := client.Chat.Completions.New(
		context.Background(),
		openai.ChatCompletionNewParams{
			Model: openai.F("gpt-5.6-luna"),
			Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
				openai.UserMessage(
					openai.F([]openai.ChatCompletionContentPartUnionParam{
						openai.TextPart("در این تصویر چه چیزی وجود دارد؟"),
						openai.ImagePart(imageURL),
					}),
				),
			}),
		},
	)

	if err != nil {
		fmt.Printf("خطا در ایجاد تکمیل: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### استفاده از API پاسخ‌ها
```go
// مثال Go با استفاده از AvalAI با URL تصویر
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
)

func main() {
	// ایجاد کلاینت با استفاده از URL پایه AvalAI
	config := openai.DefaultConfig(os.Getenv("AVALAI_API_KEY"))
	config.BaseURL = "https://api.avalai.ir/v1"
	client := openai.NewClientWithConfig(config)

	// ایجاد درخواست با تصویر
	imageURL := "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

	resp, err := client.CreateResponse(
		context.Background(),
		openai.ResponseRequest{
			model: "gpt-5.6-luna",
			Input: []openai.ResponseMessage{
				{
					Role: "user",
					Content: []openai.ResponseContent{
						{
							Type: "input_text",
							Text: "در این تصویر چه چیزی وجود دارد؟",
						},
						{
							Type: "input_image",
							ImageURL: &openai.ImageURL{
								URL: imageURL,
								// Detail: "high", // اختیاری: تعیین سطح جزئیات
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا در ایجاد پاسخ: %v\n", err)
		return
	}

	// استخراج متن از پاسخ
	var textOutput string
	for _, item := range resp.Output {
		if item.Type == "message" {
			for _, contentPart := range item.Content {
				if contentPart.Type == "output_text" {
					textOutput += contentPart.Text + "\n"
				}
			}
		}
	}

	fmt.Println(textOutput)
}
```


## تنظیمات ایمنی Gemini
_source: source-archive/تنظیمات-ایمنی-Gemini-eea775.md_

### مثال پایه
```go
package main

import (
	"context"
	"fmt"
	"github.com/google/generative-ai-go/genai"
	"google.golang.org/api/option"
)

func main() {
	ctx := context.Background()

	// مقداردهی اولیه کلاینت با AvalAI
	client, err := genai.NewClient(ctx,
		option.WithAPIKey("your-avalai-api-key"),
		option.WithEndpoint("https://api.avalai.ir"))
	if err != nil {
		fmt.Printf("خطا در ایجاد کلاینت: %v\n", err)
		return
	}
	defer client.Close()

	model := client.GenerativeModel("gemini-2.5-flash")

	// پیکربندی تنظیمات ایمنی
	model.SafetySettings = []*genai.SafetySetting{
		{
			Category:  genai.HarmCategoryHarassment,
			Threshold: genai.HarmBlockMediumAndAbove,
		},
		{
			Category:  genai.HarmCategoryHateSpeech,
			Threshold: genai.HarmBlockLowAndAbove,
		},
		{
			Category:  genai.HarmCategorySexuallyExplicit,
			Threshold: genai.HarmBlockMediumAndAbove,
		},
		{
			Category:  genai.HarmCategoryDangerousContent,
			Threshold: genai.HarmBlockOnlyHigh,
		},
	}

	// تولید محتوا
	resp, err := model.GenerateContent(ctx, genai.Text("اهمیت ایمنی آنلاین را توضیح دهید."))
	if err != nil {
		fmt.Printf("خطا در تولید محتوا: %v\n", err)
		return
	}

	// چاپ پاسخ
	for _, part := range resp.Candidates[0].Content.Parts {
		fmt.Println(part)
	}
}
```

### غیرفعال کردن فیلترهای ایمنی
```go
package main

import (
	"context"
	"fmt"
	"github.com/google/generative-ai-go/genai"
	"google.golang.org/api/option"
)

func main() {
	ctx := context.Background()
	client, _ := genai.NewClient(ctx,
		option.WithAPIKey("your-avalai-api-key"),
		option.WithEndpoint("https://api.avalai.ir"))
	defer client.Close()

	model := client.GenerativeModel("gemini-2.5-flash")

	// غیرفعال کردن تمام فیلترهای ایمنی
	model.SafetySettings = []*genai.SafetySetting{
		{Category: genai.HarmCategoryHarassment, Threshold: genai.HarmBlockNone},
		{Category: genai.HarmCategoryHateSpeech, Threshold: genai.HarmBlockNone},
		{Category: genai.HarmCategorySexuallyExplicit, Threshold: genai.HarmBlockNone},
		{Category: genai.HarmCategoryDangerousContent, Threshold: genai.HarmBlockNone},
	}

	resp, _ := model.GenerateContent(ctx, genai.Text("پرامپت شما اینجا"))
	fmt.Println(resp.Candidates[0].Content.Parts[0])
}
```

### مثال پایه با OpenAI SDK
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// توجه: برای Go، ممکن است نیاز به استفاده از درخواست‌های HTTP خام
	// برای ارسال safety_settings به عنوان پارامترهای extra_body داشته باشید
	// SDK Go OpenAI ممکن است مستقیما extra_body را پشتیبانی نکند

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gemini-2.5-flash",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: "اهمیت ایمنی آنلاین را توضیح دهید.",
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### مدیریت بازخورد ایمنی در پاسخ‌ها
```go
package main

import (
	"context"
	"fmt"
	"github.com/google/generative-ai-go/genai"
	"google.golang.org/api/option"
)

func main() {
	ctx := context.Background()
	client, _ := genai.NewClient(ctx,
		option.WithAPIKey("your-avalai-api-key"),
		option.WithEndpoint("https://api.avalai.ir"))
	defer client.Close()

	model := client.GenerativeModel("gemini-2.5-flash")
	resp, err := model.GenerateContent(ctx, genai.Text("پرامپت شما اینجا"))

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	// بررسی بازخورد پرامپت
	if resp.PromptFeedback != nil {
		fmt.Printf("دلیل مسدودسازی: %v\n", resp.PromptFeedback.BlockReason)
	}

	// بررسی رتبه‌بندی‌های ایمنی کاندید
	for _, candidate := range resp.Candidates {
		for _, rating := range candidate.SafetyRatings {
			fmt.Printf("دسته: %v، احتمال: %v، مسدود شده: %v\n",
				rating.Category, rating.Probability, rating.Blocked)
		}
	}
}
```


## تولید متن و پرامپت‌نویسی
_source: source-archive/تولید-متن-و-پرامپت-نویسی-88e099.md_

### تولید متن پایه
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	payload := map[string]any{
		"model":        "gpt-5.6-luna",
		"instructions": "You are a helpful assistant.",
		"input":        "یک داستان یک جمله‌ای قبل از خواب درباره یک تک‌شاخ بنویس.",
	}

	body, err := json.Marshal(payload)
	if err != nil {
		panic(err)
	}

	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/responses", bytes.NewBuffer(body))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	responseBody, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(responseBody))
}
```

### نقش‌های پیام و دستورالعمل‌ها
```go
// مثال استفاده از پارامتر instructions با AvalAI
config := openai.DefaultConfig(os.Getenv("AVALAI_API_KEY"))
config.BaseURL = "https://api.avalai.ir/v1"
client := openai.NewClientWithConfig(config)

resp, err := client.CreateResponse(
	context.Background(),
	openai.ResponseRequest{
		Model:        "gpt-5.6-luna",
		Instructions: "مثل دزدان دریایی صحبت کن.",
		Input:        "آیا نقطه‌ویرگول در جاوااسکریپت اختیاری است؟",
	},
)

// استخراج متن از پاسخ همانطور که قبلا نشان داده شد
```

### نقش‌های پیام و دستورالعمل‌ها
```go
// مثال استفاده از نقش‌های developer و user با AvalAI
config := openai.DefaultConfig(os.Getenv("AVALAI_API_KEY"))
config.BaseURL = "https://api.avalai.ir/v1"
client := openai.NewClientWithConfig(config)

resp, err := client.CreateResponse(
	context.Background(),
	openai.ResponseRequest{
		model: "gpt-5.6-luna",
		Input: []openai.ResponseMessage{
			{
				Role:    "developer",
				Content: "مثل دزدان دریایی صحبت کن.",
			},
			{
				Role:    "user",
				Content: "آیا نقطه‌ویرگول در جاوااسکریپت اختیاری است؟",
			},
		},
	},
)

// استخراج متن از پاسخ همانطور که قبلا نشان داده شد
```


## تولید پیشرفته تصویر با Gemini (مدل‌های Nano Banana)
_source: source-archive/تولید-پیشرفته-تصویر-با-Gemini-مدل-های-Nano-Banana-ebfd74.md_

### تولید پایه تصویر از متن
```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
	"log"
	"os"
)

func main() {
	ctx := context.Background()

	// کلاینت به صورت خودکار از AvalAI استفاده می‌کند وقتی پیکربندی شده باشد
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  os.Getenv("AVALAI_API_KEY"),
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	result, _ := client.Models.GenerateContent(
		ctx,
		"gemini-2.5-flash-image",
		genai.Text("Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"),
	)

	for _, part := range result.Candidates[0].Content.Parts {
		if part.Text != "" {
			fmt.Println(part.Text)
		} else if part.InlineData != nil {
			imageBytes := part.InlineData.Data
			_ = os.WriteFile("nano_banana_dish.png", imageBytes, 0644)
			fmt.Println("✅ تصویر ذخیره شد به عنوان nano_banana_dish.png")
		}
	}
}
```


## راهنمای شروع سریع
_source: source-archive/راهنمای-شروع-سریع-bbc716.md_

### Responses API (پیشنهادی برای برنامه‌های جدید)
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	payload := map[string]any{
		"model":        "gpt-5.6-luna",
		"instructions": "You are a helpful assistant.",
		"input":        "سلام، دنیا!",
	}

	body, _ := json.Marshal(payload)
	req, _ := http.NewRequest("POST", "https://api.avalai.ir/v1/responses", bytes.NewBuffer(body))
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	responseBody, _ := io.ReadAll(resp.Body)
	fmt.Println(string(responseBody))
}
```


## راهنمای نظارت (Moderation)
_source: source-archive/راهنمای-نظارت-Moderation-0c65ae.md_

### نظارت ورودی‌های متنی
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("AVALAI_API_KEY")
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.Moderations(
		context.Background(),
		openai.ModerationRequest{
			Input: "متن نمونه‌ای که ممکن است خط‌مشی محتوا را نقض کند.",
			Model: openai.ModerationLatest,
		},
	)

	if err != nil {
		fmt.Printf("خطای نظارت: %v\n", err)
		return
	}

	// بررسی اینکه آیا متن پرچم‌گذاری شده است
	if resp.Results[0].Flagged {
		fmt.Println("این محتوا پرچم‌گذاری شده است!")
	}

	// بررسی دسته‌بندی‌های خاص
	for category, score := range resp.Results[0].CategoryScores {
		if score > 0.5 {
			fmt.Printf("محتوا برای %s با امتیاز %.2f پرچم‌گذاری شده است\n", category, score)
		}
	}
}
```

### نظارت ورودی‌های تصویر و متن (چندوجهی)
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("AVALAI_API_KEY")
	client.BaseURL = "https://api.avalai.ir/v1"

	// ایجاد ساختار ورودی برای نظارت چندوجهی
	input := []openai.ModerationInput{
		{
			Type: "text",
			Text: "توضیحات همراه تصویر.",
		},
		{
			Type: "image_url",
			ImageURL: &openai.ImageURL{
				URL: "https://example.com/image_to_moderate.png",
			},
		},
	}

	resp, err := client.Moderations(
		context.Background(),
		openai.ModerationRequest{
			Input: input,
			Model: "omni-moderation-latest",
		},
	)

	if err != nil {
		fmt.Printf("خطای نظارت: %v\n", err)
		return
	}

	// پردازش پاسخ
	if resp.Results[0].Flagged {
		fmt.Println("این محتوا پرچم‌گذاری شده است!")
	}

	// بررسی دسته‌بندی‌های خاص
	for category, score := range resp.Results[0].CategoryScores {
		if score > 0.5 {
			fmt.Printf("محتوا برای %s با امتیاز %.2f پرچم‌گذاری شده است\n", category, score)
		}
	}
}
```


## راهنمای ورودی‌های فایل
_source: source-archive/راهنمای-ورودی-های-فایل-f8fbdf.md_

### تصویر URL در Chat Completions
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
	"os"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "در این تصویر چیست؟",
						},
						{
							Type: "image_url",
							ImageURL: &openai.ImageURL{
								URL: "https://example.com/sample-image.jpg",
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### URL PDF در Chat Completions
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
	"os"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	fileURL := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-4-6",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "این سند درباره چیست؟",
						},
						{
							Type: "file",
							File: &openai.ChatMessageFile{
								FileID: fileURL,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### URL سند در OCR API
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	requestBody := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]string{
			"type":         "document_url",
			"document_url": "https://arxiv.org/pdf/1805.04770",
		},
		"include_image_base64": true,
	}

	jsonBody, _ := json.Marshal(requestBody)

	req, _ := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(jsonBody))
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(body))
}
```

### تصویر با Base64 در Chat Completions
```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// خواندن و کدگذاری تصویر
	imageData, err := ioutil.ReadFile("image.jpg")
	if err != nil {
		fmt.Printf("خطا در خواندن فایل: %v\n", err)
		return
	}
	base64Image := base64.StdEncoding.EncodeToString(imageData)
	dataURL := "data:image/jpeg;base64," + base64Image

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "در این تصویر چیست؟",
						},
						{
							Type: "image_url",
							ImageURL: &openai.ImageURL{
								URL: dataURL,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### PDF با Base64 در Chat Completions
```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// خواندن و کدگذاری PDF
	pdfData, err := ioutil.ReadFile("document.pdf")
	if err != nil {
		fmt.Printf("خطا در خواندن فایل: %v\n", err)
		return
	}
	base64Pdf := base64.StdEncoding.EncodeToString(pdfData)
	dataURL := "data:application/pdf;base64," + base64Pdf

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gemini-2.5-flash",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "این سند را خلاصه کنید",
						},
						{
							Type: "file",
							File: &openai.ChatMessageFile{
								FileData: dataURL,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### صوت با Base64 در Chat Completions
```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// خواندن و کدگذاری صوت
	audioData, err := ioutil.ReadFile("audio.mp3")
	if err != nil {
		fmt.Printf("خطا در خواندن فایل: %v\n", err)
		return
	}
	base64Audio := base64.StdEncoding.EncodeToString(audioData)
	dataURL := "data:audio/mp3;base64," + base64Audio

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gemini-2.5-flash",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "این صوت را رونویسی کنید",
						},
						{
							Type: "file",
							File: &openai.ChatMessageFile{
								FileData: dataURL,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### اکسل با Base64 در Chat Completions
```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// خواندن و کدگذاری فایل اکسل
	excelData, err := ioutil.ReadFile("spreadsheet.xlsx")
	if err != nil {
		fmt.Printf("خطا در خواندن فایل: %v\n", err)
		return
	}
	base64Excel := base64.StdEncoding.EncodeToString(excelData)
	mimeType := "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
	dataURL := fmt.Sprintf("data:%s;base64,%s", mimeType, base64Excel)

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "این صفحه گسترده را تحلیل کنید و نکات کلیدی را ارائه دهید",
						},
						{
							Type: "file",
							File: &openai.ChatMessageFile{
								FileData: dataURL,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### آپلود فایل
```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// آپلود فایل
	fileReq := openai.FileRequest{
		FilePath: "document.pdf",
		Purpose:  "user_data",
	}
	file, err := client.CreateFile(context.Background(), fileReq)
	if err != nil {
		fmt.Printf("خطا در آپلود فایل: %v\n", err)
		return
	}
	fmt.Printf("فایل با شناسه آپلود شد: %s\n", file.ID)
}
```

### استفاده از شناسه فایل در Chat Completions
```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// با فرض اینکه فایل قبلا آپلود شده است
	fileID := "file-abc123xyz"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "این سند را خلاصه کنید",
						},
						{
							Type: "file",
							File: &openai.ChatMessageFile{
								FileID: fileID,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### استفاده از شناسه فایل در Responses API
```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	fileID := "file-abc123xyz"

	resp, err := client.CreateResponse(
		context.Background(),
		openai.ResponseRequest{
			model: "gpt-5.6-luna",
			Input: []openai.ResponseInput{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ResponseContent{
						{
							Type:   "input_file",
							FileID: fileID,
						},
						{
							Type: "input_text",
							Text: "اولین موضوع در این سند چیست؟",
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.OutputText)
}
```


## سطوح سرویس
_source: source-archive/سطوح-سرویس-332848.md_

### استفاده از سطح Default
```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/sashabaranov/go-openai"
)

func main() {
	config := openai.DefaultConfig(os.Getenv("AVALAI_API_KEY"))
	config.BaseURL = "https://api.avalai.ir/v1"
	client := openai.NewClientWithConfig(config)

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gpt-5.4",
			Messages: []openai.ChatCompletionMessage{
				{Role: "user", Content: "سلام!"},
			},
			// service_tier به طور پیش‌فرض "default" است
		},
	)
	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}
	fmt.Println(resp.Choices[0].Message.Content)
}
```

### استفاده از سطح Flex
```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/sashabaranov/go-openai"
)

func main() {
	config := openai.DefaultConfig(os.Getenv("AVALAI_API_KEY"))
	config.BaseURL = "https://api.avalai.ir/v1"
	client := openai.NewClientWithConfig(config)

	// استفاده از سطح flex برای صرفه‌جویی در هزینه کارهای غیرحساس به زمان
	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gpt-5-mini",
			Messages: []openai.ChatCompletionMessage{
				{Role: "user", Content: "این سند را خلاصه کن..."},
			},
			// تنظیم service_tier به "flex" برای قیمت‌گذاری کاهش یافته
		},
	)
	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}
	fmt.Println(resp.Choices[0].Message.Content)
}
```


## فراخوانی تابع
_source: source-archive/فراخوانی-تابع-1e4858.md_

### مثال: دریافت وضعیت آب و هوا
```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	baseURL := "https://api.avalai.ir/v1" // از URL پایه AvalAI استفاده کنید

	config := openai.DefaultConfig(apiKey)
	config.BaseURL = baseURL
	client := openai.NewClientWithConfig(config)

	tools := []openai.Tool{
		{
			Type: openai.ToolTypeFunction,
			Function: &openai.FunctionDefinition{
				Name:        "get_current_weather",
				Description: "دریافت وضعیت آب و هوای فعلی در یک مکان مشخص",
				Parameters: map[string]interface{}{
					"type": "object",
					"properties": map[string]interface{}{
						"location": map[string]interface{}{
							"type":        "string",
							"description": "شهر و استان، به عنوان مثال San Francisco, CA",
						},
						"unit": map[string]interface{}{
							"type": []string{"string", "null"},
							"enum": []interface{}{"celsius", "fahrenheit", nil},
						},
					},
					"required":             []string{"location", "unit"},
					"additionalProperties": false,
				},
			},
		},
	}

	messages := []openai.ChatCompletionMessage{
		{Role: openai.ChatMessageRoleUser, Content: "هوای بوستون چطور است؟"}, // پیام کاربر به فارسی
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model:      "gpt-5.6-luna", // از مدلی استفاده کنید که از فراخوانی تابع از طریق AvalAI پشتیبانی می‌کند
			Messages:   messages,
			Tools:      tools,
			ToolChoice: "auto", // پیش‌فرض: اجازه دهید مدل تصمیم بگیرد
		},
	)

	if err != nil {
		fmt.Printf("خطای تکمیل چت: %v\n", err)
		return
	}

	responseMessage := resp.Choices[0].Message
	toolCalls := responseMessage.ToolCalls

	// منطق مرحله ۳ در ادامه می‌آید...
	if len(toolCalls) > 0 {
		fmt.Println("مدل می‌خواهد توابع زیر را فراخوانی کند:")
		// برای مرحله ۳ و ۴ در toolCalls حلقه بزنید
		for _, toolCall := range toolCalls {
			fmt.Printf(" شناسه: %s, نوع: %s, تابع: %s, آرگومان‌ها: %s\n",
				toolCall.ID, toolCall.Type, toolCall.Function.Name, toolCall.Function.Arguments)
		}
		// responseMessage و toolCalls را برای مرحله ۳ و ۴ ذخیره کنید
	} else {
		fmt.Println("مدل درخواست فراخوانی تابع نداد.")
		fmt.Println(responseMessage.Content)
	}
}
```

### مثال: دریافت وضعیت آب و هوا
```go
// فرض کنید 'messages' حاوی تاریخچه تا پیام tool_calls دستیار است
// فرض کنید 'resultsForNextCall' حاوی اسلایس پیام‌های نتیجه ابزار از مرحله ۳ است

func sendResultsAndGetResponse(client *openai.Client, messages []openai.ChatCompletionMessage, resultsForNextCall []openai.ChatCompletionMessage) {
	if len(resultsForNextCall) > 0 {
		// نتایج ابزار را به تاریخچه پیام اضافه کنید
		messages = append(messages, resultsForNextCall...)

		fmt.Println("\nدر حال ارسال نتایج به مدل...")
		resp, err := client.CreateChatCompletion(
			context.Background(),
			openai.ChatCompletionRequest{
				Model:    "gpt-5.6-luna",
				Messages: messages,
				// در اینجا نیازی به ابزار نیست مگر اینکه بخواهید فراخوانی‌های بعدی انجام شود
			},
		)

		if err != nil {
			fmt.Printf("خطای تکمیل چت در فراخوانی دوم: %v\n", err)
			return
		}

		// مرحله ۵: دریافت پاسخ نهایی
		finalResponse := resp.Choices[0].Message.Content
		fmt.Println("\nپاسخ نهایی مدل:")
		fmt.Println(finalResponse)
	}
}

// مثال استفاده (با فرض اینکه client, messages و resultsForNextCall پر شده‌اند)
// اطمینان حاصل کنید که 'messages' شامل پیام کاربر و پیام دستیار با tool_calls است
// sendResultsAndGetResponse(client, messages, resultsForNextCall)
```


## محدودیت نرخ API AvalAI و سطوح حساب
_source: source-archive/محدودیت-نرخ-API-AvalAI-و-سطوح-حساب-32e26c.md_

### مثال پایتون
```go
package main

import (
	"context"
	"fmt"
	"math"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/openai/openai-go"
)

// تابع ارسال درخواست با عقب‌نشینی نمایی برای خطاهای محدودیت نرخ
func makeRequestWithBackoff(ctx context.Context, fn func() (interface{}, error), maxRetries int, initialDelay, maxDelay time.Duration) (interface{}, error) {
	var numRetries int
	delay := initialDelay

	for {
		// ارسال درخواست API
		result, err := fn()
		if err == nil {
			return result, nil
		}

		// بررسی خطای محدودیت نرخ
		var retryAfter time.Duration
		var isRateLimitError bool

		if apiErr, ok := err.(*openai.APIError); ok {
			isRateLimitError = apiErr.HTTPStatusCode == http.StatusTooManyRequests

			// استخراج هدر retry-after
			if isRateLimitError && apiErr.Header != nil {
				if retryAfterStr := apiErr.Header.Get("retry-after"); retryAfterStr != "" {
					if retryAfterSec, err := strconv.Atoi(retryAfterStr); err == nil {
						retryAfter = time.Duration(retryAfterSec) * time.Second
					}
				}
			}
		}

		// اگر خطای محدودیت نرخ نیست یا به حداکثر تلاش‌ها رسیده‌ایم
		if !isRateLimitError || numRetries >= maxRetries {
			return nil, err
		}

		// استفاده از بیشترین مقدار بین تاخیر فعلی و retry-after
		if retryAfter > delay {
			delay = retryAfter
		}

		// عقب‌نشینی نمایی با لرزش (jitter)
		jitter := time.Duration(rand.Float64() * 0.5 * float64(delay))
		sleepTime := delay + jitter

		fmt.Fprintf(os.Stderr, "محدودیت نرخ فراتر رفت. تلاش مجدد در %v...\n", sleepTime)

		// انتظار قبل از تلاش مجدد
		select {
		case <-time.After(sleepTime):
		case <-ctx.Done():
			return nil, ctx.Err()
		}

		// افزایش شمارنده و تاخیر
		numRetries++
		delay = time.Duration(math.Min(float64(delay*2), float64(maxDelay)))
	}
}

func main() {
	// تنظیم کلاینت
	config := openai.DefaultConfig(os.Getenv("AVALAI_API_KEY"))
	config.BaseURL = "https://api.avalai.ir/v1"
	client := openai.NewClientWithConfig(config)

	// تعریف تابع ارسال درخواست
	getCompletion := func() (interface{}, error) {
		return client.CreateChatCompletion(
			context.Background(),
			openai.ChatCompletionRequest{
				model: "gpt-5.6-luna",
				Messages: []openai.ChatCompletionMessage{
					{
						Role:    "user",
						Content: "سلام!",
					},
				},
			},
		)
	}

	// ارسال درخواست با منطق تلاش مجدد
	ctx := context.Background()
	result, err := makeRequestWithBackoff(ctx, getCompletion, 5, 1*time.Second, 60*time.Second)

	if err != nil {
		fmt.Fprintf(os.Stderr, "خطا پس از چندین تلاش: %v\n", err)
		os.Exit(1)
	}

	// نمایش پاسخ
	if resp, ok := result.(openai.ChatCompletionResponse); ok {
		fmt.Println(resp.Choices[0].Message.Content)
	} else {
		fmt.Fprintf(os.Stderr, "نوع پاسخ نامعتبر\n")
	}
}
```


## مدل‌های استدلالی
_source: source-archive/مدل-های-استدلالی-21a4c4.md_

### جریان‌های طولانی ابزارمحور و `phase`
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	prompt := `
یک اسکریپت bash بنویسید که یک ماتریس را به صورت رشته با فرمت
'[1,2],[3,4],[5,6]' دریافت کرده و ترانهاده آن را با همان فرمت چاپ کند.
`

	payload := map[string]any{
		"model":     "gpt-5.6-luna",
		"reasoning": map[string]string{"effort": "medium"},
		"input": []map[string]string{
			{
				"role":    "user",
				"content": prompt,
			},
		},
	}

	body, err := json.Marshal(payload)
	if err != nil {
		panic(err)
	}

	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/responses", bytes.NewBuffer(body))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)

	if err != nil {
		fmt.Printf("خطای Responses API: %v\n", err)
		return
	}
	defer resp.Body.Close()

	responseBody, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(responseBody))
}
```

### تخصیص فضا برای استدلال
```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	// ... (راه‌اندازی کلاینت مانند قبل) ...

	prompt := "..."  // پرامپت شما در اینجا
	maxTokens := 300 // تعریف max_tokens

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{Role: openai.ChatMessageRoleUser, Content: prompt},
			},
			MaxTokens: maxTokens, // محدود کردن کل توکن‌های تولید شده
			// در صورت لزوم، پارامترهای استدلال را اضافه کنید
		},
	)

	if err != nil {
		fmt.Printf("خطای ChatCompletion: %v\n", err)
		return
	}

	finishReason := resp.Choices[0].FinishReason
	outputText := resp.Choices[0].Message.Content

	if finishReason == openai.FinishReasonLength { // بررسی دلیل پایان length
		fmt.Println("توکن‌ها تمام شد (به max_tokens رسید).")
		if outputText != "" {
			fmt.Println("خروجی جزئی:", outputText)
		} else {
			fmt.Println("توکن‌ها در مرحله استدلال تمام شد.")
		}
	} else if finishReason == openai.FinishReasonStop {
		fmt.Println("با موفقیت تکمیل شد:")
		fmt.Println(outputText)
	} else {
		fmt.Printf("با دلیل پایان یافت: %s\n", finishReason)
		if outputText != "" {
			fmt.Println("خروجی:", outputText)
		}
	}
}
```

### مثال‌های پرامپت
```go
// --- کد فراخوانی (Go) ---
package main

import (
	"context"
	"fmt"
	"os"
	"strings"

	openai "github.com/openai/openai-go"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	baseURL := "https://api.avalai.ir/v1"

	config := openai.DefaultConfig(apiKey)
	config.BaseURL = baseURL
	client := openai.NewClientWithConfig(config)

	// توجه به تغییر: به جای بک‌تیک سه‌گانه در رشته پرامپت،
	// از تورفتگی برای مثال کد داخلی استفاده کنید.
	prompt := strings.TrimSpace(`
دستورالعمل‌ها:
- با توجه به کامپوننت React زیر، آن را طوری تغییر دهید که کتاب‌های غیرداستانی متن قرمز داشته باشند.
- فقط کد بازسازی شده React را در پاسخ خود برگردانید.
- توضیحات یا بلوک‌های کد مارک‌داون را شامل نکنید.
- از چهار فاصله برای تورفتگی استفاده کنید.
- طول خطوط را زیر ۸۰ ستون نگه دارید.

کد اصلی:

 const books = [
 { title: "تل‌ماسه", category: "fiction", id: 1 }, // داستانی
 { title: "فرانکنشتاین", category: "fiction", id: 2 }, // داستانی
 { title: "مانی‌بال", category: "nonfiction", id: 3 }, // غیرداستانی
 ];

 export default function BookList() {
 const listItems = books.map(book =>
 <li>
 {book.title}
 </li>
 );

 return (
 <ul>{listItems}</ul>
 );
 }

`) // توجه: رشته‌های فارسی در کد Go باید به درستی مدیریت شوند

	temp := float32(0.1)
	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna", // از یک مدل استدلالی مناسب از AvalAI استفاده کنید
			Messages: []openai.ChatCompletionMessage{
				{Role: openai.ChatMessageRoleUser, Content: prompt},
			},
			Temperature: &temp,
		},
	)

	if err != nil {
		fmt.Printf("خطای API: %v\n", err)
		return
	}
	fmt.Println(resp.Choices[0].Message.Content)
}
```

### مثال‌های پرامپت
```go
// --- کد فراخوانی (Go) ---
package main

import (
	"context"
	"fmt"
	"os"
	"strings"

	openai "github.com/openai/openai-go"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	baseURL := "https://api.avalai.ir/v1"

	config := openai.DefaultConfig(apiKey)
	config.BaseURL = baseURL
	client := openai.NewClientWithConfig(config)

	prompt := strings.TrimSpace(`
می‌خواهم یک برنامه پایتون بسازم که سوالات کاربر را دریافت کرده و آنها را
در یک ذخیره‌ساز ساده کلید-مقدار (مانند دیکشنری یا فایل JSON) که در آن
به پاسخ‌ها نگاشت شده‌اند، جستجو کند. اگر یک تطابق نزدیک (بررسی بدون حساسیت به حروف بزرگ و کوچک) وجود داشته باشد،
پاسخ مطابق را بازیابی می‌کند. اگر وجود نداشته باشد، از کاربر می‌خواهد
پاسخی ارائه دهد و جفت سوال/پاسخ جدید را ذخیره می‌کند.

1. طرحی برای ساختار دایرکتوری (مثلا اسکریپت اصلی، فایل داده) ارائه دهید.
2. کد کامل پایتون برای اسکریپت اصلی را برگردانید.
3. یک ساختار JSON نمونه برای فایل داده برگردانید.
4. متن توضیحی را فقط در ابتدا و انتهای خروجی ارائه دهید، نه به صورت ترکیبی در کد یا خروجی ساختار فایل.
`) // اطمینان از مدیریت صحیح UTF-8 در Go

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "deepseek-v4.1-flash", // از شناسه صریح V4.1 Flash استفاده کنید
			Messages: []openai.ChatCompletionMessage{
				{Role: openai.ChatMessageRoleUser, Content: prompt},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطای API: %v\n", err)
		return
	}
	fmt.Println(resp.Choices[0].Message.Content)
}
```

### مثال‌های پرامپت
```go
// --- کد فراخوانی (Go) ---
package main

import (
	"context"
	"fmt"
	"os"
	"strings"

	openai "github.com/openai/openai-go"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	baseURL := "https://api.avalai.ir/v1"

	config := openai.DefaultConfig(apiKey)
	config.BaseURL = baseURL
	client := openai.NewClientWithConfig(config)

	prompt := strings.TrimSpace(`
سه ترکیب یا کلاس ترکیبی که باید برای پیشبرد تحقیقات در مورد
آنتی‌بیوتیک‌های جدید، به ویژه علیه باکتری‌های مقاوم، بیشتر بررسی کنیم، کدامند؟
به طور خلاصه توضیح دهید که چرا هر کدام امیدوارکننده است.
`) // اطمینان از مدیریت صحیح UTF-8

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gemini-3.1-pro-preview", // از یک مدل استدلالی مناسب از AvalAI استفاده کنید
			Messages: []openai.ChatCompletionMessage{
				{Role: openai.ChatMessageRoleUser, Content: prompt},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطای API: %v\n", err)
		return
	}
	fmt.Println(resp.Choices[0].Message.Content)
}
```


## مدل‌های گوگل
_source: source-archive/مدل-های-گوگل-a8d7eb.md_

### تولید متن پایه
```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  "your-avalai-api-key",
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	result, _ := client.Models.GenerateContent(
		ctx,
		"gemini-2.5-flash",
		genai.Text("هوش مصنوعی چگونه کار می‌کند؟"),
		nil,
	)

	fmt.Println(result.Text())
}
```

### دستورالعمل‌های سیستمی
```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  "your-avalai-api-key",
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	config := &genai.GenerateContentConfig{
		SystemInstruction: genai.NewContentFromText("شما یک گربه هستید. نام شما نکو است.", genai.RoleUser),
	}

	result, _ := client.Models.GenerateContent(
		ctx,
		"gemini-2.5-flash",
		genai.Text("سلام"),
		config,
	)

	fmt.Println(result.Text())
}
```

### پیکربندی تفکر (مدل‌های Gemini 2.5)
```go
package main

import (
    "context"
    "fmt"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "your-avalai-api-key",
        BaseURL: "https://api.avalai.ir",
    })
    if err != nil {
        log.Fatal(err)
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash",
        genai.Text("هوش مصنوعی چگونه کار می‌کند؟"),
        &genai.GenerateContentConfig{
            ThinkingConfig: &genai.ThinkingConfig{
                ThinkingBudget: int32(0), // تفکر را غیرفعال می‌کند
            },
        }
    )

    fmt.Println(result.Text())
}
```

### پاسخ‌های جریانی
```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  "your-avalai-api-key",
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	stream := client.Models.GenerateContentStream(
		ctx,
		"gemini-2.5-flash",
		genai.Text("داستانی درباره کوله‌پشتی جادویی بنویسید."),
		nil,
	)

	for chunk, _ := range stream {
		part := chunk.Candidates[0].Content.Parts[0]
		fmt.Print(part.Text)
	}
}
```

### مکالمات چندمرحله‌ای (چت)
```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  "your-avalai-api-key",
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	history := []*genai.Content{
		genai.NewContentFromText("سلام، خوشحالم که شما را ملاقات کردم! من ۲ سگ در خانه‌ام دارم.", genai.RoleUser),
		genai.NewContentFromText("خوشحالم که شما را ملاقات کردم. چه چیزی می‌خواهید بدانید؟", genai.RoleModel),
	}

	chat, _ := client.Chats.Create(ctx, "gemini-2.5-flash", nil, history)
	res, _ := chat.SendMessage(ctx, genai.Part{Text: "چند پنجه در خانه‌ام هست؟"})

	if len(res.Candidates) > 0 {
		fmt.Println(res.Candidates[0].Content.Parts[0].Text)
	}
}
```

### استفاده از تنظیمات ایمنی با API بومی
```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  "your-avalai-api-key",
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	result, _ := client.Models.GenerateContent(
		ctx,
		"gemini-2.5-flash",
		genai.Text("پرامپت شما اینجا"),
		&genai.GenerateContentConfig{
			SafetySettings: []*genai.SafetySetting{
				{
					Category:  genai.HarmCategoryHarassment,
					Threshold: genai.HarmBlockThresholdBlockMediumAndAbove,
				},
				{
					Category:  genai.HarmCategoryHateSpeech,
					Threshold: genai.HarmBlockThresholdBlockLowAndAbove,
				},
				{
					Category:  genai.HarmCategorySexuallyExplicit,
					Threshold: genai.HarmBlockThresholdBlockOnlyHigh,
				},
				{
					Category:  genai.HarmCategoryDangerousContent,
					Threshold: genai.HarmBlockThresholdBlockMediumAndAbove,
				},
			},
		},
	)

	fmt.Println(result.Text())
}
```


## مدیریت خطا در API AvalAI
_source: source-archive/مدیریت-خطا-در-API-AvalAI-711dc1.md_

### مثال ها
```go
package main

import (
	"context"
	"fmt"
	"io"
	"math"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/openai/openai-go"
)

// تابع ارسال درخواست API با منطق تلاش مجدد
func makeApiRequestWithRetry(ctx context.Context, fn func() (interface{}, error), maxRetries int, initialDelay, maxDelay time.Duration) (interface{}, error) {
	var numRetries int
	delay := initialDelay

	for {
		// ارسال درخواست API
		result, err := fn()
		if err == nil {
			return result, nil
		}

		// بررسی نوع خطا
		var retryAfter time.Duration
		var shouldRetry bool

		// بررسی خطای محدودیت نرخ
		if apiErr, ok := err.(*openai.APIError); ok {
			if apiErr.HTTPStatusCode == http.StatusTooManyRequests {
				shouldRetry = true
				// استخراج هدر retry-after
				if apiErr.Header != nil {
					if retryAfterStr := apiErr.Header.Get("retry-after"); retryAfterStr != "" {
						if retryAfterSec, err := strconv.Atoi(retryAfterStr); err == nil {
							retryAfter = time.Duration(retryAfterSec) * time.Second
						}
					}
				}
			} else if apiErr.HTTPStatusCode >= 500 {
				// تلاش مجدد برای خطاهای سرور
				shouldRetry = true
			}
		}

		// اگر نباید تلاش مجدد کنیم یا به حداکثر تلاش‌ها رسیده‌ایم
		if !shouldRetry || numRetries >= maxRetries {
			return nil, err
		}

		// استفاده از بیشترین مقدار بین تاخیر فعلی و retry-after
		if retryAfter > delay {
			delay = retryAfter
		}

		// عقب‌نشینی نمایی با لرزش (jitter)
		jitter := time.Duration(rand.Float64() * 0.5 * float64(delay))
		sleepTime := delay + jitter

		fmt.Fprintf(os.Stderr, "تلاش مجدد در %v...\n", sleepTime)

		// انتظار قبل از تلاش مجدد
		select {
		case <-time.After(sleepTime):
		case <-ctx.Done():
			return nil, ctx.Err()
		}

		// افزایش شمارنده و تاخیر
		numRetries++
		delay = time.Duration(math.Min(float64(delay*2), float64(maxDelay)))
	}
}

func main() {
	// تنظیم کلاینت
	config := openai.DefaultConfig(os.Getenv("AVALAI_API_KEY"))
	config.BaseURL = "https://api.avalai.ir/v1"
	client := openai.NewClientWithConfig(config)

	// تعریف تابع ارسال درخواست
	getChatCompletion := func() (interface{}, error) {
		return client.CreateChatCompletion(
			context.Background(),
			openai.ChatCompletionRequest{
				model: "gpt-5.6-luna",
				Messages: []openai.ChatCompletionMessage{
					{
						Role:    "user",
						Content: "سلام!",
					},
				},
			},
		)
	}

	// ارسال درخواست با منطق تلاش مجدد
	ctx := context.Background()
	result, err := makeApiRequestWithRetry(ctx, getChatCompletion, 5, 1*time.Second, 60*time.Second)

	if err != nil {
		fmt.Fprintf(os.Stderr, "خطا پس از چندین تلاش: %v\n", err)
		os.Exit(1)
	}

	// نمایش پاسخ
	if resp, ok := result.(openai.ChatCompletionResponse); ok {
		fmt.Println(resp.Choices[0].Message.Content)
	} else {
		fmt.Fprintf(os.Stderr, "نوع پاسخ نامعتبر\n")
	}
}
```


## مرجع API بردارهای تعبیه‌سازی (Embeddings)
_source: source-archive/مرجع-API-بردارهای-تعبیه-سازی-Embeddings-6efa96.md_

### تولید تعبیه‌سازی پایه
```go
// مثال گو (Go)
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
	"os"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.CreateEmbeddings(
		context.Background(),
		openai.EmbeddingRequest{
			Model: openai.TextEmbeddingSmall,
			Input: []string{"The food was delicious and the service was excellent."},
		},
	)

	if err != nil {
		fmt.Printf("Embedding error: %v\n", err)
		return
	}

	embeddings := resp.Data[0].Embedding
	fmt.Printf("Length of embedding vector: %d\n", len(embeddings))
	fmt.Printf("First few values: %v\n", embeddings[:5])
}
```


## مرجع API تشخیص متن (OCR)
_source: source-archive/مرجع-API-تشخیص-متن-OCR-61bff2.md_

### درخواست ساده OCR
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type OCRRequest struct {
	Model    string   `json:"model"`
	Document Document `json:"document"`
}

type Document struct {
	Type        string `json:"type"`
	DocumentURL string `json:"document_url"`
}

type OCRResponse struct {
	Pages []struct {
		Index    int    `json:"index"`
		Markdown string `json:"markdown"`
	} `json:"pages"`
	Model  string `json:"model"`
	Object string `json:"object"`
}

func main() {
	apiKey := "YOUR_AVALAI_API_KEY"
	url := "https://api.avalai.ir/v1/ocr"

	reqBody := OCRRequest{
		Model: "mistral-ocr-4-0",
		Document: Document{
			Type:        "document_url",
			DocumentURL: "https://arxiv.org/pdf/2201.04234",
		},
	}

	jsonData, _ := json.Marshal(reqBody)
	req, _ := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	var result OCRResponse
	json.Unmarshal(body, &result)

	for _, page := range result.Pages {
		fmt.Printf("Page %d: %s...\n", page.Index, page.Markdown[:100])
	}
}
```


## مرجع API رتبه‌بندی مجدد (Rerank)
_source: source-archive/مرجع-API-رتبه-بندی-مجدد-Rerank-83aa7f.md_

### رتبه‌بندی مجدد پایه
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

type RerankRequest struct {
	Model     string   `json:"model"`
	Query     string   `json:"query"`
	Documents []string `json:"documents"`
	TopN      int      `json:"top_n,omitempty"`
}

type Document struct {
	Text string `json:"text"`
}

type Result struct {
	Index          int      `json:"index"`
	RelevanceScore float64  `json:"relevance_score"`
	Document       Document `json:"document"`
}

type RerankResponse struct {
	Results []Result `json:"results"`
}

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("لطفا متغیر محیطی AVALAI_API_KEY را تنظیم کنید")
		return
	}

	baseURL := "https://api.avalai.ir/v1"

	reqBody := RerankRequest{
		Model: "cohere.rerank-v3-5:0",
		Query: "مزایای انرژی‌های تجدیدپذیر چیست؟",
		Documents: []string{
			"منابع انرژی تجدیدپذیر مانند خورشید و باد برای مقابله با تغییرات آب و هوایی بسیار مهم هستند.",
			"سوخت‌های فسیلی سنتی اثرات زیست‌محیطی قابل توجهی دارند.",
			"سرمایه‌گذاری در فناوری سبز می‌تواند منجر به رشد اقتصادی و ایجاد شغل شود.",
			"پنل‌های خورشیدی نور خورشید را به برق تبدیل می‌کنند.",
		},
	}

	jsonData, err := json.Marshal(reqBody)
	if err != nil {
		fmt.Printf("خطا در تبدیل درخواست: %v\n", err)
		return
	}

	req, err := http.NewRequest("POST", baseURL+"/rerank", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}

	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("خطا در ارسال درخواست: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("خطا در خواندن پاسخ: %v\n", err)
		return
	}

	if resp.StatusCode != 200 {
		fmt.Printf("خطا: %d - %s\n", resp.StatusCode, string(body))
		return
	}

	var rerankResp RerankResponse
	err = json.Unmarshal(body, &rerankResp)
	if err != nil {
		fmt.Printf("خطا در تجزیه پاسخ: %v\n", err)
		return
	}

	for _, result := range rerankResp.Results {
		fmt.Printf("ایندکس: %d، امتیاز ارتباط: %.4f، سند: %s\n",
			result.Index, result.RelevanceScore, result.Document.Text)
	}
}
```


## مرجع API فایل‌ها (Files)
_source: source-archive/مرجع-API-فایل-ها-Files-44ecdd.md_

### مثال‌ها
```go
// مثال Go
package main

import (
	"context"
	"fmt"
	"io"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	file, err := os.Open("document.pdf")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	uploaded, err := client.Files.New(context.Background(), openai.FileNewParams{
		File:    openai.F[io.Reader](file),
		Purpose: openai.F(openai.FilePurposeUserData),
	})
	if err != nil {
		panic(err)
	}

	fmt.Printf("فایل آپلود شد: %s\n", uploaded.ID)
}
```

### مثال‌ها
```go
// مثال Go
package main

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

	files, err := client.Files.List(context.Background(), openai.FileListParams{})
	if err != nil {
		panic(err)
	}

	for _, file := range files.Data {
		fmt.Printf("%s: %s (%d بایت)\n", file.ID, file.Filename, file.Bytes)
	}
}
```

### مثال‌ها
```go
// مثال Go
package main

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

	file, err := client.Files.Get(context.Background(), "file-abc123")
	if err != nil {
		panic(err)
	}

	fmt.Printf("نام فایل: %s\n", file.Filename)
	fmt.Printf("اندازه: %d بایت\n", file.Bytes)
	fmt.Printf("هدف: %s\n", file.Purpose)
}
```

### مثال‌ها
```go
// مثال Go
package main

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

	deleted, err := client.Files.Delete(context.Background(), "file-abc123")
	if err != nil {
		panic(err)
	}

	fmt.Printf("حذف شد: %v\n", deleted.Deleted)
}
```

### مثال‌ها
```go
// مثال Go
package main

import (
	"context"
	"io"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	content, err := client.Files.Content(context.Background(), "file-abc123")
	if err != nil {
		panic(err)
	}

	file, err := os.Create("downloaded_file.pdf")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	io.Copy(file, content.Body)
}
```

### مثال: تکمیل گفتگو با فایل
```go
// مثال Go
package main

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

	// استفاده از فایل آپلود شده در تکمیل گفتگو
	response, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
		Model: openai.F("gemini-2.5-flash"),
		Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
			openai.UserMessageParts(
				openai.TextPart("این سند را خلاصه کن"),
				openai.FilePart("file-abc123"),
			),
		}),
	})
	if err != nil {
		panic(err)
	}

	fmt.Println(response.Choices[0].Message.Content)
}
```


## مرجع API مدل‌ها
_source: source-archive/مرجع-API-مدل-ها-fefc4a.md_

### نمونه درخواست (فرمت OpenAI)
```go
package main

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

	models, err := client.Models.List(context.Background())
	if err != nil {
		panic(err)
	}

	for _, model := range models.Data {
		fmt.Printf("%s - %s\n", model.ID, model.OwnedBy)
	}
}
```

### نمونه درخواست
```go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

func main() {
	resp, err := http.Get("https://api.avalai.ir/public/models")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	var result map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&result)

	data := result["data"].([]interface{})
	for _, model := range data {
		m := model.(map[string]interface{})
		fmt.Printf("%s - %s\n", m["id"], m["owned_by"])
	}
}
```

### نمونه درخواست (فرمت OpenAI)
```go
package main

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

	model, err := client.Models.Get(context.Background(), "gpt-5.6-luna")
	if err != nil {
		panic(err)
	}

	fmt.Printf("Model: %s\n", model.ID)
	fmt.Printf("Owned by: %s\n", model.OwnedBy)
}
```


## مرجع API پاسخ‌ها
_source: source-archive/مرجع-API-پاسخ-ها-c0f6f3.md_

### درخواست نمونه (ورودی متنی)
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}

	body := []byte(`{
		"model": "gpt-5.6-luna",
		"input": "یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو."
	}`)

	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/responses", bytes.NewReader(body))
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Printf("خطای درخواست API: %v\n", err)
		return
	}
	defer resp.Body.Close()

	responseBody, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("خطا در خواندن پاسخ: %v\n", err)
		return
	}

	if resp.StatusCode >= 400 {
		fmt.Printf("خطای HTTP %d: %s\n", resp.StatusCode, responseBody)
		return
	}

	var result struct {
		Output []struct {
			Type    string `json:"type"`
			Content []struct {
				Type string `json:"type"`
				Text string `json:"text"`
			} `json:"content"`
		} `json:"output"`
	}
	if err := json.Unmarshal(responseBody, &result); err != nil {
		fmt.Printf("خطا در رمزگشایی JSON: %v\n", err)
		return
	}

	for _, item := range result.Output {
		if item.Type != "message" {
			continue
		}
		for _, part := range item.Content {
			if part.Type == "output_text" {
				fmt.Println(part.Text)
			}
		}
	}
}
```

### درخواست نمونه
```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}
	responseID := "resp_123" // شناسه پاسخی که باید بازیابی شود

	req, err := http.NewRequestWithContext(
		context.Background(),
		http.MethodGet,
		"https://api.avalai.ir/v1/responses/"+responseID,
		nil,
	)
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Accept", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Printf("خطای درخواست API: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("خطا در خواندن پاسخ: %v\n", err)
		return
	}

	if resp.StatusCode >= 400 {
		fmt.Printf("خطای HTTP %d: %s\n", resp.StatusCode, body)
		return
	}

	var result map[string]any
	if err := json.Unmarshal(body, &result); err != nil {
		fmt.Printf("خطا در رمزگشایی JSON: %v\n", err)
		return
	}
	fmt.Printf("%+v\n", result)
}
```

### درخواست نمونه
```go
package main

import (
	"context"
	"fmt"
	"net/http"
	"os"
	// "io" // برای خواندن بدنه پاسخ از حالت کامنت خارج کنید

	openai "github.com/openai/openai-go" // کتابخانه ممکن است مستقیما از این پشتیبانی نکند
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}
	responseID := "resp_123" // شناسه پاسخی که باید حذف شود

	config := openai.DefaultConfig(apiKey)
	// تنظیم URL پایه AvalAI
	config.BaseURL = "https://api.avalai.ir/v1"

	// توجه: کتابخانه openai-go احتمالا متدی برای حذف 'responses' سفارشی ندارد.
	// یک درخواست HTTP DELETE خام رویکرد استاندارد است.

	fmt.Printf("تلاش برای حذف پاسخ با شناسه: %s با استفاده از HTTP DELETE خام\n", responseID)

	req, err := http.NewRequestWithContext(context.Background(), "DELETE", config.BaseURL+"/responses/"+responseID, nil)
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}
	req.Header.Set("Authorization", "Bearer "+apiKey)

	httpClient := &http.Client{}
	resp, err := httpClient.Do(req)
	if err != nil {
		fmt.Printf("خطا در انجام درخواست: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// body, _ := io.ReadAll(resp.Body) // خواندن بدنه برای پیام‌های خطای احتمالی

	if resp.StatusCode >= 200 && resp.StatusCode < 300 {
		fmt.Printf("پاسخ %s با موفقیت حذف شد (کد وضعیت: %d)\n", responseID, resp.StatusCode)
		// تجزیه بدنه در صورت نیاز: به عنوان مثال، json.Unmarshal(body, &deleteConfirmation)
	} else {
		fmt.Printf("خطای HTTP: %d\n", resp.StatusCode)
		// fmt.Printf("بدنه پاسخ: %s\n", string(body))
	}
}
```

### درخواست نمونه
```go
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"

	openai "github.com/openai/openai-go" // برای پیکربندی استفاده می‌شود، اما درخواست HTTP خام است
)

// تعریف ساختارها برای نمایش ساختار پاسخ JSON مورد انتظار
type InputItemList struct {
	Object  string      `json:"object"`
	Data    []InputItem `json:"data"`
	FirstID string      `json:"first_id"`
	LastID  string      `json:"last_id"`
	HasMore bool        `json:"has_more"`
}

type InputItem struct {
	ID      string         `json:"id"`
	Type    string         `json:"type"`
	Role    string         `json:"role"` // با فرض اینکه نوع 'message' نقش دارد
	Content []InputContent `json:"content"`
}

type InputContent struct {
	Type string `json:"type"`
	Text string `json:"text"` // با فرض نوع 'input_text'
}

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}
	responseID := "resp_abc123" // شناسه پاسخ

	config := openai.DefaultConfig(apiKey)
	// تنظیم URL پایه AvalAI
	config.BaseURL = "https://api.avalai.ir/v1"

	// توجه: کتابخانه openai-go متدی برای لیست کردن آیتم‌های ورودی یک 'response' سفارشی ندارد.
	// یک درخواست HTTP GET خام لازم است.

	fmt.Printf("تلاش برای لیست کردن آیتم‌های ورودی برای شناسه پاسخ: %s با استفاده از HTTP GET خام\n", responseID)

	// ساخت URL با پارامترهای کوئری بالقوه
	endpointURL, _ := url.Parse(config.BaseURL + "/responses/" + responseID + "/input_items")
	queryParams := url.Values{}
	// queryParams.Add("limit", "10") // مثال پارامتر کوئری
	endpointURL.RawQuery = queryParams.Encode()

	req, err := http.NewRequestWithContext(context.Background(), "GET", endpointURL.String(), nil)
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Accept", "application/json")

	httpClient := &http.Client{}
	resp, err := httpClient.Do(req)
	if err != nil {
		fmt.Printf("خطا در انجام درخواست: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("خطا در خواندن بدنه پاسخ: %v\n", err)
		return
	}

	if resp.StatusCode >= 400 {
		fmt.Printf("خطای HTTP: %d\n", resp.StatusCode)
		fmt.Printf("بدنه پاسخ: %s\n", string(body))
		return
	}

	var itemList InputItemList
	err = json.Unmarshal(body, &itemList)
	if err != nil {
		fmt.Printf("خطا در unmarshal کردن پاسخ JSON: %v\n", err)
		fmt.Printf("بدنه پاسخ خام: %s\n", string(body))
		return
	}

	fmt.Printf("لیست آیتم‌های ورودی با موفقیت بازیابی شد:\n")
	// پردازش itemList در صورت نیاز
	fmt.Printf("%+v\n", itemList)
}
```

### مدیریت جریان
```go
package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strings"
)

type streamEvent struct {
	Type  string `json:"type"`
	Delta string `json:"delta"`
	Error *struct {
		Message string `json:"message"`
	} `json:"error"`
}

func main() {
	payload := []byte(`{
		"model":"gpt-5.6-luna",
		"input":"یک داستان برایم بگو.",
		"stream":true
	}`)

	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/responses", bytes.NewReader(payload))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept", "text/event-stream")
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	fmt.Print("Assistant: ")
	scanner := bufio.NewScanner(resp.Body)
	for scanner.Scan() {
		line := scanner.Text()
		if !strings.HasPrefix(line, "data: ") {
			continue
		}

		data := strings.TrimPrefix(line, "data: ")
		if data == "[DONE]" {
			break
		}

		var event streamEvent
		if err := json.Unmarshal([]byte(data), &event); err != nil {
			continue
		}

		switch event.Type {
		case "response.output_text.delta":
			fmt.Print(event.Delta)
		case "response.completed":
			fmt.Println()
		case "error":
			if event.Error != nil {
				panic(event.Error.Message)
			}
		}
	}
}
```


## مرجع API پیام‌ها
_source: source-archive/مرجع-API-پیام-ها-1edf56.md_

### تکمیل پیام پایه
```go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/anthropic/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient(
		anthropic.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		anthropic.WithBaseURL("https://api.avalai.ir"),
	)

	resp, err := client.Messages.Create(context.Background(), &anthropic.MessagesRequest{
		Model: "anthropic.claude-sonnet-4-20250514-v1:0",
		Messages: []anthropic.Message{
			{
				Role:    "user",
				Content: "سلام! آیا می‌توانید به من کمک کنید تا محاسبات کوانتومی را درک کنم؟",
			},
		},
		MaxTokens: 1024,
	})

	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}

	fmt.Println(resp.Content)
}
```


## مرجع API کاربر (User API)
_source: source-archive/مرجع-API-کاربر-User-API-abd0f7.md_

### احراز هویت
```go
// مثال Go
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/credit", nil)
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	fmt.Println(string(body))
}
```

### درخواست
```go
// مثال Go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

type CreditResponse struct {
	Limit        float64 `json:"limit"`
	RemainingIRT float64 `json:"remaining_irt"`
	AccountTier  int     `json:"account_tier"`
}

func main() {
	req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/credit", nil)
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

	resp, _ := (&http.Client{}).Do(req)
	defer resp.Body.Close()

	var credit CreditResponse
	json.NewDecoder(resp.Body).Decode(&credit)
	fmt.Printf("اعتبار باقیمانده: %.2f تومان\n", credit.RemainingIRT)
}
```

### مثال‌ها
```go
// مثال Go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"
	"os"
)

func main() {
	baseURL := "https://api.avalai.ir/user/v1/transactions"
	params := url.Values{}
	params.Add("model", "gpt-5.6-luna")
	params.Add("hours_ago", "168")
	params.Add("page_size", "50")

	req, _ := http.NewRequest("GET", baseURL+"?"+params.Encode(), nil)
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

	resp, _ := (&http.Client{}).Do(req)
	defer resp.Body.Close()

	var result map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&result)
	fmt.Printf("تعداد کل تراکنش‌ها: %v\n", result["total"])
}
```

### مثال
```go
// مثال Go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"time"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// مرحله ۱: یک فراخوانی API انجام دهید
	chatBody, _ := json.Marshal(map[string]interface{}{
		"model":    "gpt-5.4-mini",
		"messages": []map[string]string{{"role": "user", "content": "سلام!"}},
	})

	req, _ := http.NewRequest("POST", "https://api.avalai.ir/v1/chat/completions", bytes.NewBuffer(chatBody))
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	resp, _ := (&http.Client{}).Do(req)
	requestID := resp.Header.Get("avalai-request-id")
	resp.Body.Close()
	fmt.Printf("شناسه درخواست: %s\n", requestID)

	// مرحله ۲: صبر کنید برای پردازش
	time.Sleep(5 * time.Second)

	// مرحله ۳: جستجوی تراکنش
	lookupBody, _ := json.Marshal(map[string]interface{}{
		"transaction_ids": []string{requestID},
	})

	req, _ = http.NewRequest("POST", "https://api.avalai.ir/user/v1/transactions/lookup", bytes.NewBuffer(lookupBody))
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	resp, _ = (&http.Client{}).Do(req)
	defer resp.Body.Close()

	var result map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&result)
	fmt.Printf("نتیجه: %+v\n", result)
}
```

### مثال‌ها
```go
// مثال Go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

func main() {
	req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/transactions/summary", nil)
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

	resp, _ := (&http.Client{}).Do(req)
	defer resp.Body.Close()

	var result map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&result)
	fmt.Printf("%+v\n", result)
}
```

### مثال‌ها
```go
// مثال Go
req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/transactions/summary?group_by=provider", nil)
req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
```

### مثال‌ها
```go
// مثال Go
req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/transactions/summary?group_by=date&hours_ago=168", nil)
req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
```

### مثال‌ها
```go
// مثال Go - گزارش تفصیلی ساعتی
req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/transactions/summary?group_by=hour&hours_ago=24", nil)
req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

resp, _ := (&http.Client{}).Do(req)
defer resp.Body.Close()

var result map[string]interface{}
json.NewDecoder(resp.Body).Decode(&result)
```

### درخواست
```go
// مثال Go
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/health", nil)
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

	resp, _ := (&http.Client{}).Do(req)
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	fmt.Println(string(body))
}
```


## مرجع مهاجرت API دستیاران (Assistants)
_source: source-archive/مرجع-مهاجرت-API-دستیاران-Assistants-df1a56.md_

### ایجاد یک دستیار
```go
// مثال Go: ایجاد یک دستیار از طریق AvalAI
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY") // یا با کلید خود جایگزین کنید
	if apiKey == "" {
		fmt.Println("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}
	baseURL := "https://api.avalai.ir/v1" // از URL پایه AvalAI استفاده کنید

	config := openai.DefaultConfig(apiKey)
	config.BaseURL = baseURL
	client := openai.NewClientWithConfig(config)

	req := openai.AssistantRequest{
		Model:        "gpt-5.6-luna",
		Name:         openai.NewString("Math Tutor"),
		Instructions: openai.NewString("شما یک معلم خصوصی ریاضی هستید. برای پاسخ به سوالات ریاضی کد بنویسید و اجرا کنید."),
		Tools: []openai.AssistantTool{
			{Type: openai.AssistantToolTypeCodeInterpreter},
		},
		// Description: openai.NewString("توضیحات اختیاری"), // اختیاری
		// Metadata: map[string]interface{}{"user_id": "123"}, // اختیاری
	}

	resp, err := client.CreateAssistant(context.Background(), req)
	if err != nil {
		fmt.Printf("خطا در ایجاد دستیار: %v\n", err)
		return
	}

	fmt.Printf("دستیار با شناسه ایجاد شد: %s\n", resp.ID)
}
```


## مهندسی پرامپت
_source: source-archive/مهندسی-پرامپت-5ce1f0.md_

### پیام‌ها و نقش‌ها
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	payload := map[string]any{
		"model": "gpt-5.6-luna",
		"messages": []map[string]string{
			{
				"role":    "developer",
				"content": "You are a helpful assistant that answers programming questions in the style of a southern belle from the southeast United States.",
			},
			{
				"role":    "user",
				"content": "Are semicolons optional in JavaScript?",
			},
		},
	}

	body, err := json.Marshal(payload)
	if err != nil {
		panic(err)
	}

	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/chat/completions", bytes.NewBuffer(body))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	responseBody, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(responseBody))
}
```

### پیام‌ها و نقش‌ها
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	payload := map[string]any{
		"model":        "gpt-5.6-luna",
		"instructions": "You are a helpful assistant that answers programming questions in the style of a southern belle from the southeast United States.",
		"input":        "Are semicolons optional in JavaScript?",
	}

	body, err := json.Marshal(payload)
	if err != nil {
		panic(err)
	}

	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/responses", bytes.NewBuffer(body))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	responseBody, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(string(responseBody))
}
```


## هدرهای پاسخ
_source: source-archive/هدرهای-پاسخ-a617d7.md_

### مثال کامل هدرهای پاسخ
```go
// مثال Go - دسترسی به هدرهای پاسخ
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

func main() {
	body, _ := json.Marshal(map[string]interface{}{
		"model":    "gpt-5.4-mini",
		"messages": []map[string]string{{"role": "user", "content": "سلام"}},
	})

	req, _ := http.NewRequest("POST", "https://api.avalai.ir/v1/chat/completions", bytes.NewBuffer(body))
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, _ := (&http.Client{}).Do(req)
	defer resp.Body.Close()

	// دسترسی به هدرها
	requestID := resp.Header.Get("avalai-request-id")
	remainingRequests := resp.Header.Get("x-ratelimit-remaining-requests")
	remainingTokens := resp.Header.Get("x-ratelimit-remaining-tokens")
	resetTime := resp.Header.Get("x-ratelimit-reset-requests")

	fmt.Printf("شناسه درخواست: %s\n", requestID)
	fmt.Printf("درخواست‌های باقی‌مانده: %s\n", remainingRequests)
	fmt.Printf("توکن‌های باقی‌مانده: %s\n", remainingTokens)
	fmt.Printf("زمان بازنشانی: %s\n", resetTime)
}
```


## هوش مصنوعی در رباتیک با Gemini Robotics-ER
_source: source-archive/هوش-مصنوعی-در-رباتیک-با-Gemini-Robotics-ER-71c007.md_

### پیش‌نیازها
```go
# نصب OpenAI Go SDK
go get github.com/openai/openai-go
```

### مثال: تشخیص اشیاء روی میز
```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"os"

	"github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	// خواندن و رمزگذاری تصویر
	imageData, _ := os.ReadFile("workspace.jpg")
	base64Image := base64.StdEncoding.EncodeToString(imageData)

	resp, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
		Model: openai.F("gemini-robotics-er-1.5-preview"),
		Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
			openai.UserMessage([]openai.ChatCompletionContentPartUnionParam{
				openai.TextPart("Identify objects and return 2D coordinates in JSON format"),
				openai.ImagePart("data:image/jpeg;base64," + base64Image),
			}),
		}),
	})

	if err != nil {
		panic(err)
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```


## پاسخ‌های API جریانی
_source: source-archive/پاسخ-های-API-جریانی-66d055.md_

### فعال‌سازی جریان
```go
package main

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("AVALAI_API_KEY تنظیم نشده است")
		return
	}

	body := `{
		"model": "gpt-5.6-luna",
		"input": "عبارت 'double bubble bath' را ده بار سریع بگو.",
		"stream": true
	}`

	ctx := context.Background()
	req, err := http.NewRequestWithContext(
		ctx,
		http.MethodPost,
		"https://api.avalai.ir/v1/responses",
		strings.NewReader(body),
	)
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept", "text/event-stream")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Printf("خطا در درخواست جریان: %v\n", err)
		return
	}
	defer resp.Body.Close()

	fmt.Println("پاسخ جریانی:")
	if _, err := io.Copy(os.Stdout, resp.Body); err != nil {
		fmt.Printf("\nخطا در خواندن جریان: %v\n", err)
	}
}
```


## پردازش اسناد با Mistral OCR
_source: source-archive/پردازش-اسناد-با-Mistral-OCR-46ed5d.md_

### استفاده از URL فایل PDF
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]interface{}{
			"type":         "document_url",
			"document_url": "https://arxiv.org/pdf/1805.04770",
		},
		"pages": make([]int, 100), // Process pages 0-99
	}

	// Fill pages array
	for i := 0; i < 100; i++ {
		payload["pages"].([]int)[i] = i
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Print response
	fmt.Println(string(body))
}
```

### استفاده از PDF کدگذاری شده با Base64
```go
package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// Read and encode the PDF file
	pdfBytes, err := ioutil.ReadFile("document.pdf")
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}
	base64String := base64.StdEncoding.EncodeToString(pdfBytes)
	documentUrl := "data:application/pdf;base64," + base64String

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]interface{}{
			"type":         "document_url",
			"document_url": documentUrl,
		},
		"pages": make([]int, 100), // Process pages 0-99
	}

	// Fill pages array
	for i := 0; i < 100; i++ {
		payload["pages"].([]int)[i] = i
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Print response
	fmt.Println(string(body))
}
```

### پردازش صفحات خاص
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]interface{}{
			"type":         "document_url",
			"document_url": "https://arxiv.org/pdf/1805.04770",
		},
		"pages": []int{0, 1, 5}, // Process only specific pages
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Print response
	fmt.Println(string(body))
}
```

### استفاده از URL تصویر
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]interface{}{
			"type":      "image_url",
			"image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
		},
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Print response
	fmt.Println(string(body))
}
```

### استفاده از تصاویر کدگذاری شده با Base64
```go
package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// Read and encode the image file
	imageBytes, err := ioutil.ReadFile("receipt.jpg")
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}
	base64String := base64.StdEncoding.EncodeToString(imageBytes)
	imageUrl := "data:image/jpeg;base64," + base64String

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]interface{}{
			"type":      "image_url",
			"image_url": imageUrl,
		},
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Print response
	fmt.Println(string(body))
}
```

### پاسخگویی به سؤالات با مقالات علمی
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// Create message content with both text and document
	textContent := map[string]interface{}{
		"type": "text",
		"text": "What is the main research question addressed in this paper?",
	}
	documentContent := map[string]interface{}{
		"type":         "document_url",
		"document_url": "https://arxiv.org/pdf/1805.04770",
	}

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-small-latest",
		"messages": []map[string]interface{}{
			{
				"role":    "user",
				"content": []map[string]interface{}{textContent, documentContent},
			},
		}
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/chat/completions", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Parse response to extract message content
	var result map[string]interface{}
	if err := json.Unmarshal(body, &result); err != nil {
		fmt.Printf("Error parsing response: %v\n", err)
		return
	}

	// Extract and print the message content
	choices := result["choices"].([]interface{})
	firstChoice := choices[0].(map[string]interface{})
	message := firstChoice["message"].(map[string]interface{})
	content := message["content"].(string)

	fmt.Println(content)
}
```

### استخراج اطلاعات از رسیدها
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// Create message content with both text and image
	textContent := map[string]interface{}{
		"type": "text",
		"text": "Extract the following information from this receipt: store name, date, total amount, and list of purchased items with prices.",
	}
	imageContent := map[string]interface{}{
		"type":      "image_url",
		"image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
	}

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-small-latest",
		"messages": []map[string]interface{}{
			{
				"role":    "user",
				"content": []map[string]interface{}{textContent, imageContent},
			},
		}
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/chat/completions", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Parse response to extract message content
	var result map[string]interface{}
	if err := json.Unmarshal(body, &result); err != nil {
		fmt.Printf("Error parsing response: %v\n", err)
		return
	}

	// Extract and print the message content
	choices := result["choices"].([]interface{})
	firstChoice := choices[0].(map[string]interface{})
	message := firstChoice["message"].(map[string]interface{})
	content := message["content"].(string)

	fmt.Println(content)
}
```


## پردازش فایل های PDF با API AvalAI
_source: source-archive/پردازش-فایل-های-PDF-با-API-AvalAI-4a49a9.md_

### پردازش PDF مبتنی بر URL
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// آدرس PDF
	fileUrl := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

	// ایجاد درخواست با ارجاع به فایل مبتنی بر URL
	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "این سند درباره چیست؟",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileID: fileUrl,
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-5",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### پردازش PDF مبتنی بر کدگذاری base64
```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	openai "github.com/openai/openai-go"
	"io/ioutil"
	"net/http"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// دریافت داده PDF
	pdfData, err := getPDFData()
	if err != nil {
		fmt.Printf("Error getting PDF data: %v\n", err)
		return
	}

	// کدگذاری داده PDF به base64
	encodedFile := base64.StdEncoding.EncodeToString(pdfData)
	base64URL := fmt.Sprintf("data:application/pdf;base64,%s", encodedFile)

	// ایجاد درخواست با فایل کدگذاری شده با base64
	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "این سند درباره چیست؟",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileData: base64URL,
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-5",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

// تابع دریافت داده PDF از URL یا فایل محلی
func getPDFData() ([]byte, error) {
	// روش 1: از یک URL
	pdfURL := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
	resp, err := http.Get(pdfURL)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	return ioutil.ReadAll(resp.Body)

	// روش 2: از یک فایل محلی
	// return ioutil.ReadFile("path/to/your/document.pdf")
}
```

### مشخص کردن فرمت
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// آدرس PDF
	fileUrl := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

	// ایجاد درخواست با مشخص کردن فرمت
	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "این سند درباره چیست؟",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileID: fileUrl,
				Format: "application/pdf",
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-5",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### خلاصه‌سازی اسناد
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	fileUrl := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "خلاصه‌ای مختصر از این سند ارائه دهید.",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileID: fileUrl,
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-5",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```

### استخراج اطلاعات
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	fileUrl := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "تمام تاریخ‌های ذکر شده در این سند را استخراج کرده و به ترتیب زمانی فهرست کنید.",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileID: fileUrl,
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-5",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
```


## پردازش فایل‌های اکسل با API AvalAI
_source: source-archive/پردازش-فایل-های-اکسل-با-API-AvalAI-899b49.md_

### پردازش اکسل با کدگذاری base64
```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	openai "github.com/openai/openai-go"
	"io/ioutil"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// دریافت داده اکسل
	excelData, err := getExcelData()
	if err != nil {
		fmt.Printf("خطا در دریافت داده اکسل: %v\n", err)
		return
	}

	// کدگذاری داده اکسل به base64
	encodedFile := base64.StdEncoding.EncodeToString(excelData)
	base64URL := fmt.Sprintf("data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,%s", encodedFile)

	// ایجاد درخواست با فایل کدگذاری شده با base64
	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "این صفحه گسترده را تحلیل کرده و بینش‌های کلیدی ارائه دهید.",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileData: base64URL,
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا در ChatCompletion: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

// تابع دریافت داده اکسل از فایل محلی
func getExcelData() ([]byte, error) {
	// از یک فایل محلی
	return ioutil.ReadFile("path/to/your/spreadsheet.xlsx")
}
```

### تبدیل DataFrame
```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
	"github.com/xuri/excelize/v2"
	"os"
	"strings"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// تبدیل اکسل به نمایش متنی
	excelText, err := excelToText("path/to/your/spreadsheet.xlsx")
	if err != nil {
		fmt.Printf("خطا در تبدیل اکسل: %v\n", err)
		return
	}

	// ایجاد پرامپت با داده‌های اکسل
	prompt := fmt.Sprintf(`
من داده‌های صفحه گسترده زیر را دارم:

%s

لطفا این داده‌ها را تحلیل کرده و بینش‌های کلیدی ارائه دهید.
`, excelText)

	// ارسال درخواست به مدل
	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-4-6",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: prompt,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا در ChatCompletion: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

// تابع تبدیل اکسل به نمایش متنی
func excelToText(filePath string) (string, error) {
	// باز کردن فایل اکسل
	f, err := excelize.OpenFile(filePath)
	if err != nil {
		return "", err
	}
	defer f.Close()

	// دریافت همه نام‌های کاربرگ
	sheets := f.GetSheetList()
	if len(sheets) == 0 {
		return "", fmt.Errorf("هیچ کاربرگی یافت نشد")
	}

	// دریافت همه سطرها از اولین کاربرگ
	rows, err := f.GetRows(sheets[0])
	if err != nil {
		return "", err
	}

	// تبدیل به نمایش متنی
	var sb strings.Builder
	for _, row := range rows {
		sb.WriteString(strings.Join(row, "\t"))
		sb.WriteString("\n")
	}

	return sb.String(), nil
}
```

