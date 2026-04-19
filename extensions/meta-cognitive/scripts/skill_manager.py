import os
import re

class SkillManager:
    """Dynamically loads and unloads SKILL.md based on intent."""
    
    def __init__(self, skills_dir=".gemini/skills"):
        self.skills_dir = skills_dir
        self.active_skills = set()
        
        # Simple intent mapping
        self.skill_map = {
            "security": ["auth", "hack", "vulnerability", "security"],
            "smart-memory": ["memory", "context", "token", "forget", "compact"],
            "model-advisor": ["cost", "latency", "model", "flash", "pro"]
        }

    def scan_and_load(self, prompt: str) -> str:
        """Scan prompt for keywords and load corresponding skills."""
        loaded_content = []
        prompt_lower = prompt.lower()
        
        for skill_name, keywords in self.skill_map.items():
            if any(kw in prompt_lower for kw in keywords):
                if skill_name not in self.active_skills:
                    content = self._load_skill_file(skill_name)
                    if content:
                        loaded_content.append(content)
                        self.active_skills.add(skill_name)
                        print(f"[Skill Manager] Auto-loaded skill: {skill_name}")

        return "\n".join(loaded_content)

    def _load_skill_file(self, skill_name: str):
        path = os.path.join(self.skills_dir, skill_name, "SKILL.md")
        try:
            with open(path, "r") as f:
                return f.read()
        except FileNotFoundError:
            return None
