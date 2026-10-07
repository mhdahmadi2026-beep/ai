# راهنمای استفاده سازمانی / Enterprise usage guide — https://docs.avalai.ir/fa/resellers/enterprise-guide
For large-scale organizations and API resellers needing advanced usage tracking, cost management and operational insight on high-volume AvalAI API deployments. Foundation: **User API** (`/user/v1/`). Pair with `cost-tracking-guide.md`.

## Overview — enterprise needs
High volume (100Ks–millions of calls/day) · multi-tenant (departments/customers/projects) · cost allocation per business unit · compliance (audit trail, data governance) · performance (minimal tracking latency) · analytics (BI & usage insight).

## Use cases
### 1. Internal IT service provider
Large company serving AI to multiple business units. Needs: per-department usage tracking, chargeback/showback reports, budget alerts/controls, compliance audit trail.
```python
# tag requests with a department id
response = requests.post(
    "https://api.avalai.ir/v1/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    json={
        "model": "gpt-5.6-luna",
        "messages": messages,
        "safety_identifier": f"dept-{department_id}",  # custom id in the body
    },
)

# later, filter transactions by department
transactions = get_transactions(safety_identifier=f"dept-{department_id}")
```
> Skill note: `get_transactions(...)` is pseudo-code in the doc (not a documented endpoint). To attribute cost, store `avalai-request-id` + your tags locally and use `/user/v1/transactions/lookup` (see cost-tracking-guide). Responses API equivalent: `client.responses.create(model=…, instructions=…, input=…)` → `response.output_text`; `messages`→`input`.

### 2. SaaS platform provider
AI features embedded for thousands of customers. Needs: per-customer tracking, real-time cost, usage-based billing, per-customer rate limits.
```python
# customer-specific API proxy
class CustomerAPIProxy:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.api_key = get_api_key_for_customer(customer_id)

    async def chat_completion(self, **kwargs):
        # check customer quota
        if not await self.check_quota():
            raise QuotaExceededError()

        # request with customer tracking
        response = await make_api_request(**kwargs)
        request_id = response.headers.get("avalai-request-id")

        # queue cost tracking
        await queue_cost_lookup(request_id, self.customer_id)

        return response.json()
```
**OpenAI SDK tip:** `request_id = response._request_id` (SDK parses headers automatically):
```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")
response = client.chat.completions.create(model="gpt-5.4-mini", messages=messages)

request_id = response._request_id
```
**LangChain tip:** custom httpx client + callback to capture headers (same code as in cost-tracking-guide; `request_id = callback.request_id`). Async variants: /fa/api-reference/response-headers#access-avalai-request-id-with-langchain.
```python
import httpx
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import BaseCallbackHandler
from contextvars import ContextVar
import os

request_headers: ContextVar[dict] = ContextVar('request_headers', default={})

class HeaderCapturingClient(httpx.Client):
    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)
        request_headers.set(dict(response.headers))
        return response

class HeaderAccessCallback(BaseCallbackHandler):
    def __init__(self):
        self.request_id = None

    def on_llm_end(self, response, **kwargs):
        headers = request_headers.get()
        self.request_id = headers.get('avalai-request-id')

http_client = HeaderCapturingClient()
chat = ChatOpenAI(
    base_url="https://api.avalai.ir/v1",
    api_key=os.getenv("AVALAI_API_KEY"),
    model="gpt-5.4-mini",
    http_client=http_client,
)

callback = HeaderAccessCallback()
response = chat.invoke("سلام", config={"callbacks": [callback]})
request_id = callback.request_id
```

### 3. AI-services reseller
Resells API access with markup. Needs: exact cost for billing, multiple price tiers, volume discounts, detailed invoices → see /fa/resellers/cost-tracking-guide.

### 4. Research organization
University/lab with multiple projects. Needs: grant-based cost allocation, per-project usage reports, researcher access controls, audit trails for publications.

