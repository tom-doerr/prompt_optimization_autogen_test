# Prompt Optimizer

A tool to optimize LLM prompts by removing redundancy while preserving critical information. 
Reduces token usage and improves prompt effectiveness through advanced text processing techniques.

## Features

- Removes redundant phrases and duplicate content
- Maintains technical terms and key requirements
- Configurable minimum length preservation
- Simple CLI interface for local usage
- Preserves original intent while reducing length

## Installation

```bash
pip install prompt-optimizer
```

## Usage

### Command Line Interface
```bash
# Optimize text directly
prompt-optimizer optimize -i "Your long prompt text here..."

# Optimize a file and save output
prompt-optimizer optimize -i input.txt -o optimized.txt

# Set minimum preserved length (words)
prompt-optimizer optimize -i input.txt -m 100
```

### Python API
```python
from prompt_optimizer import PromptOptimizer

optimizer = PromptOptimizer(min_preserve_length=75)
optimized_prompt = optimizer.optimize("Your original prompt...")
```

## Development
```bash
# Install dev dependencies
pip install -r requirements.txt

# Run tests
pytest tests/

# Lint code
pylint prompt_optimizer/
```

## Contributing Guidelines

1. Create an issue to discuss proposed changes
2. Fork the repository and create a feature branch
3. Write tests for any new functionality
4. Maintain 100% test coverage
5. Update documentation for all changes
6. Run linter and tests before submitting PR
