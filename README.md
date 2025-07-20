# Dotfiles

This repository contains configuration files organized for [GNU Stow](https://www.gnu.org/software/stow/). Clone it into your home directory as `~/.dotfiles`, pull the submodules, and use `stow` to symlink each package into place.

## Clone with submodules

```bash
git clone --recurse-submodules <repo-url> ~/.dotfiles
cd ~/.dotfiles
```

If you already cloned without `--recurse-submodules`, fetch them with:

```bash
git submodule update --init --recursive
```

Two directories are provided as submodules:

- `neovim/.config/nvim` – Neovim configuration
- `vimwiki/vimwiki` – personal Vimwiki notes

## Stowing packages

Run `stow` from the repository root for each package you want to enable. For example:

```bash
stow bash
stow tmux
stow neovim
stow vimwiki
```

This will create the appropriate symlinks in your home directory (e.g. `~/.bashrc`, `~/.config/tmux`).

### Tmux plugins

The `tmux` configuration expects [TPM](https://github.com/tmux-plugins/tpm). After stowing the tmux package, press `<prefix> + I` inside tmux to install plugins.

## Keeping things updated

Update this repository and its submodules periodically:

```bash
git pull --recurse-submodules
git submodule update --remote
```

Only stow the packages you need on a given system.

