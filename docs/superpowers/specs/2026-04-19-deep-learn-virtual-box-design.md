# Deep Learn Virtual Box Skill - Design Specification

> **Date:** 2026-04-19
> **Status:** Draft
> **Topic:** Mastery of the VirtualBox ecosystem through CLI, SDK, and automation.

## 1. Overview
The **Deep Learn Virtual Box** skill is a comprehensive reference guide for the Gemini agent to master VirtualBox at an expert level. It moves beyond surgical fixes to complete system administration, focusing on scriptable automation and advanced troubleshooting.

## 2. Goals & Success Criteria
- **CLI Mastery**: Full proficiency with `VBoxManage`, `vbox-img`, and `vboxwebsrv`.
- **Advanced Networking**: Ability to configure complex NAT Networks, DHCP, and Port Forwarding.
- **SDK Integration**: Programmatic control using Python (`pyvbox`) and the VirtualBox SDK.
- **Diagnostic Mastery**: Deep analysis of `VBox.log` and hex error codes (e.g., `0xC0000005`).
- **Automation Excellence**: Integration patterns for Vagrant, Terraform, and Packer.

## 3. Architecture & Modules

### 3.1 Module: CLI Mastery (`VBoxManage`)
- **Emergency Recovery**: Breaking locks (`emergencystop`), force-killing `VBoxSVC`, and fixing `<inaccessible>` states.
- **Storage Plumbing**: Converting (`clonemedium`), resizing, and plumbing (`storagectl`/`storageattach`) VDI/VMDK/VHD disks.
- **Virtualization Core**: Enforcing Nested VT-x, PAE/NX, and Large Pages via CLI.

### 3.2 Module: Advanced Networking
- **NAT Network Service**: Full lifecycle of shared NAT networks, DHCP assignment, and complex Port Forwarding rules.
- **Adapter Comparison**: Decision matrix for NAT vs. Bridged vs. Host-Only vs. Internal vs. NAT Network.

### 3.3 Module: Programmatic Integration (SDK)
- **Python (`pyvbox`)**: Patterns for listing, starting, and controlling VMs via code.
- **Web Service**: Setting up and authenticating with `vboxwebsrv` for multi-host control.

### 3.4 Module: Diagnostic & Performance
- **VBox.log Analysis**: Mapping specific hex codes to hardening or driver issues.
- **Performance Tuning**: Optimizing VRAM, 3D acceleration (VMSVGA/VBoxSVGA), and CPU execution caps.

## 4. Key Patterns & Golden Rules
- **"Headless First"**: Avoid the GUI for all complex operations to prevent locks.
- **"Scriptable Always"**: Ensure every action can be reproduced via a script or automation tool.
- **Safety First**: Never delete physical folders without unregistering via `VBoxManage` first.

## 5. Testing & Verification
- **Scenario 1**: Recover a VM stuck in a "Locked" state after a system crash.
- **Scenario 2**: Resize a VMDK disk by converting it to VDI, expanding, and converting back.
- **Scenario 3**: Automate the creation of a NAT Network with custom DHCP and SSH port forwarding.

---
**Approved by:** [User]
**Implemented by:** [Gemini CLI]
