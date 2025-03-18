# Prompt Optimizer Toolkit

A Python package for optimizing LLM prompts by removing redundancy while preserving critical technical information.

## Features

- Redundancy removal while maintaining key requirements
- Configurable minimum length preservation
- File input/output support
- CLI and Python API interfaces
- Comprehensive test coverage
- PEP8 compliant codebase

## Installation

```bash
pip install prompt-optimizer
```

## CLI Usage

```bash
# Optimize text directly (50 word minimum length)
prompt-optimizer --input "Your prompt text" --min-preserve-length 50

# Process input file and save to output
prompt-optimizer --input input.txt --output optimized.txt

# Show full help
prompt-optimizer --help
```

## Python API

```python
from prompt_optimizer import PromptOptimizer

# Initialize with minimum length constraint
optimizer = PromptOptimizer(min_preserve_length=50)

# Optimize a prompt string
optimized_prompt = optimizer.optimize("Your original prompt text")
```

## Development Setup

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run all tests
pytest tests/ --verbose --cov

# Lint code
pylint prompt_optimizer/ tests/
```

## Contributing Guidelines

1. Fork the repository and create a feature branch
2. Include tests for any new functionality
3. Maintain 100% test coverage
4. Update documentation for any changes
5. Submit a pull request with detailed notes

## License

MIT Licensed - See [LICENSE](LICENSE) for details.
