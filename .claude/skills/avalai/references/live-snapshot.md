# AvalAI live snapshot — 2026-10-07 13:47 UTC

Source: GET /public/models. USD per 1M tokens unless noted.

| id | mode | min_tier | pricing | in/out ctx |
|---|---|---|---|---|
| `cf.flux-2-dev` | image_generation | 1 | cached_input=0.0, input=0.0, input_cost_per_megapixel=0.001, output=10.0, output_cost_per_additional_megapixel=0.001, output_cost_per_image=0.01, output_cost_per_image_2mp=0.011, output_cost_per_image_3mp=0.012, output_cost_per_image_4mp=0.013, tokens_per_megapixel=1000 | / |
| `cf.flux-2-klein-4b` | image_generation | 1 | cached_input=0.0, input=0.0, input_cost_per_megapixel=0.002, output=10.0, output_cost_per_additional_megapixel=0.002, output_cost_per_image=0.01, output_cost_per_image_2mp=0.012, output_cost_per_image_3mp=0.014, output_cost_per_image_4mp=0.016, tokens_per_megapixel=1000 | / |
| `cf.flux-2-klein-9b` | image_generation | 1 | cached_input=0.0, input=0.0, input_cost_per_megapixel=0.002, output=15.0, output_cost_per_additional_megapixel=0.002, output_cost_per_image=0.015, output_cost_per_image_2mp=0.017, output_cost_per_image_3mp=0.019, output_cost_per_image_4mp=0.021, tokens_per_megapixel=1000 | / |
| `cf.lucid-origin` | image_generation | 1 | cached_input=0.0, input=0.0, output=15.0, output_cost_per_image=0.015, output_cost_per_image_2mp=0.017, output_cost_per_image_3mp=0.019, output_cost_per_image_4mp=0.021 | / |
| `cf.phoenix-1.0` | image_generation | 1 | cached_input=0.0, input=0.0, output=15.0, output_cost_per_image=0.015, output_cost_per_image_2mp=0.017, output_cost_per_image_3mp=0.019, output_cost_per_image_4mp=0.021 | / |
| `flux-1.1-pro` | image_generation | 1 | cached_input=0.0, input=0.0, output=40.0, output_cost_per_image=0.04 | / |
| `flux.1-kontext-pro` | image_generation | 1 | cached_input=0.0, input=0.0, output=40.0, output_cost_per_image=0.04 | / |
| `flux.2-pro` | image_generation | 1 | cached_input=0.0, input=15.0, input_cost_per_megapixel=0.015, output=30.0, output_cost_per_additional_megapixel=0.015, output_cost_per_image=0.03, output_cost_per_image_2mp=0.045, output_cost_per_image_3mp=0.06, output_cost_per_image_4mp=0.075 | / |
| `cf.qwen2.5-coder-32b-instruct` | chat | 0 | cached_input=0.33, input=0.66, output=1.0 | / |
| `cf.qwen3-30b-a3b-fp8` | chat | 0 | cached_input=0.025, input=0.051, output=0.34 | 40960/20000 |
| `cf.qwq-32b` | chat | 0 | cached_input=0.33, input=0.66, output=1.0 | / |
| `groq.qwen3-32b` | chat | 0 | cached_input=0.145, input=0.29, output=0.59 | 131000/131000 |
| `qwen-flash` | chat | 0 | cached_input=0.025, cached_input_above_256K=0.125, input=0.05, input_above_256K=0.25, output=0.4, output_above_256K=2.0 | 997952/32768 |
| `qwen-flash-2025-07-28` | chat | 0 | cached_input=0.025, cached_input_above_256K=0.125, input=0.05, input_above_256K=0.25, output=0.4, output_above_256K=2.0 | 997952/32768 |
| `qwen-image` | image_generation | 0 | cached_input=0.0, input=0.0, output=35.0, output_cost_per_image=0.035 | / |
| `qwen-image-2.0` | image_generation | 1 | cached_input=0.0, input=0.0, output=35.0, output_cost_per_image=0.035 | / |
| `qwen-image-2.0-pro` | image_generation | 1 | cached_input=0.0, input=0.0, output=75.0, output_cost_per_image=0.075 | / |
| `qwen-image-3.0` | image_generation | 1 | cached_input=0.0, input=0.0, input_cost_per_image=0.003, output=40.0, output_cost_per_image=0.04, output_cost_per_image_2mp=0.075, output_cost_per_image_3mp=0.075, output_cost_per_image_4mp=0.075 | / |
| `qwen-image-3.0-pro` | image_generation | 1 | cached_input=0.0, input=0.0, input_cost_per_image=0.003, output=40.0, output_cost_per_image=0.04, output_cost_per_image_2mp=0.075, output_cost_per_image_3mp=0.075, output_cost_per_image_4mp=0.075 | / |
| `qwen-image-edit` | image_generation | 0 | cached_input=0.0, input=0.0, output=45.0, output_cost_per_image=0.045 | / |
| `qwen-image-edit-plus` | image_generation | 1 | cached_input=0.0, input=0.0, output=30.0, output_cost_per_image=0.03 | / |
| `qwen-image-plus` | image_generation | 1 | cached_input=0.0, input=0.0, output=30.0, output_cost_per_image=0.03 | / |
| `qwen-max` | chat | 5 | cached_input=0.8, input=1.6, output=6.4 | 30720/8192 |
| `qwen-max-2025-01-25` | chat | 5 | cached_input=0.8, input=1.6, output=6.4 | 30720/8192 |
| `qwen-max-latest` | chat | 5 | cached_input=0.8, input=1.6, output=6.4 | 30720/8192 |
| `qwen-mt-flash` | chat | 0 | cached_input=0.08, input=0.16, output=0.49 | 8192/8192 |
| `qwen-mt-lite` | chat | 0 | cached_input=0.06, input=0.12, output=0.36 | 8192/8192 |
| `qwen-mt-plus` | chat | 0 | cached_input=1.2, input=2.46, output=7.37 | 2048/2048 |
| `qwen-mt-turbo` | chat | 0 | cached_input=0.08, input=0.16, output=0.49 | 2048/2048 |
| `qwen-plus` | chat | 0 | cached_input=0.2, input=0.4, output=4.0 | 129024/16384 |
| `qwen-plus-2025-04-28` | chat | 0 | cached_input=0.2, input=0.4, output=4.0 | 129024/16384 |
| `qwen-plus-2025-07-14` | chat | 0 | cached_input=0.2, input=0.4, output=4.0 | 129024/16384 |
| `qwen-plus-2025-07-28` | chat | 0 | cached_input=0.2, input=0.4, output=4.0 | 997952/32768 |
| `qwen-plus-2025-09-11` | chat | 0 | cached_input=0.2, input=0.4, output=4.0 | 997952/32768 |
| `qwen-plus-2025-12-01` | chat | 0 | cached_input=0.2, input=0.4, output=4.0 | 997952/32768 |
| `qwen-plus-character` | chat | 0 | cached_input=0.05, input=0.5, output=1.4 | 30000/4096 |
| `qwen-plus-latest` | chat | 0 | cached_input=0.2, input=0.4, output=4.0 | 129024/16384 |
| `qwen3-14b` | chat | 0 | cached_input=0.16, input=0.35, output=4.2 | 98304/8192 |
| `qwen3-235b-a22b` | chat | 0 | cached_input=0.35, input=0.7, output=8.4 | 131072/32768 |
| `qwen3-235b-a22b-fp8-tput` | chat | 1 | cached_input=0.1, input=0.2, output=0.6 | / |
| `qwen3-235b-a22b-instruct-2507` | chat | 0 | cached_input=0.35, input=0.7, output=2.8 | 131072/32768 |
| `qwen3-235b-a22b-thinking-2507` | chat | 0 | cached_input=0.35, input=0.7, output=8.4 | 131072/32768 |
| `qwen3-30b-a3b` | chat | 0 | cached_input=0.1, input=0.2, output=2.4 | 98304/32768 |
| `qwen3-30b-a3b-instruct-2507` | chat | 0 | cached_input=0.1, input=0.2, output=0.8 | 98304/32768 |
| `qwen3-30b-a3b-thinking-2507` | chat | 0 | cached_input=0.1, input=0.2, output=2.4 | 98304/32768 |
| `qwen3-32b` | chat | 0 | cached_input=0.35, input=0.7, output=8.4 | 98304/16384 |
| `qwen3-8b` | chat | 0 | cached_input=0.09, input=0.18, output=2.1 | 98304/8192 |
| `qwen3-coder-480b-a35b-instruct` | chat | 0 | cached_input=0.15, cached_input_above_128K=0.45, cached_input_above_32K=0.27, input=1.5, input_above_128K=4.5, input_above_32K=2.7, output=7.5, output_above_128K=22.5, output_above_32K=13.5 | 204800/65536 |
| `qwen3-coder-flash` | chat | 0 | cached_input=0.1, cached_input_above_128K=0.3, cached_input_above_256K=0.6, cached_input_above_32K=0.18, input=0.3, input_above_128K=0.8, input_above_256K=1.6, input_above_32K=0.5, output=1.5, output_above_128K=4.0, output_above_256K=9.6, output_above_32K=2.5 | 997952/65536 |
| `qwen3-coder-flash-2025-07-28` | chat | 0 | cached_input=0.1, cached_input_above_128K=0.3, cached_input_above_256K=0.6, cached_input_above_32K=0.18, input=0.3, input_above_128K=0.8, input_above_256K=1.6, input_above_32K=0.5, output=1.5, output_above_128K=4.0, output_above_256K=9.6, output_above_32K=2.5 | 997952/65536 |
| `qwen3-coder-next` | chat | 0 | cached_input=0.15, input=0.3, output=1.5 | 200000/64000 |
| `qwen3-coder-plus` | chat | 0 | cached_input=0.1, cached_input_above_128K=0.3, cached_input_above_256K=0.6, cached_input_above_32K=0.18, input=1.0, input_above_128K=3.0, input_above_256K=6.0, input_above_32K=1.8, output=5.0, output_above_128K=15.0, output_above_256K=60.0, output_above_32K=9.0 | 997952/65536 |
| `qwen3-coder-plus-2025-07-22` | chat | 0 | cached_input=0.1, cached_input_above_128K=0.3, cached_input_above_256K=0.6, cached_input_above_32K=0.18, input=1.0, input_above_128K=3.0, input_above_256K=6.0, input_above_32K=1.8, output=5.0, output_above_128K=15.0, output_above_256K=60.0, output_above_32K=9.0 | 997952/65536 |
| `qwen3-coder-plus-2025-09-23` | chat | 0 | cached_input=0.1, cached_input_above_128K=0.3, cached_input_above_256K=0.6, cached_input_above_32K=0.18, input=1.0, input_above_128K=3.0, input_above_256K=6.0, input_above_32K=1.8, output=5.0, output_above_128K=15.0, output_above_256K=60.0, output_above_32K=9.0 | 997952/65536 |
| `qwen3-max` | chat | 0 | cached_input=0.1, cached_input_above_128K=1.2, cached_input_above_32K=0.6, input=1.2, input_above_128K=3, input_above_32K=2.4, output=6, output_above_128K=15, output_above_32K=12.0 | 997952/65536 |
| `qwen3-max-2025-09-23` | chat | 0 | cached_input=0.1, cached_input_above_128K=1.2, cached_input_above_32K=0.6, input=1.2, input_above_128K=3, input_above_32K=2.4, output=6, output_above_128K=15, output_above_32K=12.0 | 258048/65536 |
| `qwen3-max-2026-01-23` | chat | 0 | cached_input=0.1, cached_input_above_128K=1.2, cached_input_above_32K=0.6, input=1.2, input_above_128K=3, input_above_32K=2.4, output=6, output_above_128K=15, output_above_32K=12.0 | 258048/65536 |
| `qwen3-max-preview` | chat | 0 | cached_input=0.1, cached_input_above_128K=1.2, cached_input_above_32K=0.6, input=1.2, input_above_128K=3, input_above_32K=2.4, output=6, output_above_128K=15, output_above_32K=12.0 | 997952/65536 |
| `qwen3-next-80b-a3b-instruct` | chat | 0 | cached_input=0.072, input=0.144, output=0.574 | 262144/65536 |
| `qwen3-next-80b-a3b-thinking` | chat | 0 | cached_input=0.072, input=0.144, output=1.434 | 262144/65536 |
| `qwen3-rerank` | rerank | 0 | cached_input=0.0035, input=0.1, output=0.0 | 40960/40960 |
| `qwen3-vl-32b-instruct` | chat | 0 | cached_input=0.08, input=0.16, output=0.64 | 126000/32000 |
| `qwen3-vl-flash` | chat | 0 | cached_input=0.01, cached_input_above_128K=0.024, cached_input_above_32K=0.015, input=0.05, input_above_128K=0.12, input_above_32K=0.075, output=0.4, output_above_128K=0.96, output_above_32K=0.6 | 252000/32000 |
| `qwen3-vl-flash-2025-10-15` | chat | 0 | cached_input=0.01, cached_input_above_128K=0.024, cached_input_above_32K=0.015, input=0.05, input_above_128K=0.12, input_above_32K=0.075, output=0.4, output_above_128K=0.96, output_above_32K=0.6 | 252000/32000 |
| `qwen3-vl-flash-2026-01-22` | chat | 0 | cached_input=0.01, cached_input_above_128K=0.024, cached_input_above_32K=0.015, input=0.05, input_above_128K=0.12, input_above_32K=0.075, output=0.4, output_above_128K=0.96, output_above_32K=0.6 | 252000/32000 |
| `qwen3-vl-plus` | chat | 0 | cached_input=0.1, cached_input_above_128K=0.3, cached_input_above_32K=0.15, input=0.2, input_above_128K=0.6, input_above_32K=0.3, output=1.6, output_above_128K=4.8, output_above_32K=2.4 | 252000/32000 |
| `qwen3-vl-plus-2025-12-19` | chat | 0 | cached_input=0.1, cached_input_above_128K=0.3, cached_input_above_32K=0.15, input=0.2, input_above_128K=0.6, input_above_32K=0.3, output=1.6, output_above_128K=4.8, output_above_32K=2.4 | 252000/32000 |
| `qwen3.5-122b-a10b` | chat | 0 | cached_input=0.04, input=0.4, output=3.2 | 252000/64000 |
| `qwen3.5-27b` | chat | 0 | cached_input=0.03, input=0.3, output=2.4 | 252000/64000 |
| `qwen3.5-35b-a3b` | chat | 0 | cached_input=0.12, input=0.25, output=2.0 | 252000/64000 |
| `qwen3.5-397b-a17b` | chat | 0 | cached_input=0.06, input=0.6, output=3.6 | 252000/64000 |
| `qwen3.5-flash` | chat | 0 | cache_creation_input=0.125, cached_input=0.01, input=0.1, output=0.4 | 991000/64000 |
| `qwen3.5-plus` | chat | 0 | cache_creation_input=0.5, cache_creation_input_above_256K=1.5, cached_input=0.04, cached_input_above_256K=0.12, input=0.4, input_above_256K=1.2, output=2.4, output_above_256K=7.2 | 991000/64000 |
| `qwen3.6-27b` | chat | 0 | cached_input=0.06, input=0.6, output=3.6 | 254000/64000 |
| `qwen3.6-35b-a3b` | chat | 0 | cached_input=0.025, input=0.248, output=1.485 | 254000/64000 |
| `qwen3.6-flash` | chat | 0 | cache_creation_input=0.3125, cache_creation_input_above_256K=1.25, cached_input=0.025, cached_input_above_256K=0.1, input=0.25, input_above_256K=1, output=1.5, output_above_128K=4 | 991000/64000 |
| `qwen3.6-max-preview` | chat | 0 | cache_creation_input=1.625, cache_creation_input_above_128K=2.5, cached_input=0.13, cached_input_above_128K=0.2, input=1.3, input_above_128K=2, output=7.8, output_above_128K=12 | 240000/64000 |
| `qwen3.6-plus` | chat | 0 | cache_creation_input=0.625, cache_creation_input_above_256K=2.5, cached_input=0.05, cached_input_above_256K=0.2, input=0.5, input_above_256K=2, output=3, output_above_256K=6 | 991000/64000 |
| `qwen3.7-max` | chat | 0 | cache_creation_input=3.125, cached_input=0.25, input=2.5, output=7.5 | 997952/65536 |
| `qwen3.7-plus` | chat | 0 | cache_creation_input=0.5, cache_creation_input_above_256K=1.5, cached_input=0.04, cached_input_above_256K=0.12, input=0.4, input_above_256K=1.2, output=1.6, output_above_256K=0.12 | 1000000/65536 |
| `qwen3.8-2.4t-a95b` | chat | 1 | cache_creation_input=2.5, cached_input=0.25, input=2.0, output=6.0 | 262144/131072 |
| `qwen3.8-27b` | chat | 0 | cache_creation_input=0.625, cached_input=0.1, input=0.5, output=2.0 | 262144/ |
| `qwen3.8-flash` | chat | 0 | cache_creation_input=0.2, cached_input=0.016, input=0.15, output=0.47 | 991000/128000 |
| `qwen3.8-max` | chat | 1 | cache_creation_input=2.5, cached_input=0.25, input=2.0, output=6.0 | 991000/128000 |
| `qwq-32b` | chat | 0 | cached_input=0.6, input=1.2, output=1.2 | / |
| `qwq-plus` | chat | 0 | cached_input=0.4, input=0.8, output=2.4 | 131072/8192 |
| `qwq-plus-2025-03-05` | chat | 0 | cached_input=0.4, input=0.8, output=2.4 | 131072/8192 |
| `text-embedding-v3` | embedding | 0 | cached_input=0.0035, input=0.07, output=0.07 | 1024/ |
| `text-embedding-v4` | embedding | 0 | cached_input=0.0035, input=0.07, output=0.07 | 1024/ |
| `tongyi-embedding-vision-flash` | embedding | 0 | cached_input=0.0045, image_input=0.03, input=0.09, output=0.09 | 1024/ |
| `tongyi-embedding-vision-plus` | embedding | 0 | cached_input=0.0045, image_input=0.03, input=0.09, output=0.09 | 1024/ |
| `wan2.2-t2i-flash` | image_generation | 1 | cached_input=0.0, input=0.0, output=25.0, output_cost_per_image=0.025 | / |
| `wan2.2-t2i-plus` | image_generation | 1 | cached_input=0.0, input=0.0, output=50.0, output_cost_per_image=0.05 | / |
| `z-image-turbo` | image_generation | 1 | cached_input=0.0, input=0.0, output=15.0, output_cost_per_image=0.015, output_cost_per_image_standard=0.015, output_cost_per_image_thinking=0.03 | / |
| `anthropic.claude-haiku-4-5-20251001-v1:0` | chat | 0 | cache_creation_input=1.25, cached_input=0.5, input=1.0, output=5.0 | 200000/64000 |
| `anthropic.claude-opus-4-6-v1` | chat | 1 | cache_creation_input=6.25, cached_input=1.5, input=5.0, output=25.0 | 1000000/128000 |
| `anthropic.claude-opus-4-7` | chat | 1 | cache_creation_input=6.25, cached_input=0.5, input=5.0, output=25.0 | 1000000/128000 |
| `anthropic.claude-opus-4-8` | chat | 1 | cache_creation_input=6.25, cached_input=0.5, input=5.0, output=25.0 | 1000000/128000 |
| `anthropic.claude-sonnet-4-5-20250929-v1:0` | chat | 1 | cache_creation_input=3.75, cached_input=1.5, input=3.0, output=15.0 | 200000/64000 |
| `anthropic.claude-sonnet-4-6` | chat | 1 | cache_creation_input=3.75, cached_input=1.5, input=3.0, output=15.0 | 1000000/64000 |
| `claude-fable-5` | chat | 1 | cache_creation_input=12.5, cached_input=1.0, input=10.0, output=50.0 | 1000000/128000 |
| `claude-fable-5-1` | chat | 2 | cache_creation_input=12.5, cached_input=0.25, input=10.0, output=50.0 | 1000000/128000 |
| `claude-haiku-4-5` | chat | 0 | cache_creation_input=1.25, cached_input=0.5, input=1.0, output=5.0 | 200000/64000 |
| `claude-opus-4-5` | chat | 1 | cache_creation_input=6.25, cached_input=1.5, input=5.0, output=25.0 | 200000/64000 |
| `claude-opus-4-6` | chat | 1 | cache_creation_input=6.25, cached_input=1.5, input=5.0, output=25.0 | 1000000/128000 |
| `claude-opus-4-7` | chat | 1 | cache_creation_input=6.25, cached_input=0.5, input=5.0, output=25.0 | 1000000/128000 |
| `claude-opus-4-8` | chat | 1 | cache_creation_input=6.25, cached_input=0.5, input=5.0, output=25.0 | 1000000/128000 |
| `claude-opus-5` | chat | 1 | cache_creation_input=6.25, cached_input=0.5, input=5.0, output=25.0 | 1000000/128000 |
| `claude-opus-5-5` | chat | 1 | cache_creation_input=8.0, cached_input=0.2, input=4.0, output=20.0 | 1000000/128000 |
| `claude-sonnet-4-5` | chat | 1 | cache_creation_input=3.75, cached_input=1.5, input=3.0, output=15.0 | 1000000/64000 |
| `claude-sonnet-4-6` | chat | 1 | cache_creation_input=3.75, cached_input=1.5, input=3.0, output=15.0 | 1000000/128000 |
| `claude-sonnet-5` | chat | 1 | cache_creation_input=6.0, cached_input=0.3, input=3.0, output=15.0 | 1000000/128000 |
| `claude-sonnet-5-5` | chat | 1 | cache_creation_input=4.0, cached_input=0.2, input=2.0, output=10.0 | 1000000/128000 |
| `seedream-4-5-251128` | image_generation | 5 | cached_input=0.0, input=0.0, output=40.0, output_cost_per_image=0.04 | / |
| `seedream-5-0-260128` | image_generation | 1 | cached_input=0.0, input=0.0, output=35.0, output_cost_per_image=0.035 | / |
| `cohere-rerank-v4.0-fast` | rerank | 0 | input=0.0, input_cost_per_query=0.002, output=0.0 | 32768/32768 |
| `cohere-rerank-v4.0-pro` | rerank | 0 | input=0.0, input_cost_per_query=0.0025, output=0.0 | 32768/32768 |
| `cohere.embed-multilingual-v3` | embedding | 0 | cached_input=0.05, input=0.1, output=0.0 | 512/ |
| `cohere.embed-v4:0` | embedding | 0 | cached_input=0.06, input=0.12, output=0.0 | 128000/ |
| `cohere.rerank-v3-5:0` | rerank | 0 | input=0.0, input_cost_per_query=0.002, output=0.0 | 32000/32000 |
| `embed-v-4-0` | embedding | 0 | image_input=0.47, input=0.12, output=0.0 | 128000/ |
| `dataforseo-search` | search | 0 | input=0.0, input_cost_per_query=0.002, output=0.0, tiered_pricing=[{'input_cost_per_query': 0.002, 'max_results_range': [0, 10]}, {'input_cost_per_query': 0.0035, 'max_results_range': [11, 20]}, {'input_cost_per_query': 0.005, 'max_results_range': [21, 30]}, {'input_cost_per_query': 0.0065, 'max_results_range': [31, 40]}, {'input_cost_per_query': 0.007, 'max_results_range': [41, 50]}, {'input_cost_per_query': 0.0155, 'max_results_range': [51, 100]}] | / |
| `cf.deepseek-r1-distill-qwen-32b` | chat | 0 | cached_input=0.25, input=0.497, output=4.881 | / |
| `deepseek-chat` | chat | 0 | cached_input=0.007, input=0.22, output=0.66 | 131072/8192 |
| `deepseek-coder` | chat | 0 | cached_input=0.007, input=0.22, output=0.66 | 128000/4096 |
| `deepseek-flash` | chat | 0 | cached_input=0.003, input=0.15, output=0.6 | 1000000/393216 |
| `deepseek-reasoner` | chat | 0 | cached_input=0.022, input=0.66, output=1.98 | 131072/65536 |
| `deepseek-v3.1` | chat | 0 | cached_input=0.022, input=0.66, output=1.98 | 163840/163840 |
| `deepseek-v3.2` | chat | 0 | cached_input=0.007, input=0.22, output=0.66 | 163840/163840 |
| `deepseek-v3.2-speciale` | chat | 0 | cached_input=0.007, input=0.22, output=0.66 | 163840/163840 |
| `deepseek-v4-flash` | chat | 0 | cached_input=0.007, input=0.22, output=0.66 | 1000000/393216 |
| `deepseek-v4-pro` | chat | 0 | cached_input=0.022, input=0.66, output=1.98 | 1000000/393216 |
| `deepseek-v4.1-flash` | chat | 0 | cached_input=0.003, input=0.15, output=0.6 | 1000000/393216 |
| `eleven_flash_v2` | audio_speech | 0 | cached_input=0.0, input=0.0, output=0.0, output_cost_per_second=0.0025 | / |
| `eleven_flash_v2_5` | audio_speech | 0 | cached_input=0.0, input=0.0, output=0.0, output_cost_per_second=0.0025 | / |
| `eleven_multilingual_v2` | audio_speech | 0 | cached_input=0.0, input=0.0, input_cost_per_character=0.0, output=0.0, output_cost_per_second=0.005 | / |
| `eleven_turbo_v2` | audio_speech | 0 | cached_input=0.0, input=0.0, output=0.0, output_cost_per_second=0.0025 | / |
| `eleven_turbo_v2_5` | audio_speech | 0 | cached_input=0.0, input=0.0, output=0.0, output_cost_per_second=0.0025 | / |
| `eleven_v3` | audio_speech | 0 | cached_input=0.0, input=0.0, input_cost_per_character=0.0, output=0.0, output_cost_per_second=0.0014 | / |
| `eleven_v4` | audio_speech | 0 | cached_input=0.0, input=0.0, input_cost_per_character=0.0, output=0.0, output_cost_per_second=0.0014 | / |
| `eleven_v4_turbo` | audio_speech | 0 | cached_input=0.0, input=0.0, input_cost_per_character=0.0, output=0.0, output_cost_per_second=0.0007 | / |
| `scribe_v1` | audio_transcription | 0 | cached_input=0.0, input=0.0, input_cost_per_second=9.722e-05, output=0.0 | / |
| `scribe_v2` | audio_transcription | 0 | cached_input=0.0, input=0.0, input_cost_per_second=9.722e-05, output=0.0 | / |
| `exa_ai-search` | search | 0 | input=0.0, input_cost_per_query=0.025, output=0.0, tiered_pricing=[{'input_cost_per_query': 0.005, 'max_results_range': [0, 25]}, {'input_cost_per_query': 0.025, 'max_results_range': [26, 100]}] | / |
| `firecrawl-search` | search | 0 | input=0.0, input_cost_per_credit=0.00083, input_cost_per_query=0.00166, output=0.0, tiered_pricing=[{'input_cost_per_query': 0.00166, 'max_results_range': [1, 10]}, {'input_cost_per_query': 0.00332, 'max_results_range': [11, 20]}, {'input_cost_per_query': 0.00498, 'max_results_range': [21, 30]}, {'input_cost_per_query': 0.00664, 'max_results_range': [31, 40]}, {'input_cost_per_query': 0.0083, 'max_results_range': [41, 50]}, {'input_cost_per_query': 0.00996, 'max_results_range': [51, 60]}, {'input_cost_per_query': 0.01162, 'max_results_range': [61, 70]}, {'input_cost_per_query': 0.01328, 'max_results_range': [71, 80]}, {'input_cost_per_query': 0.01494, 'max_results_range': [81, 90]}, {'input_cost_per_query': 0.0166, 'max_results_range': [91, 100]}] | / |
| `cf.embeddinggemma-300m` | embedding | 0 | cached_input=0.0, input=0.012, output=0.0 | 2048/2048 |
| `cf.gemma-4-26b-a4b-it` | chat | 0 | cached_input=0.01, input=0.1, output=0.3 | 262144/131072 |
| `cf.gemma-sea-lion-v4-27b-it` | chat | 0 | cached_input=0.165, input=0.35, output=0.46 | / |
| `cf.glm-5.2` | chat | 0 | cached_input=0.26, input=1.4, output=4.4 | 991000/128000 |
| `cf.kimi-k2.7-code` | chat | 0 | cached_input=0.19, input=0.95, output=4.0, search_context_cost_per_query={'low': 0.005, 'medium': 0.005, 'high': 0.01} | 262144/262144 |
| `gemini-2.5-flash` | chat | 0 | audio_cached_input=0.25, audio_input=1.0, audio_output=1.0, cached_input=0.15, input=0.3, output=2.5 | 1048576/65535 |
| `gemini-2.5-flash-image` | image_generation | 1 | cached_input=0.15, image_input=0.3, image_output=30.0, input=0.3, output=2.5, output_cost_per_image=0.04 | 32768/32768 |
| `gemini-2.5-flash-lite` | chat | 0 | audio_cached_input=0.05, audio_input=0.1, audio_output=0.4, cached_input=0.05, input=0.1, output=0.4 | 1048576/65535 |
| `gemini-2.5-flash-preview-tts` | audio_speech | 0 | audio_output=10.0, cached_input=0.25, input=0.5, output=10.0 | 8192/16384 |
| `gemini-2.5-flash-tts` | chat | 0 | audio_output=10.0, cached_input=0.25, input=0.5, output=10.0 | 1048576/65535 |
| `gemini-2.5-pro` | chat | 1 | audio_cached_input=1.5, audio_input=1.25, audio_input_above_200k=2.5, audio_output=10.0, audio_output_above_200k=15.0, cached_input=0.625, input=1.25, input_above_200k=2.5, output=10.0, output_above_200k=15.0 | 1048576/65535 |
| `gemini-2.5-pro-preview-tts` | chat | 1 | audio_output=20.0, cached_input=0.5, input=1.0, output=20.0 | 1048576/65535 |
| `gemini-2.5-pro-tts` | chat | 1 | audio_output=20.0, cached_input=0.5, input=1.0, output=20.0 | 1048576/65535 |
| `gemini-3-flash-preview` | chat | 0 | audio_cached_input=0.5, audio_input=1.5, audio_output=1.5, cached_input=0.25, input=0.5, output=3.0 | 1048576/65535 |
| `gemini-3-pro-image` | image_generation | 1 | cached_input=0.5, image_input=2.0, image_output=120.0, input=2.0, output=12.0, output_cost_per_image=0.134, output_cost_per_image_4096x4096=0.24 | 65536/32768 |
| `gemini-3-pro-image-preview` | image_generation | 1 | cached_input=0.5, image_input=2.0, image_output=120.0, input=2.0, output=12.0, output_cost_per_image=0.134, output_cost_per_image_4096x4096=0.24 | 65536/32768 |
| `gemini-3.1-flash-image` | image_generation | 1 | cached_input=0.25, image_input=0.5, image_output=60.0, input=0.5, output=3.0, output_cost_per_image=0.0672, output_cost_per_image_2048x2048=0.101, output_cost_per_image_4096x4096=0.151 | 65536/32768 |
| `gemini-3.1-flash-image-preview` | image_generation | 1 | cached_input=0.25, image_input=0.5, image_output=60.0, input=0.5, output=3.0, output_cost_per_image=0.0672, output_cost_per_image_2048x2048=0.101, output_cost_per_image_4096x4096=0.151 | 65536/32768 |
| `gemini-3.1-flash-lite` | chat | 0 | audio_cached_input=0.05, audio_input=0.5, audio_output=1.5, cached_input=0.025, input=0.25, output=1.5 | 1048576/65536 |
| `gemini-3.1-flash-lite-image` | image_generation | 1 | cached_input=0.05, image_input=0.25, image_output=30.0, input=0.25, output=1.5, output_cost_per_image=0.0336, output_cost_per_image_2048x2048=0.0672, output_cost_per_image_4096x4096=0.1344 | 65536/4096 |
| `gemini-3.1-flash-lite-preview` | chat | 0 | audio_cached_input=0.05, audio_input=0.5, audio_output=1.5, cached_input=0.025, input=0.25, output=1.5 | 1048576/65536 |
| `gemini-3.1-flash-tts-preview` | audio_speech | 1 | audio_output=20.0, cached_input=0.5, input=1.0, output=20.0 | 8192/16384 |
| `gemini-3.1-pro-preview` | chat | 1 | audio_cached_input=1.5, audio_input=7.0, audio_output=7.0, cached_input=0.825, input=2.0, input_above_200k=4.0, output=12.0, output_above_200k=18.0 | 1048576/65536 |
| `gemini-3.5-flash` | chat | 0 | audio_cached_input=0.5, audio_input=1, audio_output=1, cached_input=0.25, input=1.5, output=9.0 | 1048576/65535 |
| `gemini-3.5-flash-lite` | chat | 0 | cached_input=0.03, input=0.3, output=2.5 | 1048576/65536 |
| `gemini-3.6-flash` | chat | 0 | cached_input=0.15, input=1.5, output=7.5 | 1048576/65536 |
| `gemini-3.7-flash` | chat | 0 | cached_input=0.075, input=0.75, output=3.75 | 1048576/65536 |
| `gemini-3.8-flash` | chat | 0 | cached_input=0.075, input=0.75, output=3.75 | 1048576/65536 |
| `gemini-3.8-flash-lite-tts` | audio_speech | 0 | audio_output=6.0, cached_input=0.125, input=0.5, output=6.0 | 8192/16384 |
| `gemini-3.8-flash-tts` | audio_speech | 0 | audio_output=9.0, cached_input=0.125, input=0.5, output=9.0 | 8192/16384 |
| `gemini-embedding-001` | embedding | 0 | cached_input=0.075, input=0.15, output=0.15 | 2048/ |
| `gemini-embedding-2` | embedding | 0 | audio_input=6.5, cached_input=0.02, image_input=0.45, input=0.2, output=0.15, video_input=12.0 | 8192/ |
| `gemini-flash-latest` | chat | 0 | cached_input=0.075, input=0.75, output=3.75 | 1048576/65536 |
| `gemini-flash-lite-latest` | chat | 0 | audio_cached_input=0.05, audio_input=0.5, audio_output=1.5, cached_input=0.03, input=0.3, output=2.5 | 1048576/65536 |
| `gemini-robotics-er-1.5-preview` | chat | 0 | audio_cached_input=0.25, audio_input=1.0, cached_input=0.15, input=0.3, output=2.5 | 1048576/65535 |
| `gemma-4-26b-a4b-it` | chat | 0 | cached_input=0.013, input=0.13, output=0.4 | 262144/262144 |
| `gemma-4-31b-it` | chat | 0 | cached_input=0.014, input=0.14, output=0.4 | 262144/131072 |
| `mistral-small-2503` | chat | 0 | cached_input=0.05, input=0.1, input_cost_per_annotation_page=0.005, input_cost_per_page=0.004, output=0.3 | 128000/128000 |
| `semantic-ranker-default-004` | rerank | 0 | input=0.0, input_cost_per_query=0.001, output=0.0 | 1024/1024 |
| `semantic-ranker-fast-004` | rerank | 0 | input=0.0, input_cost_per_query=0.001, output=0.0 | 1024/1024 |
| `veo-3.1-fast-generate-001` | video_generation | 1 | output_cost_per_video_per_second=0.15 | 1024/ |
| `veo-3.1-fast-generate-preview` | video_generation | 1 | output_cost_per_video_per_second=0.15 | 1024/ |
| `veo-3.1-generate-001` | video_generation | 1 | output_cost_per_video_per_second=0.4 | 1024/ |
| `veo-3.1-generate-preview` | video_generation | 1 | output_cost_per_video_per_second=0.4 | 1024/ |
| `cf.granite-4.0-h-micro` | chat | 0 | cached_input=0.008, input=0.017, output=0.11 | 131072/32768 |
| `cf.llama-3.1-8b-instruct-fast` | chat | 0 | cached_input=0.022, input=0.045, output=0.384 | / |
| `cf.llama-3.2-1b-instruct` | chat | 0 | cached_input=0.014, input=0.027, output=0.201 | / |
| `cf.llama-3.2-3b-instruct` | chat | 0 | cached_input=0.025, input=0.051, output=0.335 | / |
| `cf.llama-3.3-70b-instruct-fp8-fast` | chat | 0 | cached_input=0.15, input=0.29, output=2.25 | / |
| `cf.llama-4-scout-17b-16e-instruct` | chat | 0 | cached_input=0.14, input=0.27, output=0.85 | 10000000/16384 |
| `cf.llama-guard-3-8b` | moderation | 0 | cached_input=0.242, input=0.484, output=0.03 | / |
| `groq.llama-4-maverick-17b-128e-instruct` | chat | 0 | cached_input=0.1, input=0.2, output=0.6 | 131072/8192 |
| `groq.llama-4-scout-17b-16e-instruct` | chat | 0 | cached_input=0.055, input=0.11, output=0.34 | 131072/8192 |
| `groq.llama-guard-4-12b` | chat | 0 | cached_input=0.1, input=0.2, output=0.2 | 128000/1024 |
| `groq.llama-prompt-guard-2-22m` | chat | 0 | cached_input=0.015, input=0.03, output=0.03 | 512/512 |
| `groq.llama-prompt-guard-2-86m` | chat | 0 | cached_input=0.02, input=0.04, output=0.04 | 512/512 |
| `llama-4-maverick-17b-128e-instruct-fp8` | chat | 1 | cached_input=0.14, input=0.27, output=0.85 | 1000000/16384 |
| `llama-4-scout-17b-16e-instruct` | chat | 0 | cached_input=0.09, input=0.18, output=0.59 | 10000000/16384 |
| `minimax-m2.5` | chat | 0 | cache_creation_input=0.375, cached_input=0.03, input=0.3, output=1.2 | 1000000/8192 |
| `minimax-m2.5-lightning` | chat | 0 | cache_creation_input=0.375, cached_input=0.03, input=0.3, output=2.4 | 1000000/8192 |
| `minimax-m2.7` | chat | 0 | cache_creation_input=0.375, cached_input=0.06, input=0.3, output=1.2 | 204800/131072 |
| `minimax-m2.7-highspeed` | chat | 0 | cache_creation_input=0.375, cached_input=0.06, input=0.6, output=2.4 | 204800/131072 |
| `minimax-m3` | chat | 0 | cached_input=0.06, cached_input_above_512K=0.12, input=0.3, input_above_512K=0.6, output=1.2, output_above_512K=2.4 | 512000/128000 |
| `cf.mistral-small-3.1-24b-instruct` | chat | 0 | cached_input=0.175, input=0.351, output=0.555 | / |
| `mistral-large-3` | chat | 0 | cached_input=0.05, input=0.5, input_cost_per_annotation_page=0.005, input_cost_per_page=0.004, output=1.5 | / |
| `mistral-ocr-2512` | ocr | 0 | input_cost_per_annotation_page=0.005, input_cost_per_page=0.002 | / |
| `mistral-ocr-4-0` | ocr | 0 | input_cost_per_annotation_page=0.005, input_cost_per_page=0.004 | / |
| `mistral-ocr-latest` | ocr | 0 | input_cost_per_annotation_page=0.005, input_cost_per_page=0.004 | / |
| `groq.kimi-k2-instruct-0905` | chat | 0 | cached_input=0.5, input=1.0, output=0.34 | 262144/16384 |
| `kimi-k2.5` | chat | 0 | cached_input=0.1, input=0.6, output=3.0, search_context_cost_per_query={'low': 0.005, 'medium': 0.005, 'high': 0.01} | 262144/262144 |
| `kimi-k2.6` | chat | 0 | cached_input=0.16, input=0.95, output=4.0, search_context_cost_per_query={'low': 0.005, 'medium': 0.005, 'high': 0.01} | 262144/262144 |
| `kimi-k2.7-code` | chat | 0 | cached_input=0.19, input=0.95, output=4.0, search_context_cost_per_query={'low': 0.005, 'medium': 0.005, 'high': 0.01} | 262144/262144 |
| `kimi-k2.7-code-highspeed` | chat | 0 | cached_input=0.38, input=1.9, output=8.0, search_context_cost_per_query={'low': 0.005, 'medium': 0.005, 'high': 0.01} | 262144/262144 |
| `kimi-k3` | chat | 0 | cached_input=0.3, input=3.0, output=15.0, search_context_cost_per_query={'low': 0.005, 'medium': 0.005, 'high': 0.01} | 262144/262144 |
| `kimi-latest` | None | 0 | cached_input=0.3, input=3.0, output=15.0, search_context_cost_per_query={'low': 0.005, 'medium': 0.005, 'high': 0.01} | / |
| `muse-glimmer-30b` | chat | 0 | cached_input=0.04, input=0.35, output=1.5 | 131072/ |
| `nemotron-3-ultra` | chat | 0 | cached_input=0.12, input=0.6, output=2.4 | 254000/64000 |
| `nemotron-3.5-lightning` | chat | 0 | cached_input=0.01, input=0.05, output=0.2 | 262144/ |
| `nvidia_nim.llama-3.3-nemotron-super-49b-v1.5` | chat | 0 | cached_input=0.001, input=0.01, output=0.03 | / |
| `nvidia_nim.nemotron-nano-12b-v2-vl` | chat | 0 | cached_input=0.001, input=0.01, output=0.06 | / |
| `nvidia_nim.nemotron-parse` | chat | 0 | cached_input=0.001, input=0.01, output=0.06 | / |
| `nvidia_nim.nv-embed-v1` | embedding | 0 | cached_input=0.001, input=0.002, output=0.002 | / |
| `nvidia_nim.nv-embedqa-e5-v5` | embedding | 0 | cached_input=0.001, input=0.002, output=0.002 | / |
| `cf.gpt-oss-120b` | chat | 0 | cached_input=0.175, input=0.35, output=0.75 | 131072/32768 |
| `cf.gpt-oss-20b` | chat | 0 | cached_input=0.1, input=0.2, output=0.3 | 131072/32768 |
| `cf.nemotron-3-120b-a12b` | chat | 0 | cached_input=0.05, input=0.5, output=1.5 | 256000/256000 |
| `codex-auto-review` | chat | 0 | cache_creation_input=2.5, cache_creation_input_above_272K=5.0, cached_input=0.2, cached_input_above_272K=0.4, input=2.0, input_above_272K=4.0, output=12.0, output_above_272K=18.0 | 1050000/128000 |
| `gpt-4.1` | chat | 0 | cached_input=0.5, input=2.0, output=8.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 1047576/32768 |
| `gpt-4.1-2025-04-14` | chat | 0 | cached_input=0.5, input=2.0, output=8.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 1047576/32768 |
| `gpt-4.1-mini` | chat | 0 | cached_input=0.1, input=0.4, output=1.6, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 1047576/32768 |
| `gpt-4.1-mini-2025-04-14` | chat | 0 | cached_input=0.1, input=0.4, output=1.6, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 1047576/32768 |
| `gpt-4.1-nano` | chat | 0 | cached_input=0.025, input=0.1, output=0.4 | 1047576/32768 |
| `gpt-4.1-nano-2025-04-14` | chat | 0 | cached_input=0.025, input=0.1, output=0.4 | 1047576/32768 |
| `gpt-4o` | chat | 0 | cached_input=1.25, input=2.5, output=10.0 | 128000/16384 |
| `gpt-4o-2024-05-13` | chat | 1 | cached_input=1.25, input=5.0, output=15.0 | 128000/4096 |
| `gpt-4o-2024-08-06` | chat | 1 | cached_input=1.25, input=2.5, output=10.0 | 128000/16384 |
| `gpt-4o-2024-11-20` | chat | 1 | cached_input=1.25, input=2.5, output=10.0 | 128000/16384 |
| `gpt-4o-mini` | chat | 0 | cached_input=0.075, input=0.15, output=0.6 | 128000/16384 |
| `gpt-4o-mini-2024-07-18` | chat | 0 | cached_input=0.075, input=0.15, output=0.6 | 128000/16384 |
| `gpt-4o-mini-transcribe` | audio_transcription | 0 | audio_input=3.0, cached_input=0.75, input=1.25, input_cost_per_second=5e-05, output=5.0 | 16000/2000 |
| `gpt-4o-transcribe` | audio_transcription | 0 | audio_input=6.0, cached_input=1.5, input=2.5, input_cost_per_second=0.0001, output=10.0 | 16000/2000 |
| `gpt-4o-transcribe-diarize` | audio_transcription | 0 | audio_input=6.0, cached_input=1.5, input=2.5, input_cost_per_second=0.0001, output=10.0 | 16000/2000 |
| `gpt-5` | chat | 1 | cached_input=0.125, input=1.25, output=10.0 | 272000/128000 |
| `gpt-5-2025-08-07` | chat | 1 | cached_input=0.125, input=1.25, output=10.0 | 272000/128000 |
| `gpt-5-mini` | chat | 0 | cached_input=0.025, input=0.25, output=2.0 | 272000/128000 |
| `gpt-5-mini-2025-08-07` | chat | 0 | cached_input=0.025, input=0.25, output=2.0 | 272000/128000 |
| `gpt-5-nano` | chat | 0 | cached_input=0.005, input=0.05, output=0.4 | 272000/128000 |
| `gpt-5-nano-2025-08-07` | chat | 0 | cached_input=0.005, input=0.05, output=0.4 | 272000/128000 |
| `gpt-5-pro` | responses | 2 | cached_input=1.5, input=15.0, output=120.0 | 400000/272000 |
| `gpt-5-pro-2025-10-06` | responses | 2 | cached_input=1.5, input=15.0, output=120.0 | 400000/272000 |
| `gpt-5.1` | chat | 0 | cached_input=0.125, input=1.25, output=10.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 272000/128000 |
| `gpt-5.1-2025-11-13` | chat | 1 | cached_input=0.125, input=1.25, output=10.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 272000/128000 |
| `gpt-5.1-codex-max` | responses | 0 | cached_input=0.125, input=1.25, output=10.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 400000/128000 |
| `gpt-5.2` | chat | 0 | cached_input=0.175, input=1.75, output=14.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 272000/128000 |
| `gpt-5.2-2025-12-11` | chat | 0 | cached_input=0.175, input=1.75, output=14.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 272000/128000 |
| `gpt-5.2-pro` | responses | 3 | cached_input=2.1, input=21.0, output=168.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 272000/128000 |
| `gpt-5.2-pro-2025-12-11` | responses | 3 | cached_input=2.1, input=21.0, output=168.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 272000/128000 |
| `gpt-5.3-codex` | responses | 0 | cached_input=0.175, input=1.75, output=14.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 272000/128000 |
| `gpt-5.4` | chat | 0 | cached_input=0.25, cached_input_above_272K=0.5, input=2.5, input_above_272K=5.0, output=15.0, output_above_272K=22.5, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 1050000/128000 |
| `gpt-5.4-mini` | chat | 0 | cached_input=0.075, input=0.75, output=4.5, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 272000/128000 |
| `gpt-5.4-nano` | chat | 0 | cached_input=0.02, input=0.2, output=1.25, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 272000/128000 |
| `gpt-5.4-pro` | responses | 2 | input=30.0, input_above_272K=60.0, output=180.0, output_above_272K=270.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 1050000/128000 |
| `gpt-5.5` | chat | 0 | cached_input=0.5, cached_input_above_272K=1.0, input=5.0, input_above_272K=10.0, output=30.0, output_above_272K=45.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 1050000/128000 |
| `gpt-5.6-luna` | chat | 0 | cached_input=0.02, cached_input_above_272K=0.04, input=0.2, input_above_272K=0.4, output=1.2, output_above_272K=1.8, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 922000/128000 |
| `gpt-5.6-sol` | chat | 0 | cache_creation_input=2.5, cache_creation_input_above_272K=12.5, cached_input=0.5, cached_input_above_272K=1.0, input=5.0, input_above_272K=10.0, output=12.0, output_above_272K=45.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 922000/128000 |
| `gpt-5.6-terra` | chat | 0 | cache_creation_input=2.5, cache_creation_input_above_272K=5.0, cached_input=0.2, cached_input_above_272K=0.4, input=2.0, input_above_272K=4.0, output=12.0, output_above_272K=18.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 922000/128000 |
| `gpt-6-astra` | chat | 1 | cache_creation_input=12.5, cache_creation_input_above_272K=25.0, cached_input=1.0, cached_input_above_272K=2.0, input=10.0, input_above_272K=20.0, output=50.0, output_above_272K=75.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 922000/128000 |
| `gpt-6-luna` | chat | 0 | cache_creation_input=0.125, cache_creation_input_above_272K=0.25, cached_input=0.01, cached_input_above_272K=0.02, input=0.1, input_above_272K=0.2, output=0.5, output_above_272K=0.75, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 922000/128000 |
| `gpt-6-sol` | chat | 0 | cache_creation_input=2.5, cache_creation_input_above_272K=5.0, cached_input=0.2, cached_input_above_272K=0.4, input=2.0, input_above_272K=4.0, output=10.0, output_above_272K=15.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 922000/128000 |
| `gpt-6.1-sol` | chat | 1 | cache_creation_input=2.5, cache_creation_input_above_272K=5.0, cached_input=0.1, cached_input_above_272K=0.2, input=2.0, input_above_272K=4.0, output=10.0, output_above_272K=15.0, search_context_cost_per_query={'low': 0.03, 'medium': 0.035, 'high': 0.05} | 922000/128000 |
| `gpt-audio` | chat | 1 | audio_input=32.0, audio_output=64.0, cached_input=1.25, input=2.5, output=10.0 | 128000/16384 |
| `gpt-audio-1.5` | chat | 1 | audio_input=32.0, audio_output=64.0, cached_input=1.25, input=2.5, output=10.0 | 128000/16384 |
| `gpt-audio-2025-08-28` | chat | 1 | audio_input=32.0, audio_output=64.0, cached_input=1.25, input=2.5, output=10.0 | 128000/16384 |
| `gpt-audio-mini` | chat | 0 | audio_input=10.0, audio_output=20.0, cached_input=0.3, input=0.6, output=2.4 | 128000/16384 |
| `gpt-audio-mini-2025-10-06` | None | 0 | audio_input=10.0, audio_output=20.0, cached_input=0.3, input=0.6, output=2.4 | / |
| `gpt-image-1` | image_generation | 1 | cached_input=1.25, image_cached_input=2.5, image_input=10.0, image_output=40.0, input=5.0, output=20.0 | / |
| `gpt-image-1-mini` | image_generation | 1 | cached_input=0.5, image_cached_input=0.625, image_input=2.5, image_output=8.0, input=2.0, output=4.0 | / |
| `gpt-image-1.5` | image_generation | 1 | cached_input=1.25, image_cached_input=2.0, image_input=8.0, image_output=32.0, input=5.0, output=10.0 | / |
| `gpt-image-2` | image_generation | 1 | cached_input=1.25, image_cached_input=2.0, image_input=8.0, image_output=30.0, input=5.0, output=10.0 | / |
| `gpt-image-2.5-flare` | image_generation | 1 | cached_input=1.25, image_cached_input=2.0, image_input=8.0, image_output=30.0, input=5.0, output=0.0 | / |
| `gpt-image-2.5-sunburst` | image_generation | 1 | cached_input=1.25, image_cached_input=2.0, image_input=8.0, image_output=30.0, input=5.0, output=0.0 | / |
| `gpt-oss-120b` | chat | 0 | cached_input=0.15, input=0.3, output=2.5 | 128000/128000 |
| `groq.gpt-oss-120b` | chat | 0 | cached_input=0.075, input=0.15, output=0.75 | 131072/32766 |
| `groq.gpt-oss-20b` | chat | 0 | cached_input=0.0375, input=0.075, output=0.3 | 131072/32768 |
| `groq.gpt-oss-safeguard-20b` | chat | 0 | cached_input=0.0375, input=0.075, output=0.3 | 131072/65536 |
| `groq.whisper-large-v3` | audio_transcription | 0 | cached_input=0.0, input=0.0, input_cost_per_second=3.1e-05, output=0.00185 | / |
| `groq.whisper-large-v3-turbo` | audio_transcription | 0 | cached_input=0.0, input=0.0, input_cost_per_second=1.111e-05, output=6.7e-05 | / |
| `nvidia_nim.gpt-oss-120b` | chat | 0 | cached_input=0.015, input=0.03, output=0.25 | / |
| `nvidia_nim.gpt-oss-20b` | chat | 0 | cached_input=0.001, input=0.007, output=0.03 | / |
| `o1` | chat | 2 | cached_input=7.5, input=15.0, output=60.0 | 200000/100000 |
| `o1-2024-12-17` | chat | 2 | cached_input=7.5, input=15.0, output=60.0 | 200000/100000 |
| `o1-pro` | responses | 4 | cached_input=75.0, input=150.0, output=600.0 | 200000/100000 |
| `o1-pro-2025-03-19` | responses | 4 | cached_input=75.0, input=150.0, output=600.0 | 200000/100000 |
| `o3` | chat | 2 | cached_input=0.5, input=2.0, output=8.0 | 200000/100000 |
| `o3-2025-04-16` | chat | 2 | cached_input=0.5, input=2.0, output=8.0 | 200000/100000 |
| `o3-mini` | chat | 2 | cached_input=0.55, input=1.1, output=4.4 | 200000/100000 |
| `o3-mini-2025-01-31` | chat | 2 | cached_input=0.55, input=1.1, output=4.4 | 200000/100000 |
| `o3-pro` | responses | 1 | cached_input=10.0, input=20.0, output=80.0 | 200000/100000 |
| `o3-pro-2025-06-10` | responses | 1 | cached_input=10.0, input=20.0, output=80.0 | 200000/100000 |
| `o4-mini` | chat | 1 | cached_input=0.55, input=1.1, output=4.4 | 200000/100000 |
| `o4-mini-2025-04-16` | chat | 1 | cached_input=0.55, input=1.1, output=4.4 | 200000/100000 |
| `omni-moderation-2024-09-26` | moderation | 0 | cached_input=0.0, input=0.0, output=0.0 | 32768/0 |
| `omni-moderation-latest` | moderation | 0 | cached_input=0.0, input=0.0, output=0.0 | 32768/0 |
| `text-embedding-3-large` | embedding | 0 | cached_input=0.06, input=0.13, output=0.13 | 8191/ |
| `text-embedding-3-small` | embedding | 0 | cached_input=0.01, input=0.02, output=0.02 | 8191/ |
| `text-embedding-ada-002` | embedding | 0 | cached_input=0.05, input=0.1, output=0.05 | 8191/ |
| `text-moderation-latest` | None | 2 | cached_input=0.0, input=0.0, output=0.0 | / |
| `text-moderation-stable` | None | 2 | cached_input=0.0, input=0.0, output=0.0 | / |
| `tts-1` | audio_speech | 0 | cached_input=0.0, input=15.0, input_cost_per_character=1.5e-05, output=0.0 | / |
| `tts-1-hd` | audio_speech | 1 | cached_input=0.0, input=30.0, input_cost_per_character=3e-05, output=0.0 | / |
| `whisper-1` | audio_transcription | 0 | cached_input=0.0, input=0.0, input_cost_per_second=0.0001, output=0.006 | / |
| `parallel_ai-search` | search | 0 | input=0.0, input_cost_per_query=0.004, output=0.0 | / |
| `parallel_ai-search-pro` | search | 0 | input=0.0, input_cost_per_query=0.009, output=0.0 | / |
| `perplexity-search` | search | 0 | input=0.0, input_cost_per_query=0.005, output=0.0 | / |
| `sonar` | chat | 0 | cached_input=0.5, input=1.0, output=1.0, search_context_cost_per_query={'high': 0.012, 'low': 0.005, 'medium': 0.008} | 128000/ |
| `sonar-deep-research` | chat | 0 | cached_input=1.0, citation=2.0, input=2.0, output=8.0, output_reasoning=3.0, search_context_cost_per_query={'high': 0.005, 'low': 0.005, 'medium': 0.005} | 128000/ |
| `sonar-pro` | chat | 0 | cached_input=1.5, input=3.0, output=15.0, search_context_cost_per_query={'high': 0.014, 'low': 0.006, 'medium': 0.01} | 200000/8000 |
| `sonar-reasoning` | chat | 0 | cached_input=0.5, input=1.0, output=5.0, search_context_cost_per_query={'high': 0.014, 'low': 0.005, 'medium': 0.008} | 128000/ |
| `sonar-reasoning-pro` | chat | 0 | cached_input=1.0, input=2.0, output=8.0, search_context_cost_per_query={'high': 0.014, 'low': 0.006, 'medium': 0.01} | 128000/ |
| `cf.plamo-embedding-1b` | embedding | 0 | cached_input=0.0, input=0.019, output=0.0 | 4096/4096 |
| `groq.playai-tts` | audio_speech | 0 | cached_input=0.0, input=50.0, input_cost_per_character=5e-05, output=0.0 | 8192/8192 |
| `groq.playai-tts-arabic` | audio_speech | 0 | cached_input=0.0, input=50.0, input_cost_per_character=5e-05, output=0.0 | 8192/8192 |
| `gen4.5` | video_generation | 1 | output_cost_per_video_per_second=0.12 | / |
| `gen4_image` | image_generation | 1 | input=0.0, output=50.0, output_cost_per_image=0.05, output_cost_per_image_1920x1080=0.08 | / |
| `gen4_image_turbo` | image_generation | 1 | input=0.0, output=20.0, output_cost_per_image=0.02 | / |
| `gen4_turbo` | video_generation | 1 | output_cost_per_video_per_second=0.05 | / |
| `runwayml.eleven_multilingual_v2` | audio_speech | 0 | cached_input=0.0, input=15.0, input_cost_per_character=1.5e-05, output=0.0 | / |
| `serper-search` | search | 0 | input=0.0, input_cost_per_query=0.001, output=0.0 | / |
| `tavily-search` | search | 0 | input=0.0, input_cost_per_query=0.008, output=0.0 | / |
| `tavily-search-advanced` | search | 0 | input=0.0, input_cost_per_query=0.016, output=0.0 | / |
| `grok-3` | None | 0 | cached_input=1.5, input=3.0, output=15.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-3-beta` | None | 0 | cached_input=1.5, input=3.0, output=15.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-3-fast` | chat | 1 | cached_input=2.5, input=5.0, output=25.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | 131072/131072 |
| `grok-3-fast-beta` | None | 1 | cached_input=2.5, input=5.0, output=25.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-3-fast-latest` | None | 0 | cached_input=2.5, input=5.0, output=25.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-3-latest` | None | 0 | cached_input=1.5, input=3.0, output=15.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-3-mini` | None | 0 | cached_input=0.15, input=0.3, output=0.5, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-3-mini-beta` | None | 0 | cached_input=0.15, input=0.3, output=0.5, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-3-mini-fast` | None | 0 | cached_input=0.3, input=0.6, output=4.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-3-mini-fast-beta` | None | 1 | cached_input=0.3, input=0.6, output=4.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-3-mini-fast-latest` | None | 0 | cached_input=0.3, input=0.6, output=4.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-3-mini-latest` | None | 0 | cached_input=0.15, input=0.3, output=0.5, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-4` | None | 1 | cached_input=0.75, input=3.0, output=15.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-4-0709` | None | 1 | cached_input=0.75, input=3.0, output=15.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-4-1-fast-non-reasoning` | None | 0 | cached_input=0.05, input=0.2, output=0.5, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-4-1-fast-reasoning` | None | 0 | cached_input=0.05, input=0.2, output=0.5, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-4-fast-non-reasoning` | chat | 0 | cached_input=0.05, input=0.2, output=0.5, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | 2000000.0/2000000.0 |
| `grok-4-fast-reasoning` | chat | 0 | cached_input=0.05, input=0.2, output=0.5, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | 2000000.0/2000000.0 |
| `grok-4-latest` | None | 1 | cached_input=0.75, input=3.0, output=15.0, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | / |
| `grok-4.20-beta-0309-non-reasoning` | chat | 0 | cached_input=0.2, cached_input_above_200K=0.4, input=2.0, input_above_200K=4.0, output=6.0, output_above_200K=12.0 | 20000000.0/2000000.0 |
| `grok-4.20-beta-0309-reasoning` | chat | 0 | cached_input=0.2, cached_input_above_200K=0.4, input=2.0, input_above_200K=4.0, output=6.0, output_above_200K=12.0 | 20000000.0/2000000.0 |
| `grok-4.20-non-reasoning` | chat | 0 | cached_input=0.2, cached_input_above_200K=0.4, input=2.0, input_above_200K=4.0, output=6.0, output_above_200K=12.0 | 20000000.0/2000000.0 |
| `grok-4.20-reasoning` | chat | 0 | cached_input=0.2, cached_input_above_200K=0.4, input=2.0, input_above_200K=4.0, output=6.0, output_above_200K=12.0 | 20000000.0/2000000.0 |
| `grok-4.3` | chat | 0 | cached_input=0.2, cached_input_above_200K=0.4, input=1.25, input_above_200K=2.5, output=2.5, output_above_200K=5.0 | 20000000.0/2000000.0 |
| `grok-4.5` | chat | 0 | cached_input=0.5, cached_input_above_200K=1.0, input=2.0, input_above_200K=4.0, output=6.0, output_above_200K=12.5 | 500000/500000 |
| `grok-4.6` | chat | 0 | cached_input=0.5, cached_input_above_200K=1.0, input=2.0, input_above_200K=4.0, output=6.0, output_above_200K=12.5 | 500000/500000 |
| `grok-4.7` | chat | 0 | cached_input=0.5, cached_input_above_200K=1.0, input=2.0, input_above_200K=4.0, output=6.0, output_above_200K=12.5 | 500000/500000 |
| `grok-code-fast-1` | chat | 0 | cached_input=0.02, input=0.2, output=1.5, search_context_cost_per_query={'low': 0.025, 'medium': 0.025, 'high': 0.025} | 256000/256000 |
| `glm-5.1` | chat | 0 | cached_input=0.26, input=1.4, output=4.4 | 200000/128000 |
| `glm-5.2` | chat | 0 | cached_input=0.26, input=1.4, output=4.4 | 991000/128000 |
| `glm-5.3` | chat | 0 | cached_input=0.26, input=1.4, output=4.4 | 991000/128000 |
| `glm-5.3-flash` | chat | 0 | cached_input=0.015, input=0.075, output=0.25 | 991000/128000 |
