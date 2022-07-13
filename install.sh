#!/bin/bash
# Copyright 2018- <linrongbin16@gmail.com>

INSTALL=~/.vcmd/install

case "$OS" in
    Linux)
        if [ -f "/etc/arch-release" ] || [ -f "/etc/artix-release" ]; then
            $INSTALL/pacman.sh
        elif [ -f "/etc/fedora-release" ] || [ -f "/etc/redhat-release" ]; then
            $INSTALL/dnf.sh
        elif [ -f "/etc/gentoo-release" ]; then
            $INSTALL/emerge.sh
        else
            # assume apt
            $INSTALL/apt.sh
        fi
        ;;
    FreeBSD)
        $INSTALL/pkg.sh
        ;;
    NetBSD)
        $INSTALL/pkgin.sh
        ;;
    OpenBSD)
        $INSTALL/pkg_add.sh
        ;;
    Darwin)
        $INSTALL/brew.sh
        ;;
    *)
        echo "OS $OS is not supported, exit..."
        exit 1
        ;;
esac

cd ~/.vcmd
if [ -d ~/.vcmd/pyenv ]; then
    rm -rf ~/.vcmd/pyenv
fi
python3 -m venv ~/.vcmd/pyenv
source ~/.vcmd/pyenv/bin/activate
pip3 install --upgrade pytz
pip3 install --upgrade chardet
deactivate

cargo install ripgrep
