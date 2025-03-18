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
# Prompt Optimizer

A toolkit for optimizing LLM prompts by removing redundancy while preserving key information.

## Installation

```bash
pip install prompt-optimizer
```

## Usage

### Command Line Interface

Optimize a prompt from text:
```bash
prompt-optimizer optimize -i "Your long prompt text here..."
```

Optimize a text file:
```bash
prompt-optimizer optimize -i input.txt -o optimized.txt
```

### Python API

```python
from prompt_optimizer import PromptOptimizer

optimizer = PromptOptimizer(min_preserve_length=50)
optimized_prompt = optimizer.optimize("Your long prompt text...")
```

## Features

- Redundancy removal
- Length preservation controls 
- File input/output support
- CLI and Python API interfaces

## Development

To contribute:

1. Clone repo & install dev dependencies:
```bash
git clone https://github.com/yourusername/prompt-optimizer.git
cd prompt-optimizer
pip install -e .[dev]
```

2. Run tests:
```bash
pytest
```

## Contributing

Contributions welcome! Please open an issue first to discuss proposed changes.
