# PHP samples extracted verbatim from the AvalAI docs (104 blocks)

Grouped by source page. These are the docs' own samples — several are **known broken or stale** (wrong constructor names, stale model ids, fictional helpers). Treat as intent, then use `examples/multi-language-clients.md` + `examples/laravel-complete-guide.md` for vetted code. Always replace model ids after `scripts/avalai_live.py check`.

## API تنظیم دقیق (Fine-tuning)
_source: source-archive/API-تنظیم-دقیق-Fine-tuning-1258de.md_

### ایجاد یک کار تنظیم دقیق
```php
<?php
// مثال PHP: ایجاد یک کار تنظیم دقیق از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/fine-tuning/jobs'; // از URL پایه AvalAI استفاده کنید

$data = [
'model' => 'fine-tunable-model-id',
'training_file' => 'file-abc123',
'validation_file' => 'file-def456', // اختیاری
'hyperparameters' => [ // اختیاری
'n_epochs' => 4
]
// 'suffix' => 'my-custom-model' // اختیاری
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json',
'Authorization: Bearer ' . $apiKey,
'Content-Length: ' . strlen($jsonData)
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #:" . $err;
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "پاسخ: " . $response;
} else {
  echo "پاسخ ایجاد کار تنظیم دقیق:\n";
  echo $response;
  // $responseData = json_decode($response, true);
  // print_r($responseData);
}
?>
```


## API تکمیل گفتگو (Chat Completions)
_source: source-archive/API-تکمیل-گفتگو-Chat-Completions-720a31.md_

### تکمیل گفتگوی پایه
```php
<?php
// مثال PHP برای تکمیل گفتگو از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

$data = [
'model' => 'gpt-5.6-sol',
'messages' => [
['role' => 'system', 'content' => 'You are a helpful assistant.'], // محتوای سیستم به انگلیسی باقی می‌ماند یا ترجمه می‌شود؟
['role' => 'user', 'content' => 'Hello!'] // محتوای کاربر به انگلیسی باقی می‌ماند یا ترجمه می‌شود؟
]
// در صورت نیاز پارامترهای دیگری مانند دما، حداکثر توکن و غیره را اضافه کنید
// 'temperature' => 0.7,
// 'max_tokens' => 150
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json',
'Authorization: Bearer ' . $apiKey,
'Content-Length: ' . strlen($jsonData)
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #:" . $err;
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo $response;
} else {
  $responseData = json_decode($response, true);
  if (isset($responseData['choices'][0]['message']['content'])) {
    echo "دستیار: " . $responseData['choices'][0]['message']['content'] . "\n";
  } else {
    echo "پاسخ دریافت شد:\n";
    print_r($responseData);
  }
}
?>
```

### تولید صوتی پایه
```php
<?php

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
            'content' => 'محاسبات کوانتومی را به زبان ساده توضیح بده.',
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


## Responses در مقابل Chat Completions
_source: source-archive/Responses-در-مقابل-Chat-Completions-41c940.md_

### مثال تولید متن
```php
<?php
// Chat Completions API
require 'vendor/autoload.php';

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$result = $client->chat()->create([
 'model' => 'gpt-5.6-luna',
 'messages' => [
 ['role' => 'user', 'content' => 'یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس.'],
 ],
]);

echo $result->choices[0]->message->content;

// Responses API
$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$result = $client->responses()->create([
 'model' => 'gpt-5.6-luna',
 'input' => [
 ['role' => 'user', 'content' => 'یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس.'],
 ],
]);

echo $result->output_text;
?>
```


## ابزار جستجوی وب
_source: source-archive/ابزار-جستجوی-وب-0b5010.md_

### مثال ابزار جستجوی وب
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php'); // با فرض بارگذاری خودکار Composer

$apiKey = getenv('AVALAI_API_KEY');
$client = OpenAI::client($apiKey, ["base_uri" => "https://api.avalai.ir/v1"]); // استفاده از کلاینت PHP OpenAI با آدرس پایه سفارشی

$response = $client->responses()->create([
'model' => 'gpt-5.6-luna',
'tools' => [['type' => 'web_search']],
'input' => 'یک خبر مثبت از امروز چه بود؟',
]);

echo $response->output_text;
?>
```

### سفارشی‌سازی موقعیت مکانی کاربر
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php'); // با فرض بارگذاری خودکار Composer

$apiKey = getenv('AVALAI_API_KEY');
$client = OpenAI::client($apiKey, ["base_uri" => "https://api.avalai.ir/v1"]); // استفاده از کلاینت PHP OpenAI با آدرس پایه سفارشی

$response = $client->responses()->create([
'model' => 'gpt-5.6-luna',
'tools' => [[
'type' => 'web_search',
'user_location' => [
'type' => 'approximate',
'country' => 'GB',
'city' => 'London',
'region' => 'London',
]
]],
'input' => 'بهترین رستوران‌های اطراف میدان گرنری کدامند؟',
]);

echo $response->output_text;
?>
```

### سفارشی‌سازی اندازه زمینه جستجو
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php'); // با فرض بارگذاری خودکار Composer

$apiKey = getenv('AVALAI_API_KEY');
$client = OpenAI::client($apiKey, ["base_uri" => "https://api.avalai.ir/v1"]); // استفاده از کلاینت PHP OpenAI با آدرس پایه سفارشی

$response = $client->responses()->create([
'model' => 'gpt-5.6-luna',
'tools' => [[
'type' => 'web_search',
'search_context_size' => 'low',
]],
'input' => 'کدام فیلم در سال ۲۰۲۵ برنده بهترین فیلم شد؟',
]);

echo $response->output_text;
?>
```


## ابزارها
_source: source-archive/ابزارها-673bf2.md_

### ابزارها
```php
<?php

$apiKey = getenv('AVALAI_API_KEY');
$payload = [
    'model' => 'gpt-5.6-luna',
    'tools' => [['type' => 'web_search']],
    'input' => 'What was a positive news story from today?',
];

$ch = curl_init('https://api.avalai.ir/v1/responses');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . $apiKey,
        'Content-Type: application/json',
    ],
    CURLOPT_POSTFIELDS => json_encode($payload),
]);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```


## استفاده از API جستجوی v1/search
_source: source-archive/استفاده-از-API-جستجوی-v1-search-a402d1.md_

### روش 1: مشخص کردن ابزار در URL
```php
<?php

$apiKey = getenv('AVALAI_API_KEY');

$data = [
    'query' => 'آخرین پیشرفت‌ها در محاسبات کوانتومی',
    'max_results' => 5
];

$ch = curl_init('https://api.avalai.ir/v1/search/perplexity-search');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

$response = curl_exec($ch);
curl_close($ch);

$results = json_decode($response, true);
print_r($results);
```

### روش 2: مشخص کردن ابزار در بدنه درخواست
```php
<?php

$apiKey = getenv('AVALAI_API_KEY');

$data = [
    'search_tool_name' => 'tavily-search',
    'query' => 'تاثیر تغییرات اقلیمی بر یخ‌های قطبی',
    'max_results' => 10
];

$ch = curl_init('https://api.avalai.ir/v1/search');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

$response = curl_exec($ch);
curl_close($ch);

$results = json_decode($response, true);

foreach ($results['results'] ?? [] as $result) {
    echo "عنوان: " . $result['title'] . "\n";
    echo "URL: " . $result['url'] . "\n";
    echo "اسنیپت: " . $result['snippet'] . "\n";
    echo "---\n";
}
```


## استفاده از قابلیت‌های جستجوی وب در مدل‌های زبانی بزرگ (LLM)
_source: source-archive/استفاده-از-قابلیت-های-جستجوی-وب-در-مدل-های-زبانی-ب-760462.md_

### جستجوی داخلی با مدل‌های OpenAI
```php
<?php

require 'vendor/autoload.php';

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

$completion = $client->chat()->create([
 'model' => 'gpt-4o-search-preview',
 'messages' => [
 [
 'role' => 'user',
 'content' => 'what\'s the news today?'
 ]
 ],
 'response_format' => [
 'type' => 'text'
 ],
 'store' => false
]);

// چاپ پاسخ
echo $completion->choices[0]->message->content;
```

### جستجو با مدل‌های OpenAI از طریق ابزار
```php
<?php

require 'vendor/autoload.php';

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

$response = $client->responses()->create([
 'model' => 'gpt-5.6-luna',
 'tools' => [['type' => 'web_search']],
 'input' => 'What was a positive news story from today?'
]);

// چاپ متن خروجی
echo $response->output_text;
```

### جستجو با مدل‌های Gemini
```php
<?php

require 'vendor/autoload.php';

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

$completion = $client->chat()->create([
 'model' => 'gemini-2.5-flash',
 'messages' => [
 [
 'role' => 'system',
 'content' => 'You are a helpful assistant.'
 ],
 [
 'role' => 'user',
 'content' => 'whats the news?'
 ]
 ],
 'tools' => [
 ['googleSearch' => new stdClass()]
 ]
]);

// چاپ پاسخ
echo $completion->choices[0]->message->content;
```

### جستجو با مدل‌های Alibaba (Qwen)
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$completion = $client->chat()->create([
 'model' => 'qwen3.7-max',
 'messages' => [
  [
   'role' => 'user',
   'content' => 'قیمت فعلی سهام تسلا چقدر است؟'
  ]
 ],
 'enable_search' => true,
 'search_options' => ['search_strategy' => 'agent']
]);

// چاپ پاسخ
echo $completion->choices[0]->message->content;
```

### جستجوی اخبار روز
```php
<?php

require 'vendor/autoload.php';

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

$completion = $client->chat()->create([
 'model' => 'gpt-4o-search-preview',
 'messages' => [
 [
 'role' => 'user',
 'content' => 'What are the major headlines today?'
 ]
 ]
]);

// چاپ پاسخ
echo $completion->choices[0]->message->content;
```

### پاسخ به پرسش‌های مبتنی بر واقعیت
```php
<?php

require 'vendor/autoload.php';

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

$completion = $client->chat()->create([
 'model' => 'gpt-4o-search-preview',
 'messages' => [
 [
 'role' => 'user',
 'content' => 'Who won the most recent Nobel Prize in Physics and what was their contribution?'
 ]
 ]
]);

// چاپ پاسخ
echo $completion->choices[0]->message->content;
```

### پارامترهای جستجو برای مدل‌های OpenAI
```php
<?php

require 'vendor/autoload.php';

$client = OpenAI::client('your-avalai-api-key', [
 'base_url' => 'https://api.avalai.ir/v1'
]);

$completion = $client->chat()->create([
 'model' => 'gpt-4o-search-preview',
 'messages' => [
 [
 'role' => 'user',
 'content' => 'What happened in the financial markets today?'
 ]
 ],
 'temperature' => 0.2, // دمای پایین‌تر برای پاسخ‌های واقعی‌تر
 'response_format' => [
 'type' => 'text' // برای پاسخ‌های فقط متنی
 ]
]);

// چاپ پاسخ
echo $completion->choices[0]->message->content;
```

### پارامترهای جستجو برای مدل‌های Gemini
```php
<?php

require 'vendor/autoload.php';

$client = OpenAI::client('your-avalai-api-key', [
 'base_url' => 'https://api.avalai.ir/v1'
]);

$detailLevel = new stdClass();
$detailLevel->detail_level = "high";

$completion = $client->chat()->create([
 'model' => 'gemini-2.5-flash',
 'messages' => [
 [
 'role' => 'user',
 'content' => 'What are the latest developments in quantum computing?'
 ]
 ],
 'tools' => [
 ['googleSearch' => $detailLevel]
 ]
]);

