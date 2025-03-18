"""Unit tests for prompt optimization functionality."""

import pytest
from prompt_optimizer.core import PromptOptimizer


@pytest.fixture(name="sample_prompt")
def sample_prompt_fixture():
    """Fixture providing a sample prompt for testing."""
    return """
    Please write a Python function that calculates factorial of a number. 
    The function should: 
    - Take one integer input
    - Return the factorial result
    - Handle edge cases properly
    """


def test_optimize_removes_redundancies(sample_prompt):
    """Test that optimization reduces prompt length while preserving key elements."""
    optimizer = PromptOptimizer()
    optimized = optimizer.optimize(sample_prompt)
    assert len(optimized) < len(sample_prompt)
    assert "integer input" in optimized
    assert "edge cases" in optimized
    assert "Please write a Python function" in optimized


def test_optimize_empty_input():
    """Test that empty input raises appropriate error."""
    optimizer = PromptOptimizer()
    with pytest.raises(ValueError):
        optimizer.optimize("")


def test_optimize_preserves_key_information(
    sample_prompt,
):  # pylint: disable=redefined-outer-name
    """Test that critical information is preserved during optimization."""
    optimizer = PromptOptimizer()
    optimized = optimizer.optimize(sample_prompt)
    key_phrases = ["Python function", "factorial", "integer input", "edge cases"]
    for phrase in key_phrases:
        assert phrase in optimized


def test_optimize_very_long_prompt():
    """Test optimization of very long prompts."""
    optimizer = PromptOptimizer()
    long_prompt = " ".join(["test"] * 1000)
    optimized = optimizer.optimize(long_prompt)
    assert len(optimized) < len(long_prompt)
    assert "test" in optimized
