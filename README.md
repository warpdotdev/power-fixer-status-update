# PowerFixer Status Update

A simple Python script for PowerFixer agents to report status updates to the PowerFixer callback API.

## Installation

Clone this repository:

```bash
git clone https://github.com/warpdotdev/power-fixer-status-update.git /workspace/power-fixer-status-update
```

## Usage

```bash
# Report in progress
python3 /workspace/power-fixer-status-update/powerfixer_status.py '{"state": "IN_PROGRESS"}'

# Report success with summary
python3 /workspace/power-fixer-status-update/powerfixer_status.py '{"state": "SUCCEEDED", "summary": "Fixed the bug"}'

# Report failure
python3 /workspace/power-fixer-status-update/powerfixer_status.py '{"state": "FAILED", "summary": "Could not reproduce"}'

# Pipe JSON from stdin
echo '{"state": "IN_PROGRESS"}' | python3 /workspace/power-fixer-status-update/powerfixer_status.py
```

## Required Environment Variables

- `POWERFIXER_CALLBACK_TOKEN` - Authentication token for the callback API
- `POWERFIXER_CALLBACK_URL` - Full URL of the PowerFixer callback endpoint (e.g., `https://powerfixer.warp.dev/api/v1/agent/runs/abc123/callback`)

## Valid States

- `IN_PROGRESS` - Agent is actively working
- `SUCCEEDED` - Agent completed successfully
- `FAILED` - Agent failed to complete the task
