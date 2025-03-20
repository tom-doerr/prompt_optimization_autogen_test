"""Unit tests for prompt optimization functionality."""

import pytest
from click.testing import CliRunner
from prompt_optimizer import cli
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


def test_optimize_preserves_markdown_and_code_blocks():
    """Test that markdown and code blocks are preserved intact."""
    optimizer = PromptOptimizer()
    prompt = """
    ## API Requirements
    ```python
    def factorial(n):
        return 1 if n == 0 else n * factorial(n-1)
    ```
    """
    optimized = optimizer.optimize(prompt)
    assert "## API Requirements" in optimized
    assert "```python" in optimized
    assert "def factorial(n):" in optimized


def test_optimize_handles_unicode_properly():
    """Test that Unicode characters are preserved during optimization."""
    optimizer = PromptOptimizer()
    prompt = "Привет! こんにちは! 안녕하세요! 😊"
    optimized = optimizer.optimize(prompt)
    assert all(
        char in optimized for char in ["Привет", "こんにちは", "안녕하세요", "😊"]
    )


def test_cli_basic_usage():
    """Test basic CLI usage."""
    runner = CliRunner()
    result = runner.invoke(
        cli, ["optimize", "--input", "test input", "--min-preserve-length", "50"]
    )
    assert result.exit_code == 0
    assert "test input" in result.output


def test_cli_file_io(tmp_path):
    """Test CLI file input/output functionality."""
    runner = CliRunner()
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    input_file.write_text("sample prompt text")

    result = runner.invoke(
        cli, ["optimize", "--input", str(input_file), "--output", str(output_file)]
    )

    assert result.exit_code == 0
    optimized_text = output_file.read_text()
    original = input_file.read_text()
    assert len(optimized_text) < len(original), "No optimization occurred"
    assert "sample" in optimized_text, "Key content missing"
    assert "prompt text" not in optimized_text, "Redundant content remains"


def test_cli_help_display():
    """Test CLI help documentation displays correctly."""
    runner = CliRunner()
    result = runner.invoke(cli, ["optimize", "--help"])
    assert result.exit_code == 0
    assert (
        "Optimize a prompt using advanced redundancy removal techniques"
        in result.output
    )
    assert "--input" in result.output
    assert "--output" in result.output
    assert "--min-preserve-length" in result.output


def test_cli_empty_input_handling():
    """Test CLI handles empty input appropriately."""
    runner = CliRunner()
    result = runner.invoke(cli, ["optimize", "--input", ""])
    assert result.exit_code == 1
    assert "Input prompt cannot be empty" in result.output  # Match actual error message
def test_cli_version_display():
    """Test CLI version display."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "0.1.1" in result.output
