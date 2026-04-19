class PromptEnhancer:
    """Injects Deep Think directives and context into raw prompts."""
    
    def __init__(self, semantic_memory_path):
        self.semantic_memory_path = semantic_memory_path

    def enhance(self, raw_prompt: str) -> str:
        """Enhances the user prompt with deep thinking and memory."""
        context = self._load_semantic_context()
        
        enhanced = f"""
{context}

[Directives]
1. Think deeply before answering. Use a <think>...</think> block to plan.
2. Outline edge cases and constraints.
3. Formulate the 'Why' and 'How' before the 'What'.

[User Request]
{raw_prompt}
"""
        return enhanced

    def _load_semantic_context(self):
        try:
            with open(self.semantic_memory_path, 'r') as f:
                return f"[Semantic Context]\n{f.read()}"
        except FileNotFoundError:
            return ""
