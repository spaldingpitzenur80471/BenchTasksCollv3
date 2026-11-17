# Agent System Prompt

## General Requirements
Please complete the implementation for rate-limiter in the current directory.

## Functional Requirements

### Core Functionality
- Implement token bucket rate limiting algorithm
- Support configurable rate limits per client
- Track request counts and enforce limits
- Return appropriate HTTP status codes when limited
- Support multiple rate limiting strategies

### Implementation Requirements
- Create a Python implementation with proper error handling
- Include unit tests for core functionality
- Document the API with docstrings
- Ensure thread-safety for concurrent requests

## Notes
- Read `docs/user_system_prompt.md` for user requirements
- Place tests in `tests/` directory