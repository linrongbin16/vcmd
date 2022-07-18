#!/bin/bash

INSTALL=~/.vcmd/install

echo "install dependencies with dnf"

sudo dnf check-update
$INSTALL/install_or_skip.sh "sudo dnf install -y unzip" "unzip"
$INSTALL/install_or_skip.sh "sudo dnf install -y zip" "zip"
$INSTALL/install_or_skip.sh "sudo dnf install -y bzip2" "bzip2"
$INSTALL/install_or_skip.sh "sudo dnf install -y p7zip p7zip-plugins" "p7zip"
$INSTALL/install_or_skip.sh "sudo dnf install -y openssh" "ssh"
$INSTALL/install_or_skip.sh "sudo dnf install -y cmake" "cmake"

# python3
$INSTALL/install_or_skip.sh "sudo dnf install -y python3 python3-devel python3-pip python3-docutils" "python3"
