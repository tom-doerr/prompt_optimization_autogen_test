# Prompt Optimizer

A toolkit for optimizing LLM prompts by removing redundancy while preserving key information.

## Features

- Removes redundant phrases and verbose expressions
- Maintains technical terms and key requirements
- Configurable minimum length preservation
- Command line interface for easy integration

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Python API

```python
from prompt_optimizer import PromptOptimizer

optimizer = PromptOptimizer(min_preserve_length=50)
optimized_prompt = optimizer.optimize("Your original prompt text here")
```

### Command Line Interface

Basic usage:
```bash
python -m prompt_optimizer.cli optimize --input "Your prompt text" --output optimized.txt
```

Process a file:
```bash
python -m prompt_optimizer.cli optimize -i input.txt -o output.txt
```

Pipe from stdin:
```bash
echo "Your prompt text" | python -m prompt_optimizer.cli optimize
```

## Options

```
Options:
  -i, --input TEXT         Input prompt text or file path  [required]
  -o, --output TEXT        Output file path (default: stdout)
  -m, --min-preserve-length INTEGER  Minimum length to preserve [default: 50]
  --help                   Show this message and exit.
```

## Contributing

Contributions are welcome! Please open an issue or PR for any improvements.