## High-volume cost tracking — batch strategy (up to 1000 ids/call)
```python
import asyncio
from typing import List
from datetime import datetime, timedelta


class EnterpriseCostTracker:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.avalai.ir"
        self.pending_requests = []

    async def track_request(self, request_id: str, metadata: dict):
        """Queue a request for cost tracking"""
        self.pending_requests.append(
            {
                "request_id": request_id,
                "metadata": metadata,
                "queued_at": datetime.now(),
            }
        )

    async def process_batch(self, batch_size: int = 1000):
        """Process pending requests in batches"""
        while self.pending_requests:
            batch = self.pending_requests[:batch_size]  # up to 1000
            request_ids = [r["request_id"] for r in batch]

            response = await self.lookup_costs(request_ids)

            for transaction in response["transactions"]:
                request_id = transaction["id"]
                metadata = next(
                    r["metadata"] for r in batch if r["request_id"] == request_id
                )

                await self.record_cost(transaction, metadata)

            self.pending_requests = self.pending_requests[batch_size:]

    async def lookup_costs(self, request_ids: List[str]):
        """Look up costs for multiple requests"""
        response = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: requests.post(
                f"{self.base_url}/user/v1/transactions/lookup",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={"transaction_ids": request_ids},
            ),
        )
        return response.json()

    async def record_cost(self, transaction: dict, metadata: dict):
        """Record cost to the database"""
        cost_usd = float(transaction["cost"]["unit"])
        cost_irt = float(transaction["cost"]["paid_irt"]) + float(
            transaction["cost"]["paid_grant_irt"]
        )

        await db.insert_cost_record(
            {
                "request_id": transaction["id"],
                "customer_id": metadata.get("customer_id"),
                "department_id": metadata.get("department_id"),
                "project_id": metadata.get("project_id"),
                "cost_usd": cost_usd,
                "cost_irt": cost_irt,
                "model": transaction["model"],
                "tokens": transaction["tokens"],
                "timestamp": transaction["requested_at"],
            }
        )


tracker = EnterpriseCostTracker(api_key)

await tracker.track_request(
    request_id,
    {"customer_id": "cust_123", "department_id": "eng", "project_id": "proj_456"},
)

# background processing every minute
while True:
    await tracker.process_batch(batch_size=1000)
    await asyncio.sleep(60)
```
> Skill notes: the loop slices `pending_requests` by `batch_size` even if some IDs weren't found yet (not-found transactions are silently dropped) — re-queue those whose cost wasn't returned (wait ≥5–30 s after the request). Also needs `import requests`; the `next(...)` raises if an id in the response isn't in the batch.

## Multi-tenant architecture
```
Load Balancer
   ├─ API Server 1 ┐
   ├─ API Server 2 ├─→ Request-tracking queue (Redis/Kafka) → Cost-processing workers (async) → Database (PostgreSQL/MongoDB)
   └─ API Server 3 ┘
```
### Example DB schema
```sql
-- customers / tenants
CREATE TABLE customers (
    id UUID PRIMARY KEY,
    name VARCHAR(255),
    api_key_id INTEGER,
    pricing_tier VARCHAR(50),
    created_at TIMESTAMP
);

-- request tracking
CREATE TABLE api_requests (
    request_id UUID PRIMARY KEY,
    customer_id UUID REFERENCES customers(id),
    model VARCHAR(100),
    requested_at TIMESTAMP,
    cost_usd DECIMAL(12, 8),
    cost_irt DECIMAL(12, 2),
    tokens_total INTEGER,
    tokens_prompt INTEGER,
    tokens_completion INTEGER,
    status VARCHAR(50),
    metadata JSONB
);

-- performance indexes
CREATE INDEX idx_requests_customer ON api_requests(customer_id);
CREATE INDEX idx_requests_timestamp ON api_requests(requested_at);
CREATE INDEX idx_requests_status ON api_requests(status);

-- daily usage summary
CREATE MATERIALIZED VIEW daily_usage_summary AS
SELECT 
    customer_id,
    DATE(requested_at) as usage_date,
    COUNT(*) as request_count,
    SUM(cost_usd) as total_cost_usd,
    SUM(cost_irt) as total_cost_irt,
    SUM(tokens_total) as total_tokens
FROM api_requests
WHERE status = 'completed'
GROUP BY customer_id, DATE(requested_at);

-- periodic refresh (CONCURRENTLY needs a UNIQUE index on the view)
REFRESH MATERIALIZED VIEW CONCURRENTLY daily_usage_summary;
```
> Skill note: `REFRESH ... CONCURRENTLY` requires a unique index on the materialized view (e.g. `CREATE UNIQUE INDEX ON daily_usage_summary(customer_id, usage_date)`).

