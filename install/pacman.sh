#!/bin/bash

INSTALL=~/.vcmd/install

echo "install dependencies with pacman"

sudo pacman -Syy
$INSTALL/install_or_skip.sh "yes | sudo pacman -S unzip" "unzip"
$INSTALL/install_or_skip.sh "yes | sudo pacman -S zip" "zip"
$INSTALL/install_or_skip.sh "yes | sudo pacman -S bzip2" "bzip2"
$INSTALL/install_or_skip.sh "yes | sudo pacman -S p7zip" "7z"
$INSTALL/install_or_skip.sh "yes | sudo pacman -S openssh" "ssh"
$INSTALL/install_or_skip.sh "yes | sudo pacman -S cmake" "cmake"

# python3
$INSTALL/install_or_skip.sh "yes | sudo pacman -S python python-pip" "python3"
