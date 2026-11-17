# Agent System Prompt

## General Requirements
Please complete the implementation for retry-mechanism in the current directory.

## Functional Requirements

### Core Functionality
- Implement retry logic with exponential backoff
- Support configurable retry strategies
- Handle transient and permanent failures differently
- Log retry attempts with details
- Support circuit breaker patterns

### Implementation Requirements
- Create a Python implementation with proper error handling
- Include unit tests for core functionality
- Document the API with docstrings
- Ensure thread-safety for concurrent retries

## Notes
- Read `docs/user_system_prompt.md` for user requirements
- Place tests in `tests/` directory