// چاپ پاسخ
echo $completion->choices[0]->message->content;
```

### نحوه پردازش ارجاعات
```php
<?php
// برای API پاسخ‌ها
$response = $client->responses()->create([
 'model' => 'gpt-5.6-luna',
 'tools' => [['type' => 'web_search']],
 'input' => 'What was a positive news story from today?'
]);

// استخراج استنادات
$content = $response->output_text;
$annotations = $response->annotations;

foreach ($annotations as $annotation) {
 if ($annotation->type === 'url_citation') {
 $url = $annotation->url;
 $title = $annotation->title;
 $start = $annotation->start_index;
 $end = $annotation->end_index;
 
 // پردازش استناد بر اساس نیاز
 echo "Citation: {$title} - {$url}\n";
 }
}
```


## بهترین شیوه‌های Production
_source: source-archive/بهترین-شیوه-های-Production-010cee.md_

### پاسخ‌های جریانی (Streaming)
```php
<?php
require 'vendor/autoload.php';

$client = OpenAI::client(getenv('AVALAI_API_KEY'), [
 'base_url' => 'https://api.avalai.ir/v1',
]);

$stream = $client->chat()->createStreamed([
 'model' => 'gpt-5.6-luna',
 'messages' => [
 ['role' => 'user', 'content' => 'داستانی درباره یک کاوشگر فضایی بنویس'],
 ],
]);

foreach ($stream as $response) {
 if ($response->choices[0]->delta->content) {
 echo $response->choices[0]->delta->content;
 ob_flush();
 flush();
 }
}
?>
```

### پردازش ناهمزمان
```php
<?php
require 'vendor/autoload.php';

$client = OpenAI::client('AVALAI_API_KEY', [
 'base_url' => 'https://api.avalai.ir/v1',
]);

function generateResponse($client, $prompt) {
 $response = $client->chat()->create([
 'model' => 'gpt-5.6-luna',
 'messages' => [
 ['role' => 'user', 'content' => $prompt],
 ],
 ]);

 return $response->choices[0]->message->content;
}

$prompts = ["سلام", "حالت چطوره؟", "هوا چطوره؟"];
$results = [];

// استفاده از درخواست‌های موازی با وعده‌ها
$promises = [];
foreach ($prompts as $index => $prompt) {
 $promises[$index] = new Promise(function($resolve, $reject) use ($client, $prompt) {
 try {
 $result = generateResponse($client, $prompt);
 $resolve($result);
 } catch (Exception $e) {
 $reject($e);
 }
 });
}

$results = Promise\all($promises)->wait();
print_r($results);
?>
```


## بهترین شیوه‌های RAG
_source: source-archive/بهترین-شیوه-های-RAG-061e85.md_

### بهترین شیوه‌ها
```php
<?php
// استفاده از PHP برای طبقه‌بندی یک پرس و جو

$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

function classifyQuery($query, $apiKey, $apiUrl) {
    $data = [
        'model' => 'gpt-5.6-luna',
        'messages' => [
            [
                'role' => 'system',
                'content' => "You are a query classifier. Respond with 'RETRIEVE' if the query requires external knowledge, or 'SUFFICIENT' if the model's knowledge is enough."
            ],
            [
                'role' => 'user',
                'content' => $query
            ]
        ]
    ];

    $jsonData = json_encode($data);

    $ch = curl_init($apiUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . $apiKey,
        'Content-Length: ' . strlen($jsonData)
    ]);

    $response = curl_exec($ch);
    $err = curl_error($ch);
    curl_close($ch);

    if ($err) {
        throw new Exception("خطای cURL: " . $err);
    }

    $responseData = json_decode($response, true);
    $classification = $responseData['choices'][0]['message']['content'];

    return strpos($classification, 'RETRIEVE') !== false;
}

// مثال استفاده
$query = "What were the key announcements at AvalAI's 2025 developer conference?";
try {
    $needsRetrieval = classifyQuery($query, $apiKey, $apiUrl);

    if ($needsRetrieval) {
        // ادامه با جریان کاری RAG
        echo "درحال بازیابی اطلاعات خارجی...";
    } else {
        // استفاده از تکمیل استاندارد
        echo "درحال استفاده از دانش داخلی مدل...";
    }
} catch (Exception $e) {
    echo "خطا: " . $e->getMessage();
}
?>
```

### بهترین شیوه‌ها
```php
<?php
// تکه‌بندی سند بر اساس جملات با همپوشانی

/**
* تابع tokenizer ساده برای جملات
* توجه: برای استفاده تولیدی، از یک کتابخانه NLP قوی‌تر استفاده کنید
*/
function sentenceTokenize($text) {
	// تقسیم بر اساس نقطه، علامت تعجب و علامت سوال که با فاصله‌ها دنبال می‌شوند
	$pattern = '/(?<=[.!?])\s+(?=[A-Z])/';
	$sentences = preg_split($pattern, $text, -1, PREG_SPLIT_NO_EMPTY);

	// تمیز کردن جملات
	$result = [];
	foreach ($sentences as $sentence) {
		$sentence = trim($sentence);
		if (!empty($sentence)) {
			$result[] = $sentence;
		}
	}

	return $result;
}

function chunkDocumentBySentences($document, $maxChunkSize = 512, $overlap = 20) {
	// تقسیم سند به جملات
	$sentences = sentenceTokenize($document);

	$chunks = [];
	$currentChunk = [];
	$currentSize = 0;

	foreach ($sentences as $sentence) {
		// تعداد تقریبی توکن (کلمات + علائم نگارشی)
		$sentenceSize = count(explode(' ', $sentence));

		if ($currentSize + $sentenceSize > $maxChunkSize && count($currentChunk) > 0) {
			// ذخیره تکه فعلی
			$chunks[] = implode(' ', $currentChunk);

			// حفظ جملات همپوشانی برای تکه بعدی
			if ($overlap > 0) {
				$overlapCount = min($overlap, count($currentChunk));
				$overlapSentences = array_slice($currentChunk, -$overlapCount);
				$currentChunk = $overlapSentences;

				// محاسبه مجدد اندازه فعلی
				$currentSize = 0;
				foreach ($overlapSentences as $s) {
					$currentSize += count(explode(' ', $s));
				}
			} else {
				$currentChunk = [];
				$currentSize = 0;
			}
		}

		$currentChunk[] = $sentence;
		$currentSize += $sentenceSize;
	}

	// اضافه کردن آخرین تکه اگر خالی نیست
	if (count($currentChunk) > 0) {
		$chunks[] = implode(' ', $currentChunk);
	}

	return $chunks;
}

// مثال استفاده
$document = "
AvalAI provides access to a wide range of language models through a unified API.
This makes it easy to experiment with different models and choose the best one for your use case.
The platform supports models from various providers including OpenAI, Anthropic, Google, and more.
Each model has different capabilities and pricing, so it's important to understand the tradeoffs.
AvalAI also provides tools for monitoring usage, managing costs, and ensuring compliance with usage policies.
";

$chunks = chunkDocumentBySentences($document, 100, 1);
foreach ($chunks as $index => $chunk) {
	echo "تکه " . ($index + 1) . ": " . $chunk . "\n";
}
?>
```

### بهترین شیوه‌ها
```php
<?php
// تولید امبدینگ با استفاده از AvalAI API

$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/embeddings';

function createEmbedding($text, $apiKey, $apiUrl) {
	// هم متن تکی و هم آرایه‌ای از متون را مدیریت می‌کند
	$input = is_array($text) ? $text : $text; // در اینجا باید $text باشد نه [$text] برای حالت تکی

	$data = [
	'model' => 'text-embedding-3-large',
	'input' => $input
	];

	$jsonData = json_encode($data);

	$ch = curl_init($apiUrl);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_POST, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
	curl_setopt($ch, CURLOPT_HTTPHEADER, [
	'Content-Type: application/json',
	'Authorization: Bearer ' . $apiKey,
	'Content-Length: ' . strlen($jsonData)
	]);

	$response = curl_exec($ch);
	$err = curl_error($ch);
	curl_close($ch);

	if ($err) {
	throw new Exception("خطای cURL: " . $err);
	}

	$responseData = json_decode($response, true);

	if (isset($responseData['error'])) {
		throw new Exception("API Error: " . $responseData['error']['message']);
	}

	// بازگرداندن امبدینگ(ها)
	// اگر ورودی یک آرایه بود، یک آرایه از امبدینگ‌ها را برمی‌گرداند
	// در غیر این صورت، یک امبدینگ تکی را برمی‌گرداند
	if (is_array($input)) {
	    return array_map(function($item) { return $item['embedding']; }, $responseData['data']);
	} else {
	    return $responseData['data'][0]['embedding'];
	}
}

// محاسبه شباهت کسینوسی بین دو بردار
function cosineSimilarity($a, $b) {
	$dotProduct = 0;
	$normA = 0;
	$normB = 0;

	for ($i = 0; $i < count($a); $i++) {
		$dotProduct += $a[$i] * $b[$i];
		$normA += $a[$i] * $a[$i];
		$normB += $b[$i] * $b[$i];
	}

	if ($normA == 0 || $normB == 0) {
	    return 0.0; // برای جلوگیری از تقسیم بر صفر
	}

	return $dotProduct / (sqrt($normA) * sqrt($normB));
}

// مثال استفاده
try {
	// تکه‌های نمونه
	$chunks = [
	"AvalAI provides access to a wide range of language models through a unified API.",
	"The platform supports models from various providers including OpenAI, Anthropic, Google, and more.",
	"Each model has different capabilities and pricing, so it's important to understand the tradeoffs."
	];

	// ایجاد امبدینگ برای هر تکه (درخواست دسته‌ای)
	$chunkEmbeddings = createEmbedding($chunks, $apiKey, $apiUrl);
	echo "تولید شد " . count($chunkEmbeddings) . " امبدینگ با ابعاد " . (count($chunkEmbeddings) > 0 ? count($chunkEmbeddings[0]) : 0) . "\n";
```


## بینایی (ورودی تصویر)
_source: source-archive/بینایی-ورودی-تصویر-392b6b.md_

### استفاده از API تکمیل گفتگو
```php
<?php
// مثال PHP با استفاده از تکمیل گفتگو با URL تصویر
require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$client = OpenAI::client($apiKey, [
  'base_url' => 'https://api.avalai.ir/v1',
]);

$response = $client->chat()->create([
  'model' => 'gpt-5.6-luna',
  'messages' => [
    [
      'role' => 'user',
      'content' => [
        [
          'type' => 'text',
          'text' => 'در این تصویر چه چیزی وجود دارد؟'
        ],
        [
          'type' => 'image_url',
          'image_url' => [
            'url' => 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg',
            // 'detail' => 'high' // اختیاری: تعیین سطح جزئیات
          ]
        ]
      ]
    ]
  ]
]);

echo $response->choices[0]->message->content;
?>
```

### استفاده از API پاسخ‌ها
```php
// مثال PHP با استفاده از AvalAI با URL تصویر
<?php
require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$client = OpenAI::client($apiKey, [
'base_url' => 'https://api.avalai.ir/v1',
]);

$response = $client->responses()->create([
'model' => 'gpt-5.6-luna',
'input' => [
[
'role' => 'user',
'content' => [
[
'type' => 'input_text',
'text' => 'در این تصویر چه چیزی وجود دارد؟'
],
[
'type' => 'input_image',
'image_url' => 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg',
// 'detail' => 'high' // اختیاری: تعیین سطح جزئیات
]
]
]
]
]);

// استخراج متن از پاسخ
$textOutput = '';
if (isset($response->output_text)) {
  $textOutput = $response->output_text;
} else {
  // تجزیه دستی اگر output_text در دسترس نباشد
  foreach ($response->output as $item) {
    if ($item->type === 'message' && isset($item->content)) {
      foreach ($item->content as $contentPart) {
        if ($contentPart->type === 'output_text') {
          $textOutput .= $contentPart->text . "\n";
        }
      }
    }
  }
}

echo trim($textOutput);
?>
```


## تولید متن و پرامپت‌نویسی
_source: source-archive/تولید-متن-و-پرامپت-نویسی-88e099.md_

### تولید متن پایه
```php
<?php

$apiKey = getenv('AVALAI_API_KEY');

$payload = [
    'model' => 'gpt-5.6-luna',
    'instructions' => 'You are a helpful assistant.',
    'input' => 'یک داستان یک جمله‌ای قبل از خواب درباره یک تک‌شاخ بنویس.',
];

$ch = curl_init('https://api.avalai.ir/v1/responses');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . $apiKey,
        'Content-Type: application/json',
    ],
    CURLOPT_POSTFIELDS => json_encode($payload),
]);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

