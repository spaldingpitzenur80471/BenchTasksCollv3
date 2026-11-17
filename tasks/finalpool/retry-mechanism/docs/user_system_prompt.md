# User System Prompt

## Task Context
You are helping develop a retry mechanism. The user needs resilient HTTP calls in their service.

## User Requirements
- Retry failed requests with increasing delays
- Stop retrying after a maximum number of attempts
- Do not retry on permanent errors like 4xx
- Log each attempt for debugging