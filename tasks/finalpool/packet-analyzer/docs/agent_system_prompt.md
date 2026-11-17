# Agent System Prompt

## General Requirements
Please complete the implementation for packet-analyzer in the current directory.

## Functional Requirements

### Core Functionality
- Parse network packets from binary capture files
- Support multiple protocol layers (Ethernet, IP, TCP, UDP)
- Extract packet metadata and payload information
- Generate analysis reports with statistics
- Handle corrupted packets gracefully

### Implementation Requirements
- Create a Python implementation with proper error handling
- Include unit tests for core functionality
- Document the API with docstrings
- Ensure thread-safety for concurrent analysis

## Notes
- Read `docs/user_system_prompt.md` for user requirements
- Place tests in `tests/` directory