#! /bin/bash
# Copyright 2018- <linrongbin16@gmail.com>

cd ~/.vcmd
If (Test-Path $env:UserProfile\.vcmd\pyenv) {
    (Get-Item $env:UserProfile\.vcmd\pyenv).Delete()
}
python3 -m venv ~/.vcmd/pyenv
$env:USERPROFILE/.vcmd/pyenv/Scripts/activate.ps1
pip3 install --upgrade pytz
pip3 install --upgrade chardet
deactivate

cargo install ripgrep