### نقش‌های پیام و دستورالعمل‌ها
```php
// مثال استفاده از پارامتر instructions با AvalAI
$apiKey = getenv('AVALAI_API_KEY');

$client = OpenAI::client($apiKey, [
'base_url' => 'https://api.avalai.ir/v1',
]);

$response = $client->responses()->create([
'model' => 'gpt-5.6-luna',
'instructions' => 'مثل دزدان دریایی صحبت کن.',
'input' => 'آیا نقطه‌ویرگول در جاوااسکریپت اختیاری است؟'
]);

// استخراج متن از پاسخ همانطور که قبلا نشان داده شد
```

### نقش‌های پیام و دستورالعمل‌ها
```php
// مثال استفاده از نقش‌های developer و user با AvalAI
$apiKey = getenv('AVALAI_API_KEY');

$client = OpenAI::client($apiKey, [
'base_url' => 'https://api.avalai.ir/v1',
]);

$response = $client->responses()->create([
'model' => 'gpt-5.6-luna',
'input' => [
[
'role' => 'developer',
'content' => 'مثل دزدان دریایی صحبت کن.'
],
[
'role' => 'user',
'content' => 'آیا نقطه‌ویرگول در جاوااسکریپت اختیاری است؟'
]
]
]);

// استخراج متن از پاسخ همانطور که قبلا نشان داده شد
```


## راهنمای شروع سریع
_source: source-archive/راهنمای-شروع-سریع-bbc716.md_

### Responses API (پیشنهادی برای برنامه‌های جدید)
```php
<?php
$apiKey = getenv('AVALAI_API_KEY');
$payload = [
    'model' => 'gpt-5.6-luna',
    'instructions' => 'You are a helpful assistant.',
    'input' => 'سلام، دنیا!',
];

$ch = curl_init('https://api.avalai.ir/v1/responses');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . $apiKey,
        'Content-Type: application/json',
    ],
    CURLOPT_POSTFIELDS => json_encode($payload),
]);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
```


## راهنمای نظارت (Moderation)
_source: source-archive/راهنمای-نظارت-Moderation-0c65ae.md_

### نظارت ورودی‌های متنی
```php
<?php
// مثال PHP با استفاده از API نظارت AvalAI
require_once 'vendor/autoload.php';

// استفاده از کتابخانه کلاینت PHP OpenAI
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

try {
  // ایجاد درخواست نظارت
  $response = $client->moderations()->create([
  'model' => 'omni-moderation-latest',
  'input' => 'متن نمونه‌ای که ممکن است خط‌مشی محتوا را نقض کند.'
  ]);

  // نمایش پاسخ
  print_r($response->toArray());
} catch (\Exception $e) {
  echo "خطا: " . $e->getMessage() . "\n";
}
```

### نظارت ورودی‌های تصویر و متن (چندوجهی)
```php
<?php
// مثال PHP با استفاده از نظارت چندوجهی AvalAI
require_once 'vendor/autoload.php';

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

try {
  $response = $client->moderations()->create([
  'model' => 'omni-moderation-latest',
  'input' => [
  [
  'type' => 'text',
  'text' => 'توضیحات همراه تصویر.'
  ],
  [
  'type' => 'image_url',
  'image_url' => [
  'url' => 'https://example.com/image_to_moderate.png'
  // یا Base64: 'url' => 'data:image/png;base64,abcdefg...'
  ]
  ]
  ]
  ]);

  print_r($response->toArray());
} catch (\Exception $e) {
  echo "خطا: " . $e->getMessage() . "\n";
}
```


## راهنمای ورودی‌های فایل
_source: source-archive/راهنمای-ورودی-های-فایل-f8fbdf.md_

### تصویر URL در Chat Completions
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$response = $client->chat()->create([
    'model' => 'gpt-5.6-luna',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'در این تصویر چیست؟'],
                [
                    'type' => 'image_url',
                    'image_url' => ['url' => 'https://example.com/sample-image.jpg']
                ]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;
```

### URL PDF در Chat Completions
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$fileUrl = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf';

$response = $client->chat()->create([
    'model' => 'claude-sonnet-4-6',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این سند درباره چیست؟'],
                ['type' => 'file', 'file' => ['file_id' => $fileUrl]]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;
```

### URL سند در OCR API
```php
<?php

$apiKey = getenv('AVALAI_API_KEY');

$data = [
    'model' => 'mistral-ocr-latest',
    'document' => [
        'type' => 'document_url',
        'document_url' => 'https://arxiv.org/pdf/1805.04770'
    ],
    'include_image_base64' => true
];

$ch = curl_init('https://api.avalai.ir/v1/ocr');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
```

### تصویر با Base64 در Chat Completions
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// خواندن و کدگذاری تصویر
$imageData = file_get_contents('image.jpg');
$base64Image = base64_encode($imageData);

$response = $client->chat()->create([
    'model' => 'gpt-5.6-luna',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'در این تصویر چیست؟'],
                [
                    'type' => 'image_url',
                    'image_url' => ['url' => 'data:image/jpeg;base64,' . $base64Image]
                ]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;
```

### PDF با Base64 در Chat Completions
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// خواندن و کدگذاری PDF
$pdfData = file_get_contents('document.pdf');
$base64Pdf = base64_encode($pdfData);

$response = $client->chat()->create([
    'model' => 'gemini-2.5-flash',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این سند را خلاصه کنید'],
                [
                    'type' => 'file',
                    'file' => ['file_data' => 'data:application/pdf;base64,' . $base64Pdf]
                ]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;
```

### صوت با Base64 در Chat Completions
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// خواندن و کدگذاری صوت
$audioData = file_get_contents('audio.mp3');
$base64Audio = base64_encode($audioData);

$response = $client->chat()->create([
    'model' => 'gemini-2.5-flash',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این صوت را رونویسی کنید'],
                [
                    'type' => 'file',
                    'file' => ['file_data' => 'data:audio/mp3;base64,' . $base64Audio]
                ]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;
```

### اکسل با Base64 در Chat Completions
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// خواندن و کدگذاری فایل اکسل
$excelData = file_get_contents('spreadsheet.xlsx');
$base64Excel = base64_encode($excelData);
$mimeType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet';

$response = $client->chat()->create([
    'model' => 'gpt-5.6-luna',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این صفحه گسترده را تحلیل کنید و نکات کلیدی را ارائه دهید'],
                [
                    'type' => 'file',
                    'file' => ['file_data' => 'data:' . $mimeType . ';base64,' . $base64Excel]
                ]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;
```

### آپلود فایل
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

// آپلود فایل
$file = $client->files()->create([
    'purpose' => 'user_data',
    'file' => fopen('document.pdf', 'r'),
]);

echo "فایل با شناسه آپلود شد: " . $file->id . "\n";
```

### استفاده از شناسه فایل در Chat Completions
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

// با فرض اینکه فایل قبلا آپلود شده است
$fileId = 'file-abc123xyz';

$response = $client->chat()->create([
    'model' => 'gpt-5.6-luna',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این سند را خلاصه کنید'],
                ['type' => 'file', 'file' => ['file_id' => $fileId]]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;
```

### استفاده از شناسه فایل در Responses API
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$fileId = 'file-abc123xyz';

$response = $client->responses()->create([
    'model' => 'gpt-5.6-luna',
    'input' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'input_file', 'file_id' => $fileId],
                ['type' => 'input_text', 'text' => 'اولین موضوع در این سند چیست؟']
            ]
        ]
    ]
]);

echo $response->outputText;
```


## سطوح سرویس
_source: source-archive/سطوح-سرویس-332848.md_

### استفاده از سطح Default
```php
<?php
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

$data = [
    'model' => 'gpt-5.4',
    'messages' => [
        ['role' => 'user', 'content' => 'سلام!']
    ],
    'service_tier' => 'default'  // اختیاری، این پیش‌فرض است
];

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);
echo $result['choices'][0]['message']['content'];
?>
```

### استفاده از سطح Flex
```php
<?php
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

// استفاده از سطح flex برای صرفه‌جویی در هزینه کارهای غیرحساس به زمان
$data = [
    'model' => 'gpt-5-mini',
    'messages' => [
        ['role' => 'user', 'content' => 'این سند را خلاصه کن...']
    ],
    'service_tier' => 'flex'
];

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);
echo $result['choices'][0]['message']['content'] . "\n";
echo "سطح سرویس استفاده شده: " . $result['service_tier'] . "\n";
?>
```


## فراخوانی تابع
_source: source-archive/فراخوانی-تابع-1e4858.md_

### مثال: دریافت وضعیت آب و هوا
```php
<?php
require 'vendor/autoload.php'; // اطمینان حاصل کنید که کلاینت PHP OpenAI نصب شده است

$apiKey = getenv('AVALAI_API_KEY');
$baseURL = 'https://api.avalai.ir/v1'; // از URL پایه AvalAI استفاده کنید

$client = OpenAI::client($apiKey);
// توجه: تنظیم URL پایه ممکن است به نسخه خاص کتابخانه کلاینت PHP بستگی داشته باشد.
// مستندات کتابخانه خود را بررسی کنید. برخی ممکن است از یک فکتوری یا شی پیکربندی استفاده کنند.
// مثال با استفاده از پیکربندی factory-style:
// $client = OpenAI::factory()
// ->withApiKey($apiKey)
// ->withBaseUri($baseURL)
// ->make();


$tools = [
 [
 'type' => 'function',
 'function' => [
 'name' => 'get_current_weather',
 'description' => 'دریافت وضعیت آب و هوای فعلی در یک مکان مشخص',
 'parameters' => [
 'type' => 'object',
 'properties' => [
 'location' => [
 'type' => 'string',
 'description' => 'شهر و استان، به عنوان مثال San Francisco, CA',
 ],
 'unit' => [
 'type' => ['string', 'null'],
 'enum' => ['celsius', 'fahrenheit', null],
 ],
 ],
 'required' => ['location', 'unit'],
 'additionalProperties' => false,
 ],
 'strict' => true,
 ],
 ]
];

$messages = [['role' => 'user', 'content' => "هوای بوستون چطور است؟"]]; // پیام کاربر به فارسی

