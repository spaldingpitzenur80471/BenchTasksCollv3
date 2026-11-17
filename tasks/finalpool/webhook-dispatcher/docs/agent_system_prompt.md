# Agent System Prompt

## General Requirements
Please complete the implementation for webhook-dispatcher in the current directory.

## Functional Requirements

### Core Functionality
- Dispatch webhook events to registered endpoints
- Sign payloads with HMAC signatures
- Retry failed deliveries with backoff
- Queue events for offline endpoints
- Log delivery attempts and responses

### Implementation Requirements
- Create a Python implementation with proper error handling
- Include unit tests for core functionality
- Document the API with docstrings
- Ensure thread-safety for concurrent dispatches

## Notes
- Read `docs/user_system_prompt.md` for user requirements
- Place tests in `tests/` directory