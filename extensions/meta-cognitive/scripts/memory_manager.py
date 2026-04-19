import os
import json
import tiktoken  # Use tiktoken or similar for token counting

class MemoryManager:
    """Handles Working, Episodic, and Semantic memory tiers."""
    
    def __init__(self, max_tokens=100000):
        self.max_tokens = max_tokens
        self.memory_dir = ".gemini/memory"
        os.makedirs(self.memory_dir, exist_ok=True)
        self.episodic_path = f"{self.memory_dir}/episodic.jsonl"
        self.semantic_path = f"{self.memory_dir}/semantic.md"

    def auto_compact_context(self, history: list) -> list:
        """Compact context if over 85% capacity."""
        current_tokens = self._count_tokens(history)
        if current_tokens > (self.max_tokens * 0.85):
            print("[Memory] Context > 85%. Triggering Flash-Lite compaction...")
            return self._summarize_history(history)
        return history

    def save_episodic(self, task: str, outcome: str):
        """Save task results to timeline."""
        with open(self.episodic_path, "a") as f:
            json.dump({"timestamp": time.time(), "task": task, "outcome": outcome}, f)
            f.write("\n")

    def _summarize_history(self, history: list) -> list:
        # Keep last 5 turns exactly, summarize the rest using Flash-Lite
        recent = history[-5:]
        older = history[:-5]
        summary = "[Flash-Lite Summary]: " + " ".join([m['content'][:50] for m in older])
        return [{"role": "system", "content": summary}] + recent

    def _count_tokens(self, history: list) -> int:
        # Mock token counter
        return sum(len(str(item)) for item in history)