try {
 $response = $client->chat()->create([
 'model' => 'gpt-5.6-luna', // از مدلی استفاده کنید که از فراخوانی تابع از طریق AvalAI پشتیبانی می‌کند
 'messages' => $messages,
 'tools' => $tools,
 'tool_choice' => 'auto', // پیش‌فرض: اجازه دهید مدل تصمیم بگیرد
 ]);

 $responseMessage = $response->choices[0]->message;
 $toolCalls = $responseMessage->toolCalls ?? null; // برای ایمنی از null coalescing استفاده کنید

 // منطق مرحله ۳ در ادامه می‌آید...
 if ($toolCalls) {
 echo "مدل می‌خواهد توابع زیر را فراخوانی کند:\n";
 print_r($toolCalls); // یا در آن‌ها حلقه بزنید
 // $responseMessage و $toolCalls را برای مرحله ۳ و ۴ ذخیره کنید
 } else {
 echo "مدل درخواست فراخوانی تابع نداد.\n";
 echo $responseMessage->content;
 }

} catch (Exception $e) {
 echo "یک خطای API رخ داد: " . $e->getMessage() . "\n";
}
```

### مثال: دریافت وضعیت آب و هوا
```php
<?php
// فرض کنید $messages حاوی تاریخچه تا پیام tool_calls دستیار است
// فرض کنید $resultsForNextCall حاوی آرایه پیام‌های نتیجه ابزار از مرحله ۳ است

if (!empty($resultsForNextCall)) {
 // نتایج ابزار را به تاریخچه پیام اضافه کنید
 $updatedMessages = array_merge($messages, $resultsForNextCall);

 echo "\nدر حال ارسال نتایج به مدل...\n";
 try {
 $secondResponse = $client->chat()->create([
 'model' => 'gpt-5.6-luna',
 'messages' => $updatedMessages,
 // در اینجا نیازی به ابزار نیست مگر اینکه بخواهید فراخوانی‌های بعدی انجام شود
 ]);

 // مرحله ۵: دریافت پاسخ نهایی
 $finalResponse = $secondResponse->choices[0]->message->content;
 echo "\nپاسخ نهایی مدل:\n";
 echo $finalResponse . "\n";

 } catch (Exception $e) {
 echo "یک خطای API در فراخوانی دوم رخ داد: " . $e->getMessage() . "\n";
 }
}
```


## محدودیت نرخ API AvalAI و سطوح حساب
_source: source-archive/محدودیت-نرخ-API-AvalAI-و-سطوح-حساب-32e26c.md_

### مثال پایتون
```php
<?php
require 'vendor/autoload.php';

/**
* تابع ارسال درخواست با عقب‌نشینی نمایی برای خطاهای محدودیت نرخ
*/
function makeRequestWithBackoff($func, $maxRetries = 5, $initialDelay = 1, $maxDelay = 60) {
  $numRetries = 0;
  $delay = $initialDelay;

  while (true) {
    try {
      return $func();
    } catch (\Exception $e) {
      // بررسی آیا خطای محدودیت نرخ است
      $isRateLimitError = false;
      $retryAfter = 0;

      if (method_exists($e, 'getResponse')) {
        $response = $e->getResponse();
        if ($response && $response->getStatusCode() === 429) {
          $isRateLimitError = true;
          $headers = $response->getHeaders();
          if (isset($headers['Retry-After'][0])) {
            $retryAfter = (int)$headers['Retry-After'][0];
          }
        }
      }

      // اگر خطای محدودیت نرخ نیست یا به حداکثر تلاش‌ها رسیده‌ایم
      if (!$isRateLimitError || $numRetries >= $maxRetries) {
        throw $e;
      }

      // تنظیم تاخیر بر اساس هدر retry-after
      if ($retryAfter > 0) {
        $delay = max($retryAfter, $delay);
      }

      // عقب‌نشینی نمایی با لرزش (jitter)
      $jitter = mt_rand() / mt_getrandmax() * 0.5 * $delay;
      $sleepTime = $delay + $jitter;

      echo "محدودیت نرخ فراتر رفت. تلاش مجدد در {$sleepTime} ثانیه...\n";
      sleep($sleepTime);

      $numRetries++;
      $delay = min($delay * 2, $maxDelay);
    }
  }
}

// تنظیم کلاینت
$apiKey = getenv('AVALAI_API_KEY');
$client = OpenAI::client($apiKey, [
'base_url' => 'https://api.avalai.ir/v1',
]);

// تعریف تابع ارسال درخواست
$getCompletion = function() use ($client) {
  return $client->chat()->create([
  'model' => 'gpt-5.6-luna',
  'messages' => [
  ['role' => 'user', 'content' => 'سلام!'],
  ],
  ]);
};

// استفاده از تابع با منطق تلاش مجدد
try {
  $response = makeRequestWithBackoff($getCompletion);
  echo $response->choices[0]->message->content . "\n";
} catch (\Exception $e) {
  echo "خطا پس از چندین تلاش: " . $e->getMessage() . "\n";
}
?>
```


## مدل‌های DeepSeek
_source: source-archive/مدل-های-DeepSeek-a969e9.md_

### جزئیات API حالت تفکری
```php
<?php
require 'vendor/autoload.php';

use OpenAI;

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$response = $client->chat()->create([
    'model' => 'deepseek-reasoner',
    'messages' => [
        ['role' => 'user', 'content' => '۹.۱۱ و ۹.۸، کدام بزرگتر است؟']
    ]
]);

// دسترسی به فرآیند استدلال
$reasoningContent = $response->choices[0]->message->reasoning_content ?? null;
// دسترسی به پاسخ نهایی
$content = $response->choices[0]->message->content;

echo "استدلال: " . $reasoningContent . "\n";
echo "پاسخ: " . $content . "\n";
```

### مکالمات چند نوبتی
```php
<?php
require 'vendor/autoload.php';

use OpenAI;

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

// نوبت ۱
$messages = [['role' => 'user', 'content' => '۱۵ + ۲۷ چند می‌شود؟']];
$response = $client->chat()->create([
    'model' => 'deepseek-reasoner',
    'messages' => $messages
]);

$reasoningContent = $response->choices[0]->message->reasoning_content ?? null;
$content = $response->choices[0]->message->content;

// نوبت ۲ - فقط content را ارسال کنید، نه reasoning_content
$messages[] = ['role' => 'assistant', 'content' => $content];
$messages[] = ['role' => 'user', 'content' => 'حالا آن را در ۲ ضرب کن.'];

$response = $client->chat()->create([
    'model' => 'deepseek-reasoner',
    'messages' => $messages
]);

echo $response->choices[0]->message->content . "\n";
```

### تفکر در استفاده از ابزار
```php
<?php
require 'vendor/autoload.php';

use OpenAI;

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$tools = [
    [
        'type' => 'function',
        'function' => [
            'name' => 'get_weather',
            'description' => 'دریافت آب و هوای یک مکان',
            'parameters' => [
                'type' => 'object',
                'properties' => [
                    'location' => ['type' => 'string', 'description' => 'نام شهر']
                ],
                'required' => ['location']
            ]
        ]
    ]
];

$messages = [['role' => 'user', 'content' => 'آب و هوای تهران امروز چطور است؟']];

while (true) {
    $response = $client->chat()->create([
        'model' => 'deepseek-reasoner',
        'messages' => $messages,
        'tools' => $tools
    ]);
    
    $message = $response->choices[0]->message;
    $reasoningContent = $message->reasoning_content ?? null;
    $content = $message->content;
    $toolCalls = $message->tool_calls ?? null;
    
    // اگر فراخوانی ابزار نداشتیم، پاسخ نهایی را داریم
    if (!$toolCalls) {
        echo "پاسخ نهایی: " . $content . "\n";
        break;
    }
    
    // بحرانی: reasoning_content را هنگام اضافه کردن پیام دستیار درج کنید
    $assistantMessage = [
        'role' => 'assistant',
        'content' => $content ?? '',
        'tool_calls' => array_map(function($tc) {
            return [
                'id' => $tc->id,
                'type' => 'function',
                'function' => [
                    'name' => $tc->function->name,
                    'arguments' => $tc->function->arguments
                ]
            ];
        }, $toolCalls)
    ];
    
    // باید reasoning_content را اگر موجود بود درج کنید
    if ($reasoningContent) {
        $assistantMessage['reasoning_content'] = $reasoningContent;
    }
    
    $messages[] = $assistantMessage;
    
    // پردازش فراخوانی‌های ابزار و اضافه کردن نتایج
    foreach ($toolCalls as $tc) {
        // پیاده‌سازی ابزار شما در اینجا
        $toolResult = "آفتابی، ۱۵-۲۲ درجه سانتیگراد";  // نتیجه نمونه
        $messages[] = [
            'role' => 'tool',
            'tool_call_id' => $tc->id,
            'content' => $toolResult
        ];
    }
}
```


## مدل‌های استدلالی
_source: source-archive/مدل-های-استدلالی-21a4c4.md_

### جریان‌های طولانی ابزارمحور و `phase`
```php
<?php
$apiKey = getenv('AVALAI_API_KEY');
$prompt = <<<PROMPT
یک اسکریپت bash بنویسید که یک ماتریس را به صورت رشته با فرمت
'[1,2],[3,4],[5,6]' دریافت کرده و ترانهاده آن را با همان فرمت چاپ کند.
PROMPT;

$payload = [
    'model' => 'gpt-5.6-luna',
    'reasoning' => ['effort' => 'medium'],
    'input' => [
        ['role' => 'user', 'content' => $prompt],
    ],
];

$ch = curl_init('https://api.avalai.ir/v1/responses');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . $apiKey,
        'Content-Type: application/json',
    ],
    CURLOPT_POSTFIELDS => json_encode($payload),
]);

$response = curl_exec($ch);
curl_close($ch);

echo $response;

?>
```

### تخصیص فضا برای استدلال
```php
<?php
require 'vendor/autoload.php';

// ... (راه‌اندازی کلاینت مانند قبل) ...

$prompt = "..."; // پرامپت شما در اینجا
$maxTokens = 300; // تعریف max_tokens

try {
 $response = $client->chat()->create([
 'model' => 'gpt-5.6-luna',
 'messages' => [
 ['role' => 'user', 'content' => $prompt],
 ],
 'max_tokens' => $maxTokens, // محدود کردن کل توکن‌های تولید شده
 // در صورت لزوم، پارامترهای استدلال را اضافه کنید
 ]);

 $finishReason = $response->choices[0]->finishReason;
 // اطمینان حاصل کنید که محتوا قبل از دسترسی وجود دارد
 $outputText = $response->choices[0]->message->content ?? null;

 if ($finishReason === 'length') { // بررسی دلیل پایان length
 echo "توکن‌ها تمام شد (به max_tokens رسید).\n";
 if ($outputText) {
 echo "خروجی جزئی: " . $outputText . "\n";
 } else {
 echo "توکن‌ها در مرحله استدلال تمام شد.\n";
 }
 } elseif ($finishReason === 'stop') {
 echo "با موفقیت تکمیل شد:\n";
 echo $outputText . "\n";
 } else {
 echo "Finished with reason: " . $finishReason . "\n";
 if ($outputText) {
 echo "Output: " . $outputText . "\n";
 }
 }

} catch (Exception $e) {
 echo "یک خطای API رخ داد: " . $e->getMessage() . "\n";
}
?>
```

### مثال‌های پرامپت
```php
// --- کد فراخوانی (PHP) ---
<?php
require 'vendor/autoload.php';

use OpenAI\Client;

