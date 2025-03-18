"""Command line interface for prompt optimization."""

import click
from .core import PromptOptimizer


@click.group()
@click.version_option()
def cli():
    """Command-line interface for prompt optimization"""

@cli.command()
@click.option("--input", "-i", required=True, help="Input text or file path")
@click.option("--output", "-o", help="Output file (default: stdout)")
@click.option(
    "--min-preserve-length",
    "-m",
    type=int,
    default=50,
    show_default=True,
    help="Minimum preserved length (words)",
)
def optimize(input, output, min_preserve_length):  # pylint: disable=redefined-builtin
    """Optimize a prompt using advanced redundancy removal techniques."""
    try:
        # Check if input is a file path or direct text
        try:
            with open(input, "r", encoding="utf-8") as f:
                prompt = f.read()
        except FileNotFoundError:
            prompt = input

        optimizer = PromptOptimizer(min_preserve_length=min_preserve_length)
        optimized = optimizer.optimize(prompt)

        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(optimized)
        else:
            click.echo(optimized)
    except ValueError as e:
        raise click.ClickException(str(e)) from e


if __name__ == "__main__":
    cli()
