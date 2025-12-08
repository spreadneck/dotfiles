from pathlib import Path
from .utils import run, info, success

PLUGINS = {
    "zsh-syntax-highlighting": "https://github.com/zsh-users/zsh-syntax-highlighting.git",
}

def install_zsh_plugins():
    for name, url in PLUGINS.items():
        dest = Path.home() / f".oh-my-zsh/custom/plugins/{name}"
        if dest.exists():
            info(f"Plugin {name} already installed.")
        else:
            info(f"Installing plugin {name}...")
            run(f"git clone {url} {dest}")
            success(f"{name} installed.")