$apiKey = getenv('AVALAI_API_KEY');
$baseURL = 'https://api.avalai.ir/v1';

// پیکربندی کلاینت (مثال)
$client = OpenAI::client($apiKey);
// تنظیم base URL در صورت نیاز از طریق factory/config

// توجه به تغییر: به جای بک‌تیک سه‌گانه در رشته پرامپت،
// از تورفتگی برای مثال کد داخلی استفاده کنید.
$prompt = trim(<<<PROMPT
دستورالعمل‌ها:
- با توجه به کامپوننت React زیر، آن را طوری تغییر دهید که کتاب‌های غیرداستانی متن قرمز داشته باشند.
- فقط کد بازسازی شده React را در پاسخ خود برگردانید.
- توضیحات یا بلوک‌های کد مارک‌داون را شامل نکنید.
- از چهار فاصله برای تورفتگی استفاده کنید.
- طول خطوط را زیر ۸۰ ستون نگه دارید.

کد اصلی:

 const books = [
 { title: 'تل‌ماسه', category: 'fiction', id: 1 }, // داستانی
 { title: 'فرانکنشتاین', category: 'fiction', id: 2 }, // داستانی
 { title: 'مانی‌بال', category: 'nonfiction', id: 3 }, // غیرداستانی
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

PROMPT);


try {
 $response = $client->chat()->create([
 'model' => 'gpt-5.6-luna', // از یک مدل استدلالی مناسب از AvalAI استفاده کنید
 'messages' => [
 ['role' => 'user', 'content' => $prompt],
 ],
 'temperature' => 0.1,
 ]);

 echo $response->choices[0]->message->content;

} catch (Exception $e) {
 echo "خطای API: " . $e->getMessage() . "\n";
}
?>
```

### مثال‌های پرامپت
```php
// --- کد فراخوانی (PHP) ---
<?php
require 'vendor/autoload.php';

use OpenAI\Client;

$apiKey = getenv('AVALAI_API_KEY');
$baseURL = 'https://api.avalai.ir/v1';

// پیکربندی کلاینت (مثال)
$client = OpenAI::client($apiKey);
// تنظیم base URL در صورت نیاز از طریق factory/config

$prompt = trim(<<<PROMPT
می‌خواهم یک برنامه پایتون بسازم که سوالات کاربر را دریافت کرده و آنها را
در یک ذخیره‌ساز ساده کلید-مقدار (مانند دیکشنری یا فایل JSON) که در آن
به پاسخ‌ها نگاشت شده‌اند، جستجو کند. اگر یک تطابق نزدیک (بررسی بدون حساسیت به حروف بزرگ و کوچک) وجود داشته باشد،
پاسخ مطابق را بازیابی می‌کند. اگر وجود نداشته باشد، از کاربر می‌خواهد
پاسخی ارائه دهد و جفت سوال/پاسخ جدید را ذخیره می‌کند.

1. طرحی برای ساختار دایرکتوری (مثلا اسکریپت اصلی، فایل داده) ارائه دهید.
2. کد کامل پایتون برای اسکریپت اصلی را برگردانید.
3. یک ساختار JSON نمونه برای فایل داده برگردانید.
4. متن توضیحی را فقط در ابتدا و انتهای خروجی ارائه دهید، نه به صورت ترکیبی در کد یا خروجی ساختار فایل.
PROMPT);

try {
 $response = $client->chat()->create([
 'model' => 'deepseek-v4.1-flash', // از شناسه صریح V4.1 Flash استفاده کنید
 'messages' => [
 ['role' => 'user', 'content' => $prompt],
 ],
 ]);

 echo $response->choices[0]->message->content;

} catch (Exception $e) {
 echo "خطای API: " . $e->getMessage() . "\n";
}
?>
```

### مثال‌های پرامپت
```php
// --- کد فراخوانی (PHP) ---
<?php
require 'vendor/autoload.php';

use OpenAI\Client;

$apiKey = getenv('AVALAI_API_KEY');
$baseURL = 'https://api.avalai.ir/v1';

// پیکربندی کلاینت (مثال)
$client = OpenAI::client($apiKey);
// تنظیم base URL در صورت نیاز از طریق factory/config

$prompt = trim(<<<PROMPT
سه ترکیب یا کلاس ترکیبی که باید برای پیشبرد تحقیقات در مورد
آنتی‌بیوتیک‌های جدید، به ویژه علیه باکتری‌های مقاوم، بیشتر بررسی کنیم، کدامند؟
به طور خلاصه توضیح دهید که چرا هر کدام امیدوارکننده است.
PROMPT);

try {
 $response = $client->chat()->create([
 'model' => 'gemini-3.1-pro-preview', // از یک مدل استدلالی مناسب از AvalAI استفاده کنید
 'messages' => [
 ['role' => 'user', 'content' => $prompt],
 ],
 ]);

 echo $response->choices[0]->message->content;

} catch (Exception $e) {
 echo "خطای API: " . $e->getMessage() . "\n";
}
?>
```


## مدیریت خطا در API AvalAI
_source: source-archive/مدیریت-خطا-در-API-AvalAI-711dc1.md_

### مثال ها
```php
<?php
require 'vendor/autoload.php';

/**
* تابع ارسال درخواست API با منطق تلاش مجدد عقب‌نشینی نمایی
*/
function makeApiRequestWithRetry($func, $maxRetries = 5, $initialDelay = 1, $maxDelay = 60) {
  $numRetries = 0;
  $delay = $initialDelay;

  while (true) {
    try {
      return $func();
    } catch (\Exception $e) {
      // بررسی خطای محدودیت نرخ
      $isRateLimitError = false;
      $retryAfter = 0;

      if (method_exists($e, 'getResponse')) {
        $response = $e->getResponse();
        if ($response && $response->getStatusCode() === 429) {
          $isRateLimitError = true;
          $headers = $response->getHeaders();
          if (isset($headers['Retry-After'][0])) {
            $retryAfter = (int)$headers['Retry-After'][0];
          }
        }
      }

      // برای خطاهای کلاینت غیر از محدودیت نرخ تلاش مجدد نکنید
      $statusCode = method_exists($e, 'getCode') ? $e->getCode() : 0;
      if (!$isRateLimitError && ($statusCode < 500 || $statusCode === 0)) {
        throw $e;
      }

      if ($numRetries >= $maxRetries) {
        throw $e;
      }

      // تنظیم تاخیر بر اساس هدر retry-after
      if ($retryAfter > 0) {
        $delay = max($retryAfter, $delay);
      }

      // عقب‌نشینی نمایی با لرزش (jitter)
      $jitter = mt_rand() / mt_getrandmax() * 0.5 * $delay;
      $sleepTime = $delay + $jitter;

      error_log("تلاش مجدد در {$sleepTime} ثانیه...");
      sleep($sleepTime);

      $numRetries++;
      $delay = min($delay * 2, $maxDelay);
    }
  }
}

// تنظیم کلاینت
$apiKey = getenv('AVALAI_API_KEY');
$client = OpenAI::client($apiKey, [
'base_url' => 'https://api.avalai.ir/v1',
]);

// تعریف تابع ارسال درخواست
$getChatCompletion = function() use ($client) {
  return $client->chat()->create([
  'model' => 'gpt-5.6-luna',
  'messages' => [
  ['role' => 'user', 'content' => 'سلام!'],
  ],
  ]);
};

// استفاده از تابع با منطق تلاش مجدد
try {
  $response = makeApiRequestWithRetry($getChatCompletion);
  echo $response->choices[0]->message->content;
} catch (\Exception $e) {
  echo "خطا پس از چندین تلاش: " . $e->getMessage();
}
?>
```


## مرجع API بردارهای تعبیه‌سازی (Embeddings)
_source: source-archive/مرجع-API-بردارهای-تعبیه-سازی-Embeddings-6efa96.md_

### تولید تعبیه‌سازی پایه
```php
<?php
// مثال PHP برای Embeddings از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/embeddings';

$data = [
'model' => 'text-embedding-3-small',
'input' => 'The food was delicious and the service was excellent.' // متن ورودی به انگلیسی باقی می‌ماند یا ترجمه می‌شود؟
// در صورت نیاز پارامترهای دیگری مانند encoding_format، dimensions و غیره را اضافه کنید
// 'encoding_format' => 'float',
// 'dimensions' => 1024
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json',
'Authorization: Bearer ' . $apiKey,
'Content-Length: ' . strlen($jsonData)
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #:" . $err;
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo $response;
} else {
  $responseData = json_decode($response, true);
  if (isset($responseData['data'][0]['embedding'])) {
    $embedding = $responseData['data'][0]['embedding'];
    echo "طول بردار تعبیه‌سازی: " . count($embedding) . "\n";
    echo "چند مقدار اول: [" . implode(', ', array_slice($embedding, 0, 5)) . "]\n";
  } else {
    echo "پاسخ دریافت شد:\n";
    print_r($responseData);
  }
}
?>
```


## مرجع API تشخیص متن (OCR)
_source: source-archive/مرجع-API-تشخیص-متن-OCR-61bff2.md_

### درخواست ساده OCR
```php
<?php

$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

$data = [
    'model' => 'mistral-ocr-4-0',
    'document' => [
        'type' => 'document_url',
        'document_url' => 'https://arxiv.org/pdf/2201.04234'
    ]
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey,
    'Content-Length: ' . strlen($jsonData)
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);
curl_close($ch);

if ($err) {
    echo "cURL Error: " . $err;
} elseif ($httpcode >= 400) {
    echo "HTTP Error: " . $httpcode . "\n";
    echo $response;
} else {
    $responseData = json_decode($response, true);
    foreach ($responseData['pages'] as $page) {
        echo "Page " . $page['index'] . ": " . substr($page['markdown'], 0, 100) . "...\n";
    }
}
?>
```


## مرجع API رتبه‌بندی مجدد (Rerank)
_source: source-archive/مرجع-API-رتبه-بندی-مجدد-Rerank-83aa7f.md_

### رتبه‌بندی مجدد پایه
```php
<?php
// مثال PHP برای Rerank از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/rerank';

$data = [
 'model' => 'cohere.rerank-v3-5:0',
 'query' => 'مزایای انرژی‌های تجدیدپذیر چیست؟',
 'documents' => [
 'منابع انرژی تجدیدپذیر مانند خورشید و باد برای مقابله با تغییرات آب و هوایی بسیار مهم هستند.',
 'سوخت‌های فسیلی سنتی اثرات زیست‌محیطی قابل توجهی دارند.',
 'سرمایه‌گذاری در فناوری سبز می‌تواند منجر به رشد اقتصادی و ایجاد شغل شود.',
 'پنل‌های خورشیدی نور خورشید را به برق تبدیل می‌کنند.'
 ]
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey,
 'Content-Length: ' . strlen($jsonData)
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
 echo "خطای cURL #:" . $err;
} elseif ($httpcode >= 400) {
 echo "خطای HTTP: " . $httpcode . "\n";
 echo $response;
} else {
 $responseData = json_decode($response, true);
 if (isset($responseData['results'])) {
 foreach ($responseData['results'] as $result) {
 echo "ایندکس: " . $result['index'] .
 "، امتیاز ارتباط: " . $result['relevance_score'] .
 "، سند: " . $result['document']['text'] . "\n";
 }
 } else {
 echo "پاسخ دریافت شد:\n";
 print_r($responseData);
 }
}
?>
```


## مرجع API فایل‌ها (Files)
_source: source-archive/مرجع-API-فایل-ها-Files-44ecdd.md_

### مثال‌ها
```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/files';

$file = new CURLFile('document.pdf', 'application/pdf', 'document.pdf');

$data = [
    'file' => $file,
    'purpose' => 'user_data'
];

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($httpcode >= 400) {
    echo "خطا: " . $httpcode . "\n";
    echo $response;
} else {
    $fileData = json_decode($response, true);
    echo "فایل آپلود شد: " . $fileData['id'] . "\n";
}
?>
```

### مثال‌ها
```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/files';

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
]);

