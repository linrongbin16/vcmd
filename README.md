# vcmd

A command line utilities implemented by python3.

Separated from [lin.vim](https://github.com/linrongbin16/lin.vim).

# Install

#### For UNIX/Linux/MacOS

> `install.sh` will install below dependencies (if not exists) by system package manager:
>
> - [python3](https://www.python.org/)
>   - [click](https://click.palletsprojects.com/) command argument parsing.
>   - [pytz](https://pypi.org/project/pytz/) for datetime and timestamp commands (vts/vdt).
>   - [chardet](https://pypi.org/project/chardet/) for file encoding commands (vfec).
> - [bzip2](https://www.sourceware.org/bzip2/), [unzip](https://linux.die.net/man/1/unzip), [p7zip](http://p7zip.sourceforge.net/) for compression commands (vzip/vunzip).
> - [openssh](https://www.openssh.com/) for SSH commands (vsshgen).
> - [cmake](https://cmake.org/) for language server protocol commands (vlsp).
>
> For now only apt(debian/ubuntu based linux), dnf(fedora/centos based linux), pacman(archlinux based linux) and homebrew(macOS) are supported.

For macOS please install [homebrew](https://brew.sh/) as a pre-request.

```bash
$ git clone https://github.com/linrongbin16/vcmd ~/.vcmd && cd ~/.vcmd && ./install.sh
```

The install script will add `~/.vcmd/.vcmdrc` to `~/.bashrc` file.
For other shells, manually add `[ -f ~/.vcmd/.vcmdrc ] && source ~/.vcmd/.vcmdrc` to local rc file, for example `~/.zshrc` on zsh.

#### For Windows

1. Install [python3](https://www.python.org/downloads/), since python3 installer don't provide `python3.exe` or `python3.10.exe`, please manually copy `python.exe` to `python3.exe` and `python3.10.exe`. Make sure `python3.exe` and `pip3.exe` in `$env:Path`.
2. Install [7-zip](https://www.7-zip.org/download.html), add `7z.exe` in `$env:Path`.
3. Install [64-bit Git for Windows Setup](https://git-scm.com/downloads) with below 3 options (this will enable `git.exe` in `$env:Path`, with linux builtin commands such as `bash`, `cp`, `mv`, `cd`, etc):
   1. In the **Select Components** step, enable **Associate .sh files to be run with Bash**.
   2. In the **Adjusting your PATH environment** step, choose **Use Git and optional Unix tools from the Command Prompt**.
   3. In the **Configuring the terminal emulator to use with Git Bash** step, choose **Use Windows's default console window**.
4. Run powershell command as administrator: `git clone https://github.com/linrongbin16/vcmd $env:USERPROFILE/.vcmd && cd $env:USERPROFILE/.vcmd && .\install.ps1`.
5. Manually add `$env:USERPROFILE/.vcmd` to environment variable `$env:Path`.

# Introduction

#### ls

- l - Alias for `ls -lh --color=auto`, list items per line, exclude hidden items.
- ll - Alias for `ls -lah --color=auto`, list items per line, include hidden items.

#### DateTime/Timestamp

- vts - Convert ISO8601 format datetime to unix timestamp.
- vdt - Convert unix timestamp to ISO8601 format datetime.

#### File Operations

- vfec - File encoding operations such as detection and convertion.
- vfty - File operations by file types.

#### Git Operations

- Suggest use [lazygit](https://github.com/jesseduffield/lazygit).

#### Search

- Suggest use [ripgrep](https://github.com/BurntSushi/ripgrep).

#### Encode/Decode

- venc - Encode with [base64](https://en.wikipedia.org/wiki/Base64) and [URL-encoding](https://en.wikipedia.org/wiki/Percent-encoding).
- vdec - Decode with [base64](https://en.wikipedia.org/wiki/Base64) and [URL-encoding](https://en.wikipedia.org/wiki/Percent-encoding).

#### IP Address

- vip - IP Address validation and convertion.

#### Compression and Extraction

- vzip - Files and directories compression.
- vunzip - Files and directories extraction.

#### Proxy

- vprox - Proxy management tools for multiple OS platforms such as Linux/MacOS/Windows, also support git proxy.

#### Language Service Protocol

- vlsp - Generate files for [language server protocol](https://microsoft.github.io/language-server-protocol/) tools, such as [clangd](https://clangd.llvm.org/).

#### SSH Key

- vgenssh - Generate SSH Keys.
