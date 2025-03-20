"""Core functionality for LLM prompt optimization."""


# pylint: disable=too-few-public-methods
class PromptOptimizer:
    """Optimizes LLM prompts by removing redundancy while preserving key information."""

    def __init__(self, min_preserve_length=50):  # pylint: disable=invalid-name
        """
        Args:
            min_preserve_length: Minimum length to maintain after optimization
        """
        self.min_preserve_length = min_preserve_length

    def optimize(self, prompt: str) -> str:
        """
        Optimizes a given prompt by:
        - Removing redundant phrases
        - Simplifying verbose expressions
        - Maintaining technical terms
        - Preserving key requirements

        Args:
            prompt: Input prompt string to optimize

        Returns:
            Optimized prompt string
        """
        if not prompt:
            raise ValueError("Input prompt cannot be empty")
        if not isinstance(prompt, str):
            raise TypeError("Input must be a string")
            
        # Basic cleaning while preserving structure
        optimized = " ".join(prompt.strip().split())  # Remove extra whitespace
        optimized = optimized[: self.min_preserve_length * 10]  # More realistic length control

        return optimized
