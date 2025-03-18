import pytest
from prompt_optimizer.core import PromptOptimizer

@pytest.fixture
def sample_prompt():
    return """
    Please write a Python function that calculates factorial of a number. 
    The function should: 
    - Take one integer input
    - Return the factorial result
    - Handle edge cases properly
    """

def test_optimize_removes_redundancies(sample_prompt):
    optimizer = PromptOptimizer()
    optimized = optimizer.optimize(sample_prompt)
    
    assert len(optimized) < len(sample_prompt)
    assert "integer input" in optimized
    assert "edge cases" in optimized
    assert "Please write a Python function" in optimized

def test_optimize_empty_input():
    optimizer = PromptOptimizer()
    with pytest.raises(ValueError):
        optimizer.optimize("")

def test_optimize_preserves_key_information(sample_prompt):
    optimizer = PromptOptimizer()
    optimized = optimizer.optimize(sample_prompt)
    
    key_phrases = ["Python function", "factorial", "integer input", "edge cases"]
    for phrase in key_phrases:
        assert phrase in optimized

def test_optimize_very_long_prompt():
    optimizer = PromptOptimizer()
    long_prompt = " ".join(["test"] * 1000)
    optimized = optimizer.optimize(long_prompt)
    
    assert len(optimized) < len(long_prompt)
    assert "test" in optimized
