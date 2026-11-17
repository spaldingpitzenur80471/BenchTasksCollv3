# Agent System Prompt

## General Requirements
Please complete the implementation for webhook-server in the current directory.

## Functional Requirements

### Core Functionality
- Receive webhook payloads over HTTP
- Verify signatures and authenticate senders
- Parse and validate incoming payloads
- Route events to registered handlers
- Respond with appropriate status codes

### Implementation Requirements
- Create a Python implementation with proper error handling
- Include unit tests for core functionality
- Document the API with docstrings
- Ensure thread-safety for concurrent requests

## Notes
- Read `docs/user_system_prompt.md` for user requirements
- Place tests in `tests/` directory