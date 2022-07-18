#!/bin/bash

INSTALL=~/.vcmd/install

echo "install dependencies with brew"

brew update
$INSTALL/install_or_skip.sh "brew install unzip" "unzip"
$INSTALL/install_or_skip.sh "brew install zip" "zip"
$INSTALL/install_or_skip.sh "brew install bzip2" "bzip2"
$INSTALL/install_or_skip.sh "brew install p7zip" "7z"
$INSTALL/install_or_skip.sh "brew install openssh" "ssh"
$INSTALL/install_or_skip.sh "brew install cmake" "cmake"

# python3
$INSTALL/install_or_skip.sh "brew install python3" "python3"
