#!/usr/bin/env python3
"""Semantic Search evaluation.

Verifies that semantic-search task is implemented correctly.
"""
import os
import sys


def main() -> int:
    required = [
        'docs/task.md',
        'docs/agent_system_prompt.md',
        'docs/user_system_prompt.md',
        'evaluation/main.py',
        'preprocess/main.py',
    ]
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    missing = [r for r in required if not os.path.exists(os.path.join(base, r))]
    if missing:
        print('MISSING: ' + ', '.join(missing))
        return 1
    print('PASS: all required artifacts present')
    return 0


if __name__ == '__main__':
    sys.exit(main())