## Advanced analytics — real-time usage dashboard (FastAPI)
```python
from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()


@app.get("/analytics/realtime/{customer_id}")
async def get_realtime_analytics(customer_id: str):
    """Real-time usage analytics for a customer"""
    now = datetime.now()

    # last hour
    hour_stats = await db.query(
        """
        SELECT 
            COUNT(*) as requests,
            SUM(cost_usd) as cost,
            SUM(tokens_total) as tokens,
            AVG(tokens_total) as avg_tokens_per_request
        FROM api_requests
        WHERE customer_id = $1
        AND requested_at >= $2
    """,
        customer_id,
        now - timedelta(hours=1),
    )

    # model distribution (24 h)
    model_dist = await db.query(
        """
        SELECT 
            model,
            COUNT(*) as count,
            SUM(cost_usd) as cost
        FROM api_requests
        WHERE customer_id = $1
        AND requested_at >= $2
        GROUP BY model
        ORDER BY count DESC
    """,
        customer_id,
        now - timedelta(hours=24),
    )

    # cost trend (last 7 days)
    cost_trend = await db.query(
        """
        SELECT 
            DATE(requested_at) as date,
            SUM(cost_usd) as daily_cost
        FROM api_requests
        WHERE customer_id = $1
        AND requested_at >= $2
        GROUP BY DATE(requested_at)
        ORDER BY date
    """,
        customer_id,
        now - timedelta(days=7),
    )

    return {
        "customer_id": customer_id,
        "last_hour": hour_stats,
        "model_distribution": model_dist,
        "cost_trend": cost_trend,
    }
```

