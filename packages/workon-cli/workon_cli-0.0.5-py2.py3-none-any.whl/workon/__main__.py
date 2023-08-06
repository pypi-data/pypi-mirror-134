"""Workon entry point."""

from workon import cli, __app_name__
from workon.cli import __app_name__

def main():
    """Workon entry point."""
    
    cli.app(prog_name = __app_name__)

if __name__ == "__main__":
    main()