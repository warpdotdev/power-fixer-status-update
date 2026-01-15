#!/usr/bin/env python3
"""PowerFixer status reporting script.

This script posts status updates to the PowerFixer callback API.
It should be used by agents to report their progress.

Usage:
    python3 powerfixer_status.py '{"state": "IN_PROGRESS"}'
    python3 powerfixer_status.py '{"state": "SUCCEEDED", "summary": "Fixed the bug"}'
    echo '{"state": "FAILED"}' | python3 powerfixer_status.py

Required environment variables:
    POWERFIXER_CALLBACK_TOKEN - Authentication token for the callback API
    POWERFIXER_CALLBACK_URL - Base URL of the PowerFixer server
"""
import json
import os
import sys
import urllib.request


def post_status(payload):
    """Post a status update to the PowerFixer callback API."""
    token = os.environ["POWERFIXER_CALLBACK_TOKEN"]
    base = os.environ["POWERFIXER_CALLBACK_URL"].rstrip("/")
    url = base + "/api/v1/agent/status"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            "ngrok-skip-browser-warning": "1",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        resp.read()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = json.loads(sys.argv[1])
    else:
        payload = json.load(sys.stdin)
    post_status(payload)
