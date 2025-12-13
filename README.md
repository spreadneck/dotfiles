# Dotfiles setup (Fedora/RHEL)

These dotfiles are managed with [chezmoi](https://www.chezmoi.io/). Applying the configuration bootstraps a Python virtual environment and runs the `chezctl` helper to install Oh My Zsh, Powerlevel10k, and bundled Zsh plugins.

## Prerequisites
Install the base tools on Fedora, RHEL, or other `dnf`-based systems:

```bash
sudo dnf install -y git curl zsh python3 python3-pip python3-virtualenv chezmoi
```

The first `chezmoi apply` will automatically run `run_once_00_dnf_prereqs.sh` to install the same packages with `dnf` (using `sudo`
when necessary). If you already have the prerequisites, the step will exit immediately.

## First-time installation
1. Clone or initialize chezmoi with this repository (replace the URL with your fork if needed):
   ```bash
   chezmoi init --apply https://github.com/<your-user>/dotfiles.git
   ```
2. On first apply, chezmoi will create a virtual environment under `~/.local/share/chezctl/venv`, install the Python dependencies in `scripts/chezctl/requirements.txt`, and run the bootstrap sequence (`chezctl bootstrap`). The bootstrap installs Oh My Zsh, the Powerlevel10k theme, and the `zsh-syntax-highlighting` plugin.

## Updating your setup
- Pull and re-apply any changes:
  ```bash
  chezmoi update
  chezmoi apply
  ```
- Re-run the bootstrap steps (useful after reinstalling Zsh):
  ```bash
  source ~/.local/share/chezctl/venv/bin/activate
  python -m chezctl bootstrap
  ```

## Notes
- Neovim configuration is tracked as an external repository via `.chezmoiexternal.toml` and will be fetched automatically during `chezmoi apply`.
- The `run_once_00_venv_install.sh.tmpl` and `run_once_01_chezctl_bootstrap.sh.tmpl` scripts are executed only on the first apply to set up the virtual environment and run the bootstrap helper.
