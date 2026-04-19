# Deep Learn Virtual Box Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a comprehensive "Deep Learn Virtual Box" skill covering CLI, SDK, and automation for expert-level mastery.

**Architecture:** A module-based SKILL.md document with troubleshooting-first emergency recovery, detailed CLI storage/networking guides, and programmatic SDK patterns.

**Tech Stack:** VirtualBox 7.1+, VBoxManage CLI, pyvbox (Python SDK).

---

### Task 1: Create Skill Folder & SKILL.md Structure

**Files:**
- Create: `skills/deep-learn-virtual-box/SKILL.md`

- [ ] **Step 1: Scaffolding the Skill**
Create the base structure with frontmatter and overview.

```markdown
---
name: Deep-Learn-Virtual-Box
description: Use when mastering VirtualBox via CLI (VBoxManage), SDK (pyvbox), or automation tools (Vagrant/Terraform/Packer).
---

# Deep Learn Virtual Box

## Overview
Comprehensive reference for expert-level VirtualBox management, focusing on scriptable automation and deep troubleshooting.
```

- [ ] **Step 2: Add Module 1: CLI Mastery (Emergency & Storage)**
Add instructions for `emergencystop`, breaking locks, and disk conversion/resizing.

- [ ] **Step 3: Add Module 2: Advanced Networking**
Add instructions for NAT Networks, DHCP, and complex Port Forwarding syntax.

- [ ] **Step 4: Add Module 3: Programmatic Integration (SDK)**
Add Python `pyvbox` and `vboxwebsrv` setup patterns.

- [ ] **Step 5: Add Module 4: Diagnostic Deep Dive**
Add `VBox.log` analysis and common hex error code mappings.

- [ ] **Step 6: Add common red flags and anti-patterns**

- [ ] **Step 7: Commit**

```bash
git add skills/deep-learn-virtual-box/SKILL.md
git commit -m "feat(skills): add Deep Learn Virtual Box skill"
```

### Task 2: Verification and Delivery

- [ ] **Step 1: Self-Review for Completeness**
Ensure all syllabus modules from the design spec are present and accurate.

- [ ] **Step 2: Final Commit and Push**

```bash
git push origin main
```
