# 💎 Gemini Master Skills Library (Rushikesh Edition)
> **"For you sir, always." — Just A Rather Very Intelligent System.**

[![GitHub license](https://img.shields.io/github/license/rushikeshsakharleofficial/gemini-skills)](https://github.com/rushikeshsakharleofficial/gemini-skills/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/rushikeshsakharleofficial/gemini-skills)](https://github.com/rushikeshsakharleofficial/gemini-skills/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/rushikeshsakharleofficial/gemini-skills)](https://github.com/rushikeshsakharleofficial/gemini-skills/issues)
[![Gemini CLI Compatibility](https://img.shields.io/badge/Gemini%20CLI-0.40.0--nightly-blue)](https://github.com/google/gemini-cli)

A consolidated repository of high-performance skills and extensions for the **Gemini CLI**. This library implements **agentic workflows** and **autonomous-ops** for the terminal, transforming standard AI interactions into a proactive, state-aware **Autonomous Engineering Environment**. Optimized for **VirtualBox automation**, **Python SDK** integration, and **self-healing infrastructure**.

## 📍 Table of Contents
- [🛠️ Installation Guide](#️-installation-guide)
- [🚀 The Core Breakthroughs](#-the-core-breakthroughs)
- [🗂️ Library Architecture](#️-library-architecture)
- [📦 VirtualBox Mastery Suite](#-virtualbox-mastery-suite)
- [🧠 How-to: Agentic Automation](#-how-to-agentic-automation)
- [🤝 Contributing](#-contributing)

## 🛠️ Installation Guide

Follow the protocols specific to your operating system to deploy the **Rushikesh AI Core**.

### 1. Prerequisites (All Platforms)

#### **📦 Step 1: Install Node.js & npm**
The Rushikesh AI Core requires **Node.js v20.0.0** or higher. npm is included automatically.

*   **🪟 Windows:** Download the LTS installer from [nodejs.org](https://nodejs.org/) or run:
    ```powershell
    winget install OpenJS.NodeJS
    ```
*   **🍎 macOS:** Use Homebrew:
    ```bash
    brew install node
    ```
*   **🐧 Linux (Ubuntu/Debian):**
    ```bash
    sudo apt update && sudo apt install -y nodejs npm
    ```

#### **🤖 Step 2: Install Gemini CLI (Exact Version)**
The architecture is optimized for version **0.40.0-nightly.20260415.g06e7621b2**. Install it globally:
```bash
npm install -g @google/gemini-cli@0.40.0-nightly.20260415.g06e7621b2
```

### 2. Platform-Specific Deployment

#### **🪟 Windows (PowerShell)**
```powershell
# Install the J.A.R.V.I.S. Core directly
gemini skills install https://github.com/rushikeshsakharleofficial/gemini-skills.git --path skills/jarvis-core --scope user

# Link extensions (Requires Git Bash or PowerShell)
git clone https://github.com/rushikeshsakharleofficial/gemini-skills.git
cd gemini-skills
npm install
cd extensions/gemini-superpowers
gemini extensions link .
```

#### **🍎 macOS & 🐧 Linux (Bash/Zsh)**
```bash
# Install the J.A.R.V.I.S. Core directly
gemini skills install https://github.com/rushikeshsakharleofficial/gemini-skills.git --path skills/jarvis-core --scope user

# Clone and Link Extensions
git clone https://github.com/rushikeshsakharleofficial/gemini-skills.git
cd gemini-skills
npm install
cd extensions/gemini-superpowers
gemini extensions link .
```

### 3. Direct Deployment (The Elite Handshake)
This method is platform-agnostic and installs neural units directly from the cloud:

```bash
# Install Multi-Agent Orchestrator
gemini skills install https://github.com/rushikeshsakharleofficial/gemini-skills.git --path skills/multi-agent-orchestrator --scope user

# Install Systematic Execution (OODA Loop)
gemini skills install https://github.com/rushikeshsakharleofficial/gemini-skills.git --path skills/systematic-execution --scope user
```

### 4. Initialize the Handshake
Restart your Gemini CLI session and run:
```bash
/skills reload
```

## 🚀 The Core Breakthroughs
This isn't just a collection of prompts. It is an architectural overhaul that solves the fundamental limitations of modern AI agents:

*   **Native Pseudo-Terminal (PTY) Integration:** Gemini now handles passwords, `[y/n]` prompts, and interactive menus directly in the core. No more "hanging" on interactive commands.
*   **Strategic Steering Interruption:** Implements an OODA-loop scheduler that allows for mid-batch pivots. Type a new instruction while Gemini is "thinking," and it will adapt instantly—just like Claude Code.
*   **Live Token Analytics:** Real-time +Delta tracking per turn and cumulative session totals in the dynamic footer.
*   **3-Tier Smart Routing:** Automatic model switching (Lite → Flash → Pro) based on task complexity to optimize token quota and performance.
*   **Persistent Multi-Agent Orchestration:** A shared "Blackboard" architecture that allows multiple background subagents to coordinate complex, multi-file refactors without collisions.

## 🗂️ Library Architecture

### 🧠 The J.A.R.V.I.S. Neural Core (`/skills/jarvis-core`)
The primary interface layer. Encodes the sophisticated, dryly witty persona of Tony Stark's assistant. It acts as a proactive system caretaker, running background diagnostics and providing safety briefings before risky operations.

### 🛡️ Resilient Execution Layer (`/skills/systematic-execution`)
Mandates a strict **Observe-Orient-Decide-Act (OODA)** loop. Every command is verified, failures are analyzed with native remediation hints, and environment state is synchronized turn-by-turn.

### 📡 SMTP & Network Expert (`/skills/smtp-expert`)
A deep-diagnostic specialist for email infrastructure and networking. Features **Smart Continuous Learning**, building a local JSON knowledge base of every resolution to prevent repeat diagnostics.

### ⚙️ Windows & Python Specialization
Natively optimized tools for high-performance Windows administration (`windows-admin`) and professional Python development (`python-specialist`).

### 📦 VirtualBox Mastery Suite
A complete ecosystem for expert-level virtualization management.
*   **Deep Learn Virtual Box (`/skills/deep-learn-virtual-box`)**: A master-level reference for `VBoxManage` CLI, storage plumbing, and programmatic SDK integration (Python `pyvbox`).
*   **VirtualBox Assistant Extension (`/extensions/vbox-assistant`)**: Automatically injects real-time VM context (status and IP addresses) into your Gemini sessions at start.

## 🧠 How-to: Agentic Automation

### **How to automate VirtualBox with Gemini?**
Use the `Deep-Learn-Virtual-Box` skill to provide the Gemini agent with the full `VBoxManage` command set. Once active, you can use natural language to provision VMs, e.g., *"Set up a Ubuntu 22.04 VM with 4GB RAM and a 40GB VDI disk."*

### **How to fix a locked VirtualBox session with AI?**
If a VM is stuck in "Locked" or "Being Unlocked" state, the agent can use the emergency break pattern:
```bash
VBoxManage startvm <VM_NAME> --type emergencystop
```
This is built into the `vbox-assistant` troubleshooting module.

### **How to inject VM context into AI sessions?**
Link the `vbox-assistant` extension. It uses a **Python SessionStart hook** to detect all running VMs and their IP addresses, making the agent "infrastructure-aware" before you even type your first command.

## 🛠️ Global Deployment
Every capability in this library is **100% Portable**. All 14 skills are pre-packaged in the `dist/` folder.

**To deploy any unit, use the Master Handshake:**
```bash
gemini skills install ./dist/<skill-name>.skill --scope user
```

## 🤝 Contributing
Contributions are welcome! If you have a high-performance skill or extension, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature.
3. Ensure your `SKILL.md` follows the architectural standards in `skills/jarvis-core`.
4. Submit a Pull Request.

---
*Developed for the Rushikesh Sakharle AI core. Stability: 100% | Persona: Online.*
