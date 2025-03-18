"""Prompt optimization toolkit for LLM interactions.

Provides:
- PromptOptimizer class for core optimization logic
- CLI interface for command-line usage
- Configuration options for length preservation
"""

from .core import PromptOptimizer
from .cli import cli

__version__ = "0.1.1"
__all__ = ["PromptOptimizer", "cli"]
