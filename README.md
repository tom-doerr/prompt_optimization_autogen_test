# Prompt Optimizer

A tool for optimizing LLM prompts by removing redundancy while preserving key information.

## Features

- Redundancy removal for cleaner prompts
- Preservation of technical terms and key requirements
- Configurable minimum length preservation
- File input/output support
- CLI interface for easy integration into workflows

## Installation

```bash
pip install prompt-optimizer
```

## Usage

### Command Line Interface

```bash
# Optimize a prompt string
prompt-optimizer optimize --input "Your prompt text here" --min-preserve-length 75

# Process input file and save to output file 
prompt-optimizer optimize --input input.txt --output optimized.txt

# See help documentation
prompt-optimizer --help
```

### Python API

```python
from prompt_optimizer import PromptOptimizer

optimizer = PromptOptimizer(min_preserve_length=50)
optimized_prompt = optimizer.optimize("Your original prompt text here")
```

## Development

Contributions are welcome! Please create an issue first to discuss proposed changes.

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

## License

MIT License - See LICENSE file for details.
