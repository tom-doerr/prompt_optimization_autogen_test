# Prompt Optimizer

A toolkit for optimizing LLM prompts by removing redundancy while preserving critical information.

## Features

- Redundancy removal for cleaner prompts
- Length preservation controls
- CLI and Python API interfaces
- File input/output support

## Installation

```bash
pip install prompt-optimizer
```

## CLI Usage

```bash
# Optimize text directly
prompt-optimizer optimize --input "Your long prompt text here..."

# Process files
prompt-optimizer optimize --input input.txt --output optimized.txt

# Set minimum length preservation
prompt-optimizer optimize --input input.txt -m 100

# Get version
prompt-optimizer --version
```

## Python API

```python
from prompt_optimizer import PromptOptimizer

optimizer = PromptOptimizer(min_preserve_length=75)
optimized_prompt = optimizer.optimize("Your long prompt...")
```

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Lint code
pylint prompt_optimizer/ tests/
```

## Contributing

1. Create an issue to discuss changes
2. Add tests for new features
3. Maintain 100% test coverage
4. Update documentation
5. Submit pull request
