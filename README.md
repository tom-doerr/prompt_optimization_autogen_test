# Prompt Optimizer

A tool for optimizing LLM prompts by removing redundancy while preserving critical information and technical terminology.

## Features

- Removes redundant phrases and simplifies verbose expressions  
- Maintains key technical terms and requirements
- Configurable minimum length preservation
- CLI and Python API interfaces

## Installation

```bash
pip install prompt-optimizer
```

## CLI Usage

```bash
# Optimize a prompt from text
prompt-optimizer optimize --input "Your prompt text" --min-preserve-length 100

# Optimize a prompt from file
prompt-optimizer optimize --input input.txt --output optimized.txt

# Get help
prompt-optimizer --help
prompt-optimizer optimize --help
```

## Python API

```python
from prompt_optimizer import PromptOptimizer

optimizer = PromptOptimizer(min_preserve_length=75)
optimized_prompt = optimizer.optimize("Your original prompt text")
```

## Development

```bash
# Install dev dependencies
pip install -r requirements.txt

# Run tests with coverage
pytest --cov --cov-report=term-missing

# Lint code
pylint prompt_optimizer tests
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for any changes
4. Submit a pull request

## License

MIT License - See [LICENSE](LICENSE) for details.