$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
foreach ($data['data'] as $file) {
    echo $file['id'] . ": " . $file['filename'] . " (" . $file['bytes'] . " بایت)\n";
}
?>
```

### مثال‌ها
```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$fileId = 'file-abc123';
$apiUrl = "https://api.avalai.ir/v1/files/{$fileId}";

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
]);

$response = curl_exec($ch);
curl_close($ch);

$file = json_decode($response, true);
echo "نام فایل: " . $file['filename'] . "\n";
echo "اندازه: " . $file['bytes'] . " بایت\n";
echo "هدف: " . $file['purpose'] . "\n";
?>
```

### مثال‌ها
```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$fileId = 'file-abc123';
$apiUrl = "https://api.avalai.ir/v1/files/{$fileId}";

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
]);

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);
echo "حذف شد: " . ($result['deleted'] ? 'بله' : 'خیر') . "\n";
?>
```

### مثال‌ها
```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$fileId = 'file-abc123';
$apiUrl = "https://api.avalai.ir/v1/files/{$fileId}/content";

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
]);

$content = curl_exec($ch);
curl_close($ch);

file_put_contents('downloaded_file.pdf', $content);
echo "فایل با موفقیت دانلود شد\n";
?>
```

### مثال: تکمیل گفتگو با فایل
```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

$data = [
    'model' => 'gemini-2.5-flash',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این سند را خلاصه کن'],
                ['type' => 'file', 'file' => ['file_id' => 'file-abc123']],
            ],
        ],
    ],
];

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey,
]);

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);
echo $result['choices'][0]['message']['content'] . "\n";
?>
```


## مرجع API مدل‌ها
_source: source-archive/مرجع-API-مدل-ها-fefc4a.md_

### نمونه درخواست (فرمت OpenAI)
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$models = $client->models()->list();

foreach ($models->data as $model) {
    echo $model->id . " - " . $model->ownedBy . "\n";
}
```

### نمونه درخواست
```php
<?php

$response = file_get_contents("https://api.avalai.ir/public/models");
$models = json_decode($response, true);

foreach ($models["data"] as $model) {
    echo $model["id"] . " - " . $model["owned_by"] . "\n";
}
```

### نمونه درخواست (فرمت OpenAI)
```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$model = $client->models()->retrieve('gpt-5.6-luna');

echo "Model: " . $model->id . "\n";
echo "Owned by: " . $model->ownedBy . "\n";
```


## مرجع API پاسخ‌ها
_source: source-archive/مرجع-API-پاسخ-ها-c0f6f3.md_

### درخواست نمونه (ورودی متنی)
```php
<?php
// مثال PHP برای API پاسخ‌های AvalAI (/v1/responses)

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
if (!$apiKey) {
  die("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.\n");
}

$apiUrl = 'https://api.avalai.ir/v1/responses';

$data = [
'model' => 'gpt-5.6-luna', // مدل مورد نظر را مشخص کنید
'input' => 'یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو.'
// پارامترهای دیگر را در صورت نیاز اضافه کنید، به عنوان مثال:
// 'temperature' => 0.7,
// 'max_output_tokens' => 100,
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json',
'Authorization: Bearer ' . $apiKey, // اطمینان حاصل کنید که این AVALAI_API_KEY شما است
'Content-Length: ' . strlen($jsonData)
]);
// اختیاری: تنظیمات وقفه زمانی را اضافه کنید
// curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
// curl_setopt($ch, CURLOPT_TIMEOUT, 30);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #: " . $err . "\n";
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "بدنه پاسخ: " . $response . "\n";
} else {
  $responseData = json_decode($response, true);
  if (json_last_error() !== JSON_ERROR_NONE) {
    echo "خطا در رمزگشایی پاسخ JSON: " . json_last_error_msg() . "\n";
    echo "پاسخ خام: " . $response . "\n";
  } elseif (isset($responseData['output'][0]['content'][0]['text'])) {
    // دسترسی به متن بر اساس ساختار پاسخ نمونه ارائه شده
    echo "دستیار: " . $responseData['output'][0]['content'][0]['text'] . "\n";
  } else {
    echo "پاسخ دریافت شد، اما محتوای متنی مورد انتظار یافت نشد.\n";
    echo "پاسخ کامل:\n";
    print_r($responseData);
  }
}
?>
```

### درخواست نمونه
```php
<?php
// مثال PHP برای بازیابی یک پاسخ خاص AvalAI (/v1/responses/{response_id})

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
if (!$apiKey) {
  die("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.\n");
}

$responseId = 'resp_123'; // شناسه پاسخی که باید بازیابی شود
$apiUrl = 'https://api.avalai.ir/v1/responses/' . $responseId;

// اختیاری: پارامترهای کوئری مانند 'include' را اضافه کنید
// $queryParams = ['include' => 'message.input_image.image_url'];
// $apiUrl .= '?' . http_build_query($queryParams);


$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json', // Content-Type ممکن است برای GET به طور دقیق لازم نباشد، اما روش خوبی است
'Authorization: Bearer ' . $apiKey
]);
// اختیاری: تنظیمات وقفه زمانی را اضافه کنید
// curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
// curl_setopt($ch, CURLOPT_TIMEOUT, 30);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #: " . $err . "\n";
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "بدنه پاسخ: " . $response . "\n";
} else {
  $responseData = json_decode($response, true);
  if (json_last_error() !== JSON_ERROR_NONE) {
    echo "خطا در رمزگشایی پاسخ JSON: " . json_last_error_msg() . "\n";
    echo "پاسخ خام: " . $response . "\n";
  } else {
    echo "پاسخ با موفقیت بازیابی شد:\n";
    print_r($responseData);
  }
}
?>
```

### درخواست نمونه
```php
<?php
// مثال PHP برای حذف یک پاسخ خاص AvalAI (/v1/responses/{response_id})

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
if (!$apiKey) {
  die("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.\n");
}

$responseId = 'resp_123'; // شناسه پاسخی که باید حذف شود
$apiUrl = 'https://api.avalai.ir/v1/responses/' . $responseId;

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE"); // مشخص کردن متد DELETE
curl_setopt($ch, CURLOPT_HTTPHEADER, [
// 'Content-Type: application/json', // معمولا برای DELETE لازم نیست
'Authorization: Bearer ' . $apiKey
]);
// اختیاری: تنظیمات وقفه زمانی را اضافه کنید
// curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
// curl_setopt($ch, CURLOPT_TIMEOUT, 30);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #: " . $err . "\n";
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "بدنه پاسخ: " . $response . "\n";
} else {
  $responseData = json_decode($response, true);
  if (json_last_error() !== JSON_ERROR_NONE) {
    echo "خطا در رمزگشایی پاسخ JSON: " . json_last_error_msg() . "\n";
    echo "پاسخ خام: " . $response . "\n";
  } elseif (isset($responseData['deleted']) && $responseData['deleted'] === true) {
    echo "شناسه پاسخ " . (isset($responseData['id']) ? $responseData['id'] : $responseId) . " با موفقیت حذف شد.\n";
  } else {
    echo "پاسخ دریافت شد، اما تایید حذف یافت نشد یا نامعتبر است.\n";
    echo "پاسخ کامل:\n";
    print_r($responseData);
  }
}
?>
```

### درخواست نمونه
```php
<?php
// مثال PHP برای لیست کردن آیتم‌های ورودی برای یک پاسخ AvalAI (/v1/responses/{response_id}/input_items)

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
if (!$apiKey) {
  die("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.\n");
}

$responseId = 'resp_abc123'; // شناسه پاسخ
$apiUrlBase = 'https://api.avalai.ir/v1/responses/' . $responseId . '/input_items';

// اختیاری: پارامترهای کوئری را اضافه کنید
$queryParams = [
// 'limit' => 10,
// 'order' => 'desc',
// 'after' => 'msg_xyz789',
// 'include' => 'message.input_image.image_url'
];
$apiUrl = $apiUrlBase . (empty($queryParams) ? '' : '?' . http_build_query($queryParams));


$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json', // ممکن است برای GET به طور دقیق لازم نباشد
'Authorization: Bearer ' . $apiKey
]);
// اختیاری: تنظیمات وقفه زمانی را اضافه کنید
// curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
// curl_setopt($ch, CURLOPT_TIMEOUT, 30);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #: " . $err . "\n";
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "بدنه پاسخ: " . $response . "\n";
} else {
  $responseData = json_decode($response, true);
  if (json_last_error() !== JSON_ERROR_NONE) {
    echo "خطا در رمزگشایی پاسخ JSON: " . json_last_error_msg() . "\n";
    echo "پاسخ خام: " . $response . "\n";
  } else {
    echo "لیست آیتم‌های ورودی با موفقیت بازیابی شد:\n";
    print_r($responseData);
  }
}
?>
```

### مدیریت جریان
```php
<?php
$apiKey = getenv('AVALAI_API_KEY');
if (!$apiKey) {
  die("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.\n");
}

$payload = json_encode([
  'model' => 'gpt-5.6-luna',
  'input' => 'یک داستان برایم بگو.',
  'stream' => true,
]);

$ch = curl_init('https://api.avalai.ir/v1/responses');
curl_setopt_array($ch, [
  CURLOPT_POST => true,
  CURLOPT_POSTFIELDS => $payload,
  CURLOPT_RETURNTRANSFER => false,
  CURLOPT_HTTPHEADER => [
    'Content-Type: application/json',
    'Accept: text/event-stream',
    'Authorization: Bearer ' . $apiKey,
  ],
  CURLOPT_WRITEFUNCTION => function ($curl, $chunk) {
    foreach (explode("\n", $chunk) as $line) {
      if (!str_starts_with($line, 'data: ')) {
        continue;
      }

      $data = substr($line, 6);
      if ($data === '[DONE]') {
        return strlen($chunk);
      }

      $event = json_decode($data, true);
      if (($event['type'] ?? null) === 'response.output_text.delta') {
        echo $event['delta'] ?? '';
        flush();
      }
    }

    return strlen($chunk);
  },
]);

curl_exec($ch);
if (curl_errno($ch)) {
  fwrite(STDERR, "\nخطای جریان: " . curl_error($ch) . "\n");
}
curl_close($ch);
echo "\n";
?>
```


## مرجع API پیام‌ها
_source: source-archive/مرجع-API-پیام-ها-1edf56.md_

### تکمیل پیام پایه
```php
<?php
// مثال PHP برای API پیام‌ها از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید واقعی خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/messages';

$data = [
 'model' => 'claude-haiku-4-5',
 'messages' => [
 ['role' => 'user', 'content' => 'سلام! آیا می‌توانید به من کمک کنید تا محاسبات کوانتومی را درک کنم؟']
 ],
 'max_tokens' => 1024
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'x-api-key: ' . $apiKey,
 'Content-Length: ' . strlen($jsonData)
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
 echo "خطای cURL #:" . $err;
} elseif ($httpcode >= 400) {
 echo "خطای HTTP: " . $httpcode . "\n";
 echo $response;
} else {
 $responseData = json_decode($response, true);
 echo "دستیار: " . $responseData['content'][0]['text'] . "\n";
}
?>
```


