from pathlib import Path
from .utils import run, info, success

def install_p10k():
    theme_dir = Path.home() / ".oh-my-zsh/custom/themes/powerlevel10k"

    if theme_dir.exists():
        info("Powerlevel10k already installed.")
        return

    info("Installing Powerlevel10k theme...")
    run("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git " + str(theme_dir))
    success("Powerlevel10k installed.")

