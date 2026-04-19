---
name: Deep-Learn-Virtual-Box
description: Use when mastering VirtualBox via CLI (VBoxManage), SDK (pyvbox), or automation tools (Vagrant/Terraform/Packer).
---

# Deep Learn Virtual Box

## Overview
Comprehensive reference for expert-level VirtualBox management, focusing on scriptable automation and deep troubleshooting.

## Core Principles
1.  **"Headless First"**: Operate without a GUI whenever possible to reduce resource overhead and prevent session locks.
2.  **"Scriptable Always"**: Ensure all configurations (storage, networking, resources) are reproducible via CLI or Code.
3.  **"Least Privilege"**: Use standard users for VM management where possible; only elevate for specific host driver or network interface operations.

---

## 🛠️ CLI Mastery (`VBoxManage`)

### 1. Emergency Operations
Use these when a VM is stuck, locked, or the VirtualBox GUI is unresponsive.

*   **Break Session Lock**:
    ```bash
    VBoxManage startvm <VM_NAME> --type emergencystop
    ```
*   **Force Power Off**:
    ```bash
    VBoxManage controlvm <VM_NAME> poweroff
    ```
*   **Fix `<inaccessible>` VMs**:
    Usually caused by a corrupt `.vbox` file.
    1.  Rename `VMName.vbox` to `VMName.vbox-broken`.
    2.  Rename `VMName.vbox-prev` to `VMName.vbox`.
    3.  If it remains inaccessible, unregister the entry: `VBoxManage unregistervm <UUID>`.

### 2. Storage Plumbing & Disk Management
VirtualBox cannot natively resize `VMDK` or fixed-size disks; they must be converted to `VDI` first.

*   **Resize a VMDK**:
    1.  **Convert to VDI**: `VBoxManage clonemedium disk source.vmdk target.vdi --format VDI`
    2.  **Resize VDI**: `VBoxManage modifymedium disk target.vdi --resize <SizeInMB>`
    3.  **Convert back (Optional)**: `VBoxManage clonemedium disk target.vdi resized.vmdk --format VMDK`
*   **Plumbing Disks to a VM**:
    ```bash
    # Add a SATA Controller
    VBoxManage storagectl "VMName" --name "SATA" --add sata --controller IntelAhci
    # Attach the disk
    VBoxManage storageattach "VMName" --storagectl "SATA" --port 0 --device 0 --type hdd --medium path/to/disk.vdi
    ```

### 3. Core Virtualization Settings
Must be set while the VM is **powered off**.

*   **Nested Virtualization**: `VBoxManage modifyvm "VMName" --nested-hw-virt on`
*   **PAE/NX**: `VBoxManage modifyvm "VMName" --pae on`
*   **Nested Paging**: `VBoxManage modifyvm "VMName" --nestedpaging on`

---

## 🌐 Advanced Networking

### 1. NAT Network Service
A shared NAT service for multiple VMs (unlike standard NAT which is isolated).

*   **Create Service**:
    ```bash
    VBoxManage natnetwork add --netname "MyNet" --network "10.0.20.0/24" --enable --dhcp on
    ```
*   **Port Forwarding (CLI Syntax)**:
    `"RuleName:Protocol:[HostIP]:HostPort:[GuestIP]:GuestPort"`
    ```bash
    VBoxManage natnetwork modify --netname "MyNet" --port-forward-4 "ssh:tcp:[]:2222:[10.0.20.5]:22"
    ```

### 2. Network Adapter Decision Matrix
| Mode | Internet Access | Host Access | VM-to-VM Access | Recommended Use |
| :--- | :---: | :---: | :---: | :--- |
| **NAT** | ✅ | ❌ | ❌ | Default, simple internet access. |
| **NAT Network** | ✅ | ❌ | ✅ | Shared internet + internal communication. |
| **Bridged** | ✅ | ✅ | ✅ | VM appears as a physical device on your LAN. |
| **Host-Only** | ❌ | ✅ | ✅ | Private network between Host and Guest. |
| **Internal** | ❌ | ❌ | ✅ | Isolated multi-VM testing (no host access). |

---

## 🐍 Programmatic Integration (SDK)

### 1. Python (`pyvbox`) Setup
1.  Install SDK from VirtualBox downloads.
2.  `cd sdk/installer && python vboxapisetup.py install`
3.  `pip install virtualbox`

### 2. Lifecycle Script Example
```python
import virtualbox
vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
vm = vbox.find_machine("MyVM")
# Launch Headless
progress = vm.launch_vm_process(session, "headless", [])
progress.wait_for_completion()
# ... perform operations ...
session.console.power_down()
```

---

## 🔍 Diagnostics & Performance

### 1. Hex Code Mapping (VBox.log)
*   **`0xC0000005`**: Access Violation. Usually a "Hardening" error. The host OS rejected a VirtualBox driver/DLL due to signing issues or 3rd party interference (Antivirus).
*   **`0x80BB0001`**: Machine is locked. Check for background `VBoxSVC` processes.

### 2. 3D Acceleration Troubleshooting
1.  **VMSVGA** is mandatory for modern Linux guests.
2.  **VBoxSVGA** for Windows guests.
3.  **VRAM**: Ensure at least 128MB for 3D (`VBoxManage modifyvm "VM" --vram 128`).

---

## 🚩 Red Flags & Common Mistakes
*   **Manual Deletion**: Deleting `.vmdk` or `.vbox` folders via File Explorer without using `VBoxManage unregistervm` first. Leads to persistent "Inaccessible" errors.
*   **Resizing VMDK**: Attempting to resize a VMDK directly. It will fail silently or corrupt the disk. Always convert to VDI first.
*   **Hyper-V Conflict**: Running VirtualBox on a Windows host with Hyper-V enabled (WSL2/Docker). Causes "Green Turtle" mode (Software emulation) and massive performance loss.

---

## 🚀 Quick Reference: Common Commands
*   **List all VMs**: `VBoxManage list vms`
*   **List running VMs**: `VBoxManage list runningvms`
*   **Show VM info**: `VBoxManage showvminfo "VMName"`
*   **Take Snapshot**: `VBoxManage snapshot "VMName" take "BeforeUpdate"`
*   **Restore Snapshot**: `VBoxManage snapshot "VMName" restore "BeforeUpdate"`