## مرجع API کاربر (User API)
_source: source-archive/مرجع-API-کاربر-User-API-abd0f7.md_

### احراز هویت
```php
<?php
// مثال PHP
$apiKey = getenv('AVALAI_API_KEY');

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.avalai.ir/user/v1/credit');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
    'Content-Type: application/json'
]);

$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
print_r($data);
?>
```

### درخواست
```php
<?php
// مثال PHP
$apiKey = getenv('AVALAI_API_KEY');

$ch = curl_init('https://api.avalai.ir/user/v1/credit');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . $apiKey]);

$response = curl_exec($ch);
curl_close($ch);

$credit = json_decode($response, true);
echo "اعتبار باقیمانده: " . $credit['remaining_irt'] . " تومان\n";
echo "سطح حساب: " . $credit['account_tier'] . "\n";
?>
```

### مثال‌ها
```php
<?php
// مثال PHP
$apiKey = getenv('AVALAI_API_KEY');

$params = http_build_query([
    'model' => 'gpt-5.6-luna',
    'hours_ago' => 168,
    'page_size' => 50
]);

$ch = curl_init('https://api.avalai.ir/user/v1/transactions?' . $params);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . $apiKey]);

$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
foreach ($data['transactions'] as $tx) {
    echo $tx['id'] . ': ' . $tx['model'] . ' - ' . $tx['tokens']['total'] . " توکن\n";
}
?>
```

### مثال
```php
<?php
// مثال PHP
$apiKey = getenv('AVALAI_API_KEY');

// مرحله ۱: یک فراخوانی API انجام دهید و avalai-request-id را ذخیره کنید
$ch = curl_init('https://api.avalai.ir/v1/chat/completions');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
    'Content-Type: application/json'
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
    'model' => 'gpt-5.4-mini',
    'messages' => [['role' => 'user', 'content' => 'سلام!']]
]));

$response = curl_exec($ch);
$headerSize = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
$headers = substr($response, 0, $headerSize);
curl_close($ch);

// استخراج avalai-request-id از هدرها
preg_match('/avalai-request-id:\s*([^\r\n]+)/i', $headers, $matches);
$requestId = trim($matches[1] ?? '');
echo "شناسه درخواست: $requestId\n";

// مرحله ۲: صبر کنید برای پردازش
sleep(5);

// مرحله ۳: جستجوی تراکنش
$ch = curl_init('https://api.avalai.ir/user/v1/transactions/lookup');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
    'Content-Type: application/json'
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
    'transaction_ids' => [$requestId]
]));

$lookupResponse = curl_exec($ch);
curl_close($ch);

$data = json_decode($lookupResponse, true);
if ($data['summary']['found'] > 0) {
    $tx = $data['transactions'][0];
    echo "هزینه دقیق: " . $tx['cost']['unit'] . " دلار\n";
    echo "هزینه دقیق: " . $tx['cost']['paid_irt'] . " تومان\n";
}
?>
```

### مثال‌ها
```php
<?php
// مثال PHP
$ch = curl_init('https://api.avalai.ir/user/v1/transactions/summary');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . getenv('AVALAI_API_KEY')]);

$response = curl_exec($ch);
curl_close($ch);

print_r(json_decode($response, true));
?>
```

### مثال‌ها
```php
<?php
$ch = curl_init('https://api.avalai.ir/user/v1/transactions/summary?group_by=provider');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . getenv('AVALAI_API_KEY')]);
$response = curl_exec($ch);
?>
```

### مثال‌ها
```php
<?php
$params = http_build_query(['group_by' => 'date', 'hours_ago' => 168]);
$ch = curl_init('https://api.avalai.ir/user/v1/transactions/summary?' . $params);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . getenv('AVALAI_API_KEY')]);
?>
```

### مثال‌ها
```php
<?php
// مثال PHP - تحلیل الگوی استفاده
$params = http_build_query(['group_by' => 'hour', 'hours_ago' => 24]);
$ch = curl_init('https://api.avalai.ir/user/v1/transactions/summary?' . $params);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . getenv('AVALAI_API_KEY')]);

$response = curl_exec($ch);
$data = json_decode($response, true);

foreach ($data['summary'] as $hour) {
    echo "ساعت {$hour['hour']}: {$hour['count']} درخواست\n";
}
?>
```

### درخواست
```php
<?php
// مثال PHP
$ch = curl_init('https://api.avalai.ir/user/v1/health');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . getenv('AVALAI_API_KEY')]);

$response = curl_exec($ch);
curl_close($ch);

print_r(json_decode($response, true));
?>
```


## مرجع مهاجرت API دستیاران (Assistants)
_source: source-archive/مرجع-مهاجرت-API-دستیاران-Assistants-df1a56.md_

### ایجاد یک دستیار
```php
<?php
// مثال PHP: ایجاد یک دستیار از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/assistants'; // از URL پایه AvalAI استفاده کنید

$data = [
'model' => 'gpt-5.6-luna',
'name' => 'Math Tutor',
'instructions' => 'شما یک معلم خصوصی ریاضی هستید. برای پاسخ به سوالات ریاضی کد بنویسید و اجرا کنید.',
'tools' => [['type' => 'code_interpreter']],
// 'description' => 'توضیحات اختیاری', // اختیاری
// 'metadata' => ['user_id' => '123'] // اختیاری
];

// Ensure instructions are properly encoded if they contain non-ASCII characters
$jsonData = json_encode($data, JSON_UNESCAPED_UNICODE);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json',
'Authorization: Bearer ' . $apiKey,
'OpenAI-Beta: assistants=v2', // هدر الزامی برای Assistants API v2
'Content-Length: ' . strlen($jsonData)
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #:" . $err;
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "پاسخ: " . $response;
} else {
  echo "پاسخ ایجاد دستیار:\n";
  echo $response;
  // $responseData = json_decode($response, true);
  // if (isset($responseData['id'])) {
    // echo "دستیار با شناسه ایجاد شد: " . $responseData['id'] . "\n";
    // } else {
      // print_r($responseData);
      // }
    }
    ?>
```


## مهندسی پرامپت
_source: source-archive/مهندسی-پرامپت-5ce1f0.md_

### پیام‌ها و نقش‌ها
```php
<?php

$apiKey = getenv('AVALAI_API_KEY');

$payload = [
    'model' => 'gpt-5.6-luna',
    'messages' => [
        [
            'role' => 'developer',
            'content' => 'You are a helpful assistant that answers programming questions in the style of a southern belle from the southeast United States.',
        ],
        [
            'role' => 'user',
            'content' => 'Are semicolons optional in JavaScript?',
        ],
    ],
];

$ch = curl_init('https://api.avalai.ir/v1/chat/completions');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . $apiKey,
        'Content-Type: application/json',
    ],
    CURLOPT_POSTFIELDS => json_encode($payload),
]);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
```

### پیام‌ها و نقش‌ها
```php
<?php

$apiKey = getenv('AVALAI_API_KEY');

$payload = [
    'model' => 'gpt-5.6-luna',
    'instructions' => 'You are a helpful assistant that answers programming questions in the style of a southern belle from the southeast United States.',
    'input' => 'Are semicolons optional in JavaScript?',
];

$ch = curl_init('https://api.avalai.ir/v1/responses');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . $apiKey,
        'Content-Type: application/json',
    ],
    CURLOPT_POSTFIELDS => json_encode($payload),
]);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
```


## هدرهای پاسخ
_source: source-archive/هدرهای-پاسخ-a617d7.md_

### مثال کامل هدرهای پاسخ
```php
<?php
// مثال PHP - دسترسی به هدرهای پاسخ
$ch = curl_init('https://api.avalai.ir/v1/chat/completions');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . getenv('AVALAI_API_KEY'),
    'Content-Type: application/json'
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
    'model' => 'gpt-5.4-mini',
    'messages' => [['role' => 'user', 'content' => 'سلام']]
]));

$response = curl_exec($ch);
$headerSize = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
$headers = substr($response, 0, $headerSize);
$body = substr($response, $headerSize);
curl_close($ch);

// تجزیه هدرها
preg_match('/avalai-request-id:\s*([^\r\n]+)/i', $headers, $requestId);
preg_match('/x-ratelimit-remaining-requests:\s*([^\r\n]+)/i', $headers, $remainingRequests);
preg_match('/x-ratelimit-remaining-tokens:\s*([^\r\n]+)/i', $headers, $remainingTokens);
preg_match('/x-ratelimit-reset-requests:\s*([^\r\n]+)/i', $headers, $resetTime);

echo "شناسه درخواست: " . trim($requestId[1] ?? '') . "\n";
echo "درخواست‌های باقی‌مانده: " . trim($remainingRequests[1] ?? '') . "\n";
echo "توکن‌های باقی‌مانده: " . trim($remainingTokens[1] ?? '') . "\n";
echo "زمان بازنشانی: " . trim($resetTime[1] ?? '') . "\n";
?>
```


## هوش مصنوعی در رباتیک با Gemini Robotics-ER
_source: source-archive/هوش-مصنوعی-در-رباتیک-با-Gemini-Robotics-ER-71c007.md_

### پیش‌نیازها
```php
# نصب OpenAI PHP SDK
composer require openai-php/client
```

### مثال: تشخیص اشیاء روی میز
```php
<?php

require 'vendor/autoload.php';

use OpenAI;

$client = OpenAI::factory()
    ->withApiKey($_ENV['AVALAI_API_KEY'])
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

// خواندن و رمزگذاری تصویر
$imageData = file_get_contents('workspace.jpg');
$base64Image = base64_encode($imageData);

$response = $client->chat()->create([
    'model' => 'gemini-robotics-er-1.5-preview',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                [
                    'type' => 'text',
                    'text' => 'Identify objects and return 2D coordinates in JSON format'
                ],
                [
                    'type' => 'image_url',
                    'image_url' => [
                        'url' => 'data:image/jpeg;base64,' . $base64Image
                    ]
                ]
            ]
        ]
    ]
]);

echo $response['choices'][0]['message']['content'];
```


## پاسخ‌های API جریانی
_source: source-archive/پاسخ-های-API-جریانی-66d055.md_

### فعال‌سازی جریان
```php
<?php
require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');

if (!$apiKey) {
    die("کلید API AvalAI پیدا نشد. متغیر محیطی AVALAI_API_KEY را تنظیم کنید.");
}

$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

try {
 $stream = $client->responses()->createStreamed([
 'model' => 'gpt-5.6-luna',
 'input' => [
 ['role' => 'user', 'content' => "عبارت 'double bubble bath' را ده بار سریع بگو."],
 ],
 // 'stream' => true, // اغلب توسط متد createStreamed مشخص می‌شود
 ]);

 echo "پاسخ جریانی:\n";
 foreach ($stream as $event) {
 // هر رویداد را به محض رسیدن پردازش کنید
 // ساختار $event به کتابخانه کلاینت PHP خاص بستگی دارد
 // مثال: دسترسی به داده‌ها اگر شیئی با متد toArray یا ویژگی‌های عمومی باشد
 if (method_exists($event, 'toArray')) {
 print_r($event->toArray());
 } else {
 var_dump($event);
 }
 echo "\n---\n";
 }

} catch (Exception $e) {
 echo "خطای API رخ داد: " . $e->getMessage() . "\n";
}
```


## پردازش اسناد با Mistral OCR
_source: source-archive/پردازش-اسناد-با-Mistral-OCR-46ed5d.md_