## Security best practices
### API key management — separate key per customer/tenant
```python
class APIKeyManager:
    def __init__(self):
        self.key_store = {}  # use proper secrets management

    def create_customer_key(self, customer_id: str) -> str:
        """Create a dedicated API key for a customer"""
        key_id = self.register_key(customer_id)
        return f"customer_{customer_id}_key_{key_id}"

    def get_avalai_key(self, customer_key: str) -> str:
        """Map a customer key to the master AvalAI key"""
        if not self.validate_key(customer_key):
            raise UnauthorizedError()

        return os.getenv("AVALAI_MASTER_API_KEY")
```
(Doc's pattern: customers get *your* keys; you map to the master AvalAI key server-side. Never expose the AvalAI key to customers/browsers; use real secrets management and generate high-entropy random customer keys rather than guessable `customer_<id>_key_<n>` strings.)
### Per-customer rate limiting (Redis)
```python
from redis import Redis
from datetime import datetime, timedelta


class EnterpriseRateLimiter:
    def __init__(self, redis_client: Redis):
        self.redis = redis_client

    async def check_limit(self, customer_id: str, limit_per_minute: int = 1000) -> bool:
        """Check the customer is within rate limits"""
        key = f"rate_limit:{customer_id}:{datetime.now().strftime('%Y%m%d%H%M')}"

        count = await self.redis.incr(key)
        if count == 1:
            await self.redis.expire(key, 60)

        return count <= limit_per_minute
```
(The code uses `await` with a sync `redis.Redis` — use `redis.asyncio.Redis`. Remember your own limit must also fit your AvalAI account-tier limits — see 09-rate-limits.)

## Performance optimization
### Cost cache
```python
from functools import lru_cache
import redis


class CostCache:
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
        self.cache_ttl = 3600  # 1 hour

    async def get_cached_cost(self, request_id: str) -> dict:
        """Get cost from cache if present"""
        cached = await self.redis.get(f"cost:{request_id}")
        if cached:
            return json.loads(cached)
        return None

    async def cache_cost(self, request_id: str, cost_data: dict):
        """Cache cost data"""
        await self.redis.setex(
            f"cost:{request_id}", self.cache_ttl, json.dumps(cost_data)
        )
```
(needs `import json`; async redis client)
### Connection pooling
```python
import aiohttp
from aiohttp import TCPConnector

# reuse connections for better performance
connector = TCPConnector(limit=100, limit_per_host=30)
session = aiohttp.ClientSession(connector=connector)


async def make_api_request(**kwargs):
    """API request with connection pooling"""
    async with session.post(
        "https://api.avalai.ir/v1/chat/completions", **kwargs
    ) as response:
        return await response.json()
```
Responses API equivalent for the chat examples (`client.responses.create(model="gpt-5.6-luna", instructions="You are a helpful assistant.", input="Write a one-sentence summary of AvalAI.")` → `response.output_text`).

## Video-generation tracking (Sora, Veo, Runway)
Unlike chat completions, where `request_id` is only in response **headers**, **Video API responses include tracking fields in the JSON body**: `id` (video id), **`request_id`** (UUID v7, for cost tracking) and `safety_identifier`.
```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/videos",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": "sora-2",
        "prompt": "ویدیوی نمایش محصول",
        "size": "1280x720",
        "seconds": "4",
        "safety_identifier": f"dept-{department_id}",  # your internal id
    },
)

video = response.json()

print(f"video id: {video['id']}")
print(f"request id: {video['request_id']}")  # UUID v7 for cost tracking
print(f"safety id: {video.get('safety_identifier')}")
```
> ⚠ **`sora-2` / `sora-2-pro` and OpenAI's Videos API were shut down 2026-09-24** (see 10-deprecations). Treat Sora examples as pattern only; use a currently available video model (e.g. Veo / Runway Gen-4 in 06-pricing) and verify on `/v1/models`.
### Filter videos by identifier
```python
# all videos of a department
department_videos = requests.get(
    "https://api.avalai.ir/v1/videos",
    headers={"Authorization": f"Bearer {API_KEY}"},
    params={"safety_identifier": f"dept-{department_id}"},
).json()

# one video by request_id
specific_video = requests.get(
    "https://api.avalai.ir/v1/videos",
    headers={"Authorization": f"Bearer {API_KEY}"},
    params={"request_id": "019b47a0-ece8-75b2-8a4c-40fcf4b49479"},
).json()
```
### Video-cost tracking service (multi-service)
```python
class VideoTrackingService:
    """
    Track video generation across multiple services using safety_identifier.
    Use case: marketing requests video generation; multiple services
    (billing, analytics, notifications) need to query the same video.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.avalai.ir"

    async def create_tracked_video(
        self, prompt: str, department_id: str, project_id: str
    ) -> dict:
        """Create a video with enterprise tracking identifiers"""
        # composite safety_identifier for multi-dimensional tracking
        safety_id = f"dept_{department_id}_proj_{project_id}"

        response = requests.post(
            f"{self.base_url}/v1/videos",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": "sora-2-pro",
                "prompt": prompt,
                "size": "1792x1024",
                "seconds": "8",
                "safety_identifier": safety_id,
            },
        )

        video = response.json()

        # store request_id for cost tracking
        await self.queue_cost_lookup(
            request_id=video["request_id"],
            video_id=video["id"],
            department_id=department_id,
            project_id=project_id,
        )

        return video

    async def get_department_videos(self, department_id: str) -> list:
        """All videos for a department using a safety_identifier prefix"""
        response = requests.get(
            f"{self.base_url}/v1/videos",
            headers={"Authorization": f"Bearer {self.api_key}"},
            params={"safety_identifier": f"dept_{department_id}"},
        )

        return response.json()["data"]

    async def queue_cost_lookup(self, request_id: str, **metadata):
        """Queue video cost tracking using request_id"""
        cost_response = requests.post(
            f"{self.base_url}/user/v1/transactions/lookup",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"transaction_ids": [request_id]},
        )

        if cost_response.json()["transactions"]:
            transaction = cost_response.json()["transactions"][0]
            await self.record_video_cost(transaction, metadata)
```
> Note: immediately looking up cost after creation will often return nothing (cost is available after ~30 s, and video generation is async) — retry/queue. A `safety_identifier` *prefix* filter is the doc's assumption; verify exact-match vs prefix behavior in /fa/api-reference/videos.
### Video tracking DB schema
```sql
CREATE TABLE video_requests (
    video_id VARCHAR(64) PRIMARY KEY,
    request_id UUID UNIQUE NOT NULL,
    safety_identifier VARCHAR(256),
    customer_id UUID REFERENCES customers(id),
    department_id VARCHAR(50),
    project_id VARCHAR(50),
    model VARCHAR(100),
    prompt TEXT,
    size VARCHAR(20),
    seconds INTEGER,
    status VARCHAR(20),
    requested_at TIMESTAMP,
    completed_at TIMESTAMP,
    cost_usd DECIMAL(12, 8),
    cost_irt DECIMAL(12, 2)
);

CREATE INDEX idx_video_safety_id ON video_requests(safety_identifier);
CREATE INDEX idx_video_request_id ON video_requests(request_id);
CREATE INDEX idx_video_customer ON video_requests(customer_id);
CREATE INDEX idx_video_department ON video_requests(department_id);
CREATE INDEX idx_video_status ON video_requests(status);
```

## Related
/fa/api-reference/user · /fa/api-reference/videos · /fa/resellers/cost-tracking-guide · /fa/api-reference/response-headers · /fa/guides/rate-limits
**Enterprise support:** dedicated account management & enterprise pricing → **support@avalai.ir**.
