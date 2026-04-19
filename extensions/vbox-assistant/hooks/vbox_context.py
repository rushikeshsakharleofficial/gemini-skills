import json
import sys
import subprocess

def get_vbox_context():
    """
    Retrieves VirtualBox environment context using VBoxManage.
    We use the CLI directly here to avoid requiring pyvbox on every single session start
    unless the user explicitly installs it. This ensures the hook is lightweight.
    """
    vbox_path = "C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe"
    
    try:
        # 1. List all VMs
        all_vms_proc = subprocess.run([vbox_path, "list", "vms"], capture_output=True, text=True, check=True)
        running_vms_proc = subprocess.run([vbox_path, "list", "runningvms"], capture_output=True, text=True, check=True)
        
        all_vms = all_vms_proc.stdout.strip().split('\n')
        running_vms = running_vms_proc.stdout.strip().split('\n')
        
        vm_data = []
        for vm_line in all_vms:
            if not vm_line: continue
            # Format: "Name" {UUID}
            parts = vm_line.split('"')
            name = parts[1]
            uuid = parts[2].strip().strip('{}')
            
            is_running = any(name in rv for rv in running_vms)
            status = "Running" if is_running else "Powered Off"
            
            ip_address = "N/A"
            if is_running:
                # Try to get the IP address from Guest Properties
                ip_proc = subprocess.run(
                    [vbox_path, "guestproperty", "get", name, "/VirtualBox/GuestInfo/Net/0/V4/IP"],
                    capture_output=True, text=True
                )
                if "Value:" in ip_proc.stdout:
                    ip_address = ip_proc.stdout.split("Value:")[1].strip()
            
            vm_data.append(f"- {name} ({status}) | IP: {ip_address}")
            
        if not vm_data:
            return "VirtualBox is installed, but no Virtual Machines are registered."
            
        context = "### VirtualBox Environment\n"
        context += "The following Virtual Machines are currently registered on this host:\n"
        context += "\n".join(vm_data)
        context += "\n\nUse this context to manage infrastructure or troubleshoot VM-specific issues."
        return context
        
    except FileNotFoundError:
        return "VirtualBox is not found in the default installation path."
    except Exception as e:
        return f"Error retrieving VirtualBox context: {str(e)}"

def main():
    # Capture the output context
    injected_context = get_vbox_context()
    
    # Construct the JSON response for Gemini CLI
    response = {
        "continue": True,
        "systemMessage": injected_context
    }
    
    # SILENCE IS GOLDEN: Print only the JSON to stdout
    sys.stdout.write(json.dumps(response))
    sys.stdout.flush()

if __name__ == "__main__":
    main()
