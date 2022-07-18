#!/bin/bash
# Copyright 2018- <linrongbin16@gmail.com>

INSTALL=~/.vcmd/install
OS="$(uname -s)"

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

# pip packages
sudo pip3 install --upgrade click pytz chardet

# cargo commands
cargo install ripgrep

# environment path
echo "export PATH=~/.vcmd:\$PATH" >> ~/.bashrc
