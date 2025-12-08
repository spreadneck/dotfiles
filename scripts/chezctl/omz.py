from pathlib import Path
from .utils import run, info, success

def install_omz():
    omz_dir = Path.home() / ".oh-my-zsh"
    if omz_dir.exists():
        info("OH-MY-ZSH already installed.")
        return

    info("Installing OH-MY-ZSH...")
    run('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
    success("OH-MY-ZSH installed.")

