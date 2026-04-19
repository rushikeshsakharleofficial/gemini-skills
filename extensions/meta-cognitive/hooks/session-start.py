import sys
import os
import json

def main():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        extension_root = os.path.dirname(script_dir)
        
        # Try finding SKILL.md in the global skills directory first
        gemini_root = os.path.dirname(os.path.dirname(extension_root))
        skill_path = os.path.join(gemini_root, "skills", "meta-cognitive", "SKILL.md")

        if not os.path.exists(skill_path):
            # Fallback to looking inside the extension directory
            skill_path = os.path.join(extension_root, "skills", "meta-cognitive", "SKILL.md")
            
        if not os.path.exists(skill_path):
            sys.stderr.write(f"Error: meta-cognitive skill not found at {skill_path}\n")
            sys.exit(1)

        with open(skill_path, 'r', encoding='utf-8') as f:
            skill_content = f.read()

        output = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": f"<EXTREMELY_IMPORTANT>\nYou are operating under Meta-Cognitive Architecture.\n\n**Below is the full content of your 'meta-cognitive' skill. Apply these rules immediately:**\n\n{skill_content}\n</EXTREMELY_IMPORTANT>"
            }
        }

        print(json.dumps(output))
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
