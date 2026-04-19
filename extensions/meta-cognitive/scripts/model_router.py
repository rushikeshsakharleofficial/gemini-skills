import json
import os
import time

class ModelRouter:
    """Dynamic model router with fallback and tiered execution."""
    
    TIERS = {
        "PLANNING": ["gemini-3-pro", "gemini-1.5-pro"],
        "EXECUTION": ["gemini-1.5-flash"],
        "COMMAND_IO": ["gemini-1.5-flash-lite"]
    }

    def __init__(self):
        self.cooldowns = {}

    def route_task(self, task_type: str, prompt: str):
        """Route to appropriate tier based on task complexity."""
        models = self.TIERS.get(task_type, self.TIERS["EXECUTION"])
        return self._execute_with_fallback(models, prompt)

    def _execute_with_fallback(self, models: list, prompt: str):
        """Execute with automatic 429 fallback handling."""
        for model in models:
            if self._is_on_cooldown(model):
                continue
            
            try:
                print(f"[Router] Routing to {model}...")
                return self._mock_call_llm(model, prompt)
            except RateLimitError:
                print(f"[Router] 429 Quota hit for {model}. Falling back...")
                self._set_cooldown(model)
                continue
        
        raise Exception("All fallback models exhausted or rate limited.")

    def _mock_call_llm(self, model, prompt):
        # Simulated LLM call
        return f"Output from {model}"

    def _is_on_cooldown(self, model):
        return time.time() < self.cooldowns.get(model, 0)

    def _set_cooldown(self, model, minutes=5):
        self.cooldowns[model] = time.time() + (minutes * 60)

class RateLimitError(Exception):
    pass
