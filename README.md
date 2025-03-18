# Prompt Optimizer

A Python toolkit for optimizing LLM prompts by removing redundancy while preserving key information.

## Features

- Redundancy removal while maintaining technical terms
- Configurable minimum length preservation (50+ words)
- File input/output support
- Command-line interface (CLI)
- Python API integration

## Installation

```bash
pip install prompt-optimizer
```

## Usage

### Command-line Interface

```bash
# Optimize text with minimum 100 words preserved
prompt-optimizer optimize --input "Your prompt text" --min-preserve-length 100

# Process file input and save to output file 
prompt-optimizer optimize --input input.txt --output optimized.txt

# Show help for optimize command
prompt-optimizer optimize --help
```

### Python API

```python
from prompt_optimizer import PromptOptimizer

# Initialize with custom length constraint
optimizer = PromptOptimizer(min_preserve_length=75)

# Optimize prompt text
original_prompt = "Your detailed instructions here..."
optimized_prompt = optimizer.optimize(original_prompt)
```

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests with coverage
pytest --cov=prompt_optimizer tests/

# Lint codebase
pylint prompt_optimizer/ tests/
```

## Contributing

1. Create an issue to discuss proposed changes
2. Write tests for new features
3. Ensure 100% test coverage
4. Update documentation accordingly
5. Submit pull request with descriptive title

## License

MIT - See [LICENSE](LICENSE) for full details.
