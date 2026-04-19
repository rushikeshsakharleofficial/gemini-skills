# VirtualBox Assistant Extension

This extension provides real-time VirtualBox context to the Gemini CLI. It automatically detects registered VMs, their status, and guest IP addresses at the start of every session.

## Features
- **Session Context**: Automatically lists all VMs when you start `gemini`.
- **IP Detection**: Retrieves the guest IP address for running VMs (requires VirtualBox Guest Additions).
- **Lightweight**: Uses standard `VBoxManage` CLI calls to minimize overhead.

## Installation
To link this extension to your Gemini CLI:
```bash
gemini extensions link extensions/vbox-assistant
```

## How it Works
The extension registers a `SessionStart` hook that executes `hooks/vbox_context.py`. This script outputs a JSON-formatted system message that is injected into the model's context, making the agent "aware" of your local infrastructure immediately.
