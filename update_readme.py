#!/usr/bin/env python3
"""
Script to update the README.md with current device issues from GitHub API.
Also generates EC testability interface documentation.
"""

import re
a section that lists supported devices and links each one to its open issues on GitHub.
import urllib.request
import json
import os
import sys


def get_github_token():
- Extracts all device labels and their associated keys.
    return os.environ.get('GITHUB_TOKEN')



def fetch_issues(labels=None):
    """Fetch open issues from the dasharo-issues repository."""
    token = get_github_token()
        python3 update_readme_devices.py
"""

import yaml
import urllib.parse
import re

REPO = "dasharo/dasharo-issues"
YAML_PATH = ".github/advanced-issue-labeler.yml"
README_PATH = "README.md"
START_MARKER = "<!-- BEGIN DEVICE ISSUES -->"
END_MARKER = "<!-- END DEVICE ISSUES -->"

def load_policy_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def extract_device_entries(policy):
    entries = []
    for section in policy.get("policy", []):
        for sec in section.get("section", []):
            if sec.get("id") == ["device"] and "other" in sec.get("block-list", []):
                for item in sec.get("label", []):
                    label_name = item["name"]
                    for key in item.get("keys", []):
                        entries.append((key, label_name))
    return entries

def generate_issue_search_url(repo, label_name):
        return []



def get_device_labels():
    """Get all device-specific labels from issues."""
    issues = fetch_issues()
        url = generate_issue_search_url(REPO, label_name)
        lines.append(f"- [{device_name}]({url})")
    return "\n".join(lines)

def update_readme(readme_path, new_section):
    with open(readme_path, "r") as f:
        content = f.read()

    pattern = re.compile(rf"{START_MARKER}.*?{END_MARKER}", re.DOTALL)
    replacement = f"{START_MARKER}\n{new_section}\n{END_MARKER}"

    if pattern.search(content):
    return sorted(device_labels)



def generate_device_section():
    """Generate the device issues section for README."""
    device_labels = get_device_labels()

if __name__ == "__main__":
    policy = load_policy_yaml(YAML_PATH)
    entries = extract_device_entries(policy)
    section = generate_readme_section(entries)
    update_readme(README_PATH, section)
    print("README.md updated with flat device issue links.")
    return section



def update_readme():
    """Update the README.md file with current device issues."""
    try:
        print(f"Error updating README: {e}")



def generate_ec_testability_docs():
    """Generate EC testability interface documentation."""
    docs = """# EC Testability Interface

## Overview

The EC Testability Interface provides a remote control mechanism for testing
laptop platforms where the Embedded Controller (EC) manages critical platform
aspects. This enables comprehensive remote testing of platforms that would
otherwise require physical access.

## Interface Specification

### Communication Protocol

The EC testability interface supports two communication methods:

1. **SMBus Interface** - For platforms with exposed SMBus connectivity
2. **Parallel Port Interface** - For direct hardware debugging

### Supported Commands

#### Key Press Generation
- `KEY_PRESS <scancode>` - Simulate a single key press
- `KEY_HOLD <scancode>` - Hold a key down
- `KEY_RELEASE <scancode>` - Release a held key
- `KEY_COMBO <scancode1> [scancode2 ...]` - Press multiple keys simultaneously

#### Button Press Generation
- `PWR_BTN_PRESS` - Simulate power button press
- `PWR_BTN_HOLD <duration_ms>` - Hold power button for specified duration
- `RST_BTN_PRESS` - Simulate reset button press

#### Power Control
- `POWER_ON` - Power on the platform
- `POWER_OFF` - Force power off
- `POWER_CYCLE` - Perform power cycle
- `RESET` - Perform platform reset
- `SUSPEND` - Enter suspend state
- `RESUME` - Resume from suspend

#### EC Debug
- `EC_VERSION` - Get EC firmware version
- `EC_STATUS` - Get EC status information
- `EC_RESET` - Reset the EC
- `EC_CONSOLE <enable|disable>` - Enable/disable EC console output

### BIOS Configuration

A new BIOS option `EC Testability Interface` is available under:
**Security** -> **EC Debug Options** -> **EC Testability Interface**

| Setting | Description |
|---------|-------------|
| `Disabled` (default) | EC testability interface is disabled |
| `Enabled` | EC testability interface is active |

**Important:** This option defaults to `Disabled` for security reasons.
It must be explicitly enabled to allow remote EC control.

### Debugger Firmware Requirements

The debugger firmware must support bidirectional console communication
to properly interface with the EC testability module.

Required debugger firmware features:
- Bidirectional console support
- SMBus master/slave capability (for SMBus mode)
- GPIO control (for parallel mode)
- Command buffering and parsing

### Security Considerations

- The interface is disabled by default
- Requires physical access to enable (BIOS setting)
- All commands are logged for audit purposes
- Invalid commands are rejected and logged

### Platform Support

This interface is supported on the following platforms:
- NovaCustom NV4x (TGL)
- NovaCustom NS5x/7x (TGL)
- NovaCustom NS7x (TGL)
- NovaCustom NS5x/7x (ADL)
- NovaCustom NV4x (ADL)
- NovaCustom V54x (MTL)
- NovaCustom V56x (MTL)

"""
    return docs


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--ec-docs':
        print(generate_ec_testability_docs())
    else:
        update_readme()