### استفاده از URL فایل PDF
```php
<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

// Create request payload
$payload = [
    'model' => 'mistral-ocr-latest',
    'document' => [
        'type' => 'document_url',
        'document_url' => 'https://arxiv.org/pdf/1805.04770'
    ],
    'pages' => range(0, 99), // Process up to 100 pages
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
    echo 'Error: ' . curl_error($ch);
} else {
    // Decode and display the response
    $result = json_decode($response, true);
    print_r($result);
}

// Close cURL session
curl_close($ch);
```

### استفاده از PDF کدگذاری شده با Base64
```php
<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

// Read and encode the PDF file
$pdfData = file_get_contents('document.pdf');
$base64Pdf = base64_encode($pdfData);
$documentUrl = 'data:application/pdf;base64,' . $base64Pdf;

// Create request payload
$payload = [
 'model' => 'mistral-ocr-latest',
 'document' => [
 'type' => 'document_url',
 'document_url' => $documentUrl
 ],
 'pages' => range(0, 99), // Process up to 100 pages
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
 echo 'Error: ' . curl_error($ch);
} else {
 // Decode and display the response
 $result = json_decode($response, true);
 print_r($result);
}

// Close cURL session
curl_close($ch);
```

### پردازش صفحات خاص
```php
<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

// Create request payload
$payload = [
 'model' => 'mistral-ocr-latest',
 'document' => [
 'type' => 'document_url',
 'document_url' => 'https://arxiv.org/pdf/1805.04770'
 ],
 'pages' => [0, 1, 5], // Process only specific pages
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
 echo 'Error: ' . curl_error($ch);
} else {
 // Decode and display the response
 $result = json_decode($response, true);
 print_r($result);
}

// Close cURL session
curl_close($ch);
```

### استفاده از URL تصویر
```php
<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

// Create request payload
$payload = [
 'model' => 'mistral-ocr-latest',
 'document' => [
 'type' => 'image_url',
 'image_url' => 'https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png'
 ],
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
 echo 'Error: ' . curl_error($ch);
} else {
 // Decode and display the response
 $result = json_decode($response, true);
 print_r($result);
}

// Close cURL session
curl_close($ch);
```

### استفاده از تصاویر کدگذاری شده با Base64
```php
<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

// Read and encode the image file
$imageData = file_get_contents('receipt.jpg');
$base64Image = base64_encode($imageData);
$imageUrl = 'data:image/jpeg;base64,' . $base64Image;

// Create request payload
$payload = [
 'model' => 'mistral-ocr-latest',
 'document' => [
 'type' => 'image_url',
 'image_url' => $imageUrl
 ],
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
	echo 'Error: ' . curl_error($ch);
} else {
	// Decode and display the response
	$result = json_decode($response, true);
	print_r($result);
}

// Close cURL session
curl_close($ch);
```

### پاسخگویی به سؤالات با مقالات علمی
```php
<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

// Create message content with both text and document
$messageContent = [
 ['type' => 'text', 'text' => 'What is the main research question addressed in this paper?'],
 ['type' => 'document_url', 'document_url' => 'https://arxiv.org/pdf/1805.04770']
];

// Create request payload
$payload = [
 'model' => 'mistral-small-latest',
 'messages' => [
 [
 'role' => 'user',
 'content' => $messageContent
 ]
 ]
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
 echo 'Error: ' . curl_error($ch);
} else {
 // Decode and display the response
 $result = json_decode($response, true);
 echo $result['choices'][0]['message']['content'];
}

// Close cURL session
curl_close($ch);
```

### استخراج اطلاعات از رسیدها
```php
<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

// Create message content with both text and image
$messageContent = [
 ['type' => 'text', 'text' => 'Extract the following information from this receipt: store name, date, total amount, and list of purchased items with prices.'],
 ['type' => 'image_url', 'image_url' => 'https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png']
];

// Create request payload
$payload = [
 'model' => 'mistral-small-latest',
 'messages' => [
 [
 'role' => 'user',
 'content' => $messageContent
 ]
 ]
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
 echo 'Error: ' . curl_error($ch);
} else {
 // Decode and display the response
 $result = json_decode($response, true);
 echo $result['choices'][0]['message']['content'];
}

// Close cURL session
curl_close($ch);
```


## پردازش فایل های PDF با API AvalAI
_source: source-archive/پردازش-فایل-های-PDF-با-API-AvalAI-4a49a9.md_

### پردازش PDF مبتنی بر URL
```php
<?php

require 'vendor/autoload.php';

// مقداردهی اولیه کلاینت با API AvalAI
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

// آدرس PDF
$fileUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

// ایجاد درخواست با ارجاع به فایل مبتنی بر URL
$fileContent = [
 [
 "type" => "text",
 "text" => "این سند درباره چیست؟"
 ],
 [
 "type" => "file",
 "file" => [
 "file_id" => $fileUrl
 ]
 ]
];

// ارسال درخواست به مدل
$completion = $client->chat()->create([
 'model' => 'claude-sonnet-4-6',
 'messages' => [
 [
 'role' => 'user',
 'content' => $fileContent
 ]
 ]
]);

echo $completion->choices[0]->message->content;
```

### پردازش PDF مبتنی بر کدگذاری base64
```php
<?php

require 'vendor/autoload.php';

// مقداردهی اولیه کلاینت با API AvalAI
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

// تابع دریافت PDF کدگذاری شده با base64
function getBase64PDF() {
 // روش 1: از یک URL
 $pdfUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";
 $fileData = file_get_contents($pdfUrl);
 
 // روش 2: از یک فایل محلی
 // $fileData = file_get_contents("path/to/your/document.pdf");
 
 return "data:application/pdf;base64," . base64_encode($fileData);
}

// دریافت PDF کدگذاری شده با base64
$base64Pdf = getBase64PDF();

// ایجاد درخواست با فایل کدگذاری شده با base64
$fileContent = [
 [
 "type" => "text",
 "text" => "این سند درباره چیست؟"
 ],
 [
 "type" => "file",
 "file" => [
 "file_data" => $base64Pdf
 ]
 ]
];

// ارسال درخواست به مدل
$completion = $client->chat()->create([
 'model' => 'claude-sonnet-4-6',
 'messages' => [
 [
 'role' => 'user',
 'content' => $fileContent
 ]
 ]
]);

echo $completion->choices[0]->message->content;
```

### مشخص کردن فرمت
```php
<?php

require 'vendor/autoload.php';

// مقداردهی اولیه کلاینت با API AvalAI
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

// آدرس PDF
$fileUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

// ایجاد درخواست با مشخص کردن فرمت
$fileContent = [
 [
 "type" => "text",
 "text" => "این سند درباره چیست؟"
 ],
 [
 "type" => "file",
 "file" => [
 "file_id" => $fileUrl,
 "format" => "application/pdf"
 ]
 ]
];

// ارسال درخواست به مدل
$completion = $client->chat()->create([
 'model' => 'claude-sonnet-4-6',
 'messages' => [
 [
 'role' => 'user',
 'content' => $fileContent
 ]
 ]
]);

echo $completion->choices[0]->message->content;
```

### خلاصه‌سازی اسناد
```php
<?php

require 'vendor/autoload.php';

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

$fileUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

$fileContent = [
 [
 "type" => "text",
 "text" => "خلاصه‌ای مختصر از این سند ارائه دهید."
 ],
 [
 "type" => "file",
 "file" => [
 "file_id" => $fileUrl
 ]
 ]
];

$completion = $client->chat()->create([
 'model' => 'claude-sonnet-4-6',
 'messages' => [
 [
 'role' => 'user',
 'content' => $fileContent
 ]
 ]
]);

echo $completion->choices[0]->message->content;
```

### استخراج اطلاعات
```php
<?php

require 'vendor/autoload.php';

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

$fileUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

$fileContent = [
 [
 "type" => "text",
 "text" => "تمام تاریخ‌های ذکر شده در این سند را استخراج کرده و به ترتیب زمانی فهرست کنید."
 ],
 [
 "type" => "file",
 "file" => [
 "file_id" => $fileUrl
 ]
 ]
];

$completion = $client->chat()->create([
 'model' => 'claude-sonnet-4-6',
 'messages' => [
 [
 'role' => 'user',
 'content' => $fileContent
 ]
 ]
]);

echo $completion->choices[0]->message->content;
```


## پردازش فایل‌های اکسل با API AvalAI
_source: source-archive/پردازش-فایل-های-اکسل-با-API-AvalAI-899b49.md_

### پردازش اکسل با کدگذاری base64
```php
<?php

require 'vendor/autoload.php';

// مقداردهی اولیه کلاینت با API AvalAI
$client = OpenAI::client('your-avalai-api-key', [
	'base_url' => 'https://api.avalai.ir/v1'
]);

// تابع دریافت فایل اکسل کدگذاری شده با base64
function getBase64Excel() {
	// از یک فایل محلی
	$fileData = file_get_contents("path/to/your/spreadsheet.xlsx");
	return "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64," . base64_encode($fileData);
}

// دریافت فایل اکسل کدگذاری شده با base64
$base64Excel = getBase64Excel();

// ایجاد درخواست با فایل کدگذاری شده با base64
$fileContent = [
	[
		"type" => "text",
		"text" => "این صفحه گسترده را تحلیل کرده و بینش‌های کلیدی ارائه دهید."
	],
	[
		"type" => "file",
		"file" => [
			"file_data" => $base64Excel
		]
	]
];

// ارسال درخواست به مدل
$completion = $client->chat()->create([
	'model' => 'gpt-5.6-luna',
	'messages' => [
		[
			'role' => 'user',
			'content' => $fileContent
		]
	]
]);

echo $completion->choices[0]->message->content;
```

### تبدیل DataFrame
```php
<?php

require 'vendor/autoload.php';
use PhpOffice\PhpSpreadsheet\IOFactory;

// مقداردهی اولیه کلاینت با API AvalAI
$client = OpenAI::client('your-avalai-api-key', [
	'base_url' => 'https://api.avalai.ir/v1'
]);

// تابع تبدیل اکسل به نمایش متنی
function excelToText($filePath) {
	// بارگذاری فایل اکسل
	$spreadsheet = IOFactory::load($filePath);
	$worksheet = $spreadsheet->getActiveSheet();

	// دریافت بالاترین سطر و ستون
	$highestRow = $worksheet->getHighestRow();
	$highestColumn = $worksheet->getHighestColumn();

	// تبدیل به نمایش متنی
	$textRepresentation = '';
	for ($row = 1; $row <= $highestRow; $row++) {
		$rowData = [];
		for ($col = 'A'; $col <= $highestColumn; $col++) {
			$rowData[] = $worksheet->getCell($col . $row)->getValue();
		}
		$textRepresentation .= implode("\t", $rowData) . "\n";
	}

	return $textRepresentation;
}

// دریافت نمایش متنی فایل اکسل
$excelText = excelToText("path/to/your/spreadsheet.xlsx");

// ایجاد پرامپت با داده‌های اکسل
$prompt = "
من داده‌های صفحه گسترده زیر را دارم:

$excelText

لطفا این داده‌ها را تحلیل کرده و بینش‌های کلیدی ارائه دهید.
";

// ارسال درخواست به مدل
$completion = $client->chat()->create([
	'model' => 'claude-sonnet-4-6',
	'messages' => [
		[
			'role' => 'user',
			'content' => $prompt
		]
	]
]);

echo $completion->choices[0]->message->content;
```

