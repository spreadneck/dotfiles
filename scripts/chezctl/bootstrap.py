import click
from .omz import install_omz
from .zsh_plugins import install_zsh_plugins
from .p10k import install_p10k
from .utils import info, success

@click.group()
def main():
    """chezctl — dotfile bootstrap & tooling."""
    pass

@main.command()
def bootstrap():
    """Run complete bootstrap sequence."""
    info("== Bootstrap starting ==")
    install_omz()
    install_zsh_plugins()
    install_p10k()
    success("== Bootstrap complete ==")

