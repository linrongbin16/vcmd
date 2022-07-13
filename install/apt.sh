#!/usr/bin/env bash

INSTALL=~/.vcmd/install

echo "install dependencies with apt"

sudo apt-get update
$INSTALL/install_or_skip.sh "sudo apt-get install -y bzip2" "bzip2"
$INSTALL/install_or_skip.sh "sudo apt-get install -y unzip" "unzip"
$INSTALL/install_or_skip.sh "sudo apt-get install -y zip" "zip"
$INSTALL/install_or_skip.sh "sudo apt-get install -y p7zip-full" "7z"
$INSTALL/install_or_skip.sh "sudo apt-get install -y openssh" "ssh"
$INSTALL/install_or_skip.sh "sudo apt-get install -y cmake" "cmake"

# python3
$INSTALL/install_or_skip.sh "sudo apt-get install -y python3 python3-dev python3-venv python3-pip python3-docutils" "python3"
$INSTALL/install_or_skip.sh "sudo apt-get install -y python3 python3-dev python3-venv python3-pip python3-docutils" "pip3"
