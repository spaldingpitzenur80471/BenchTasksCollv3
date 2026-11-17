# User System Prompt

## Task Context
You are helping develop a webhook server. The user receives events from external services.

## User Requirements
- Accept POST requests with JSON payloads
- Verify the sender signature
- Run the right handler for each event
- Return 200 on success and 4xx on bad requests