# vcmd

A command line utilities implemented by python3.

Separated from [lin.vim](https://github.com/linrongbin16/lin.vim).

# Install

#### Dependencies

The install script will install these softwares if not exists (by system package manager: apt/dnf/brew/pacman/etc):

- [python3](https://www.python.org/)
  - [click](https://click.palletsprojects.com/) command argument parsing.
  - [pytz](https://pypi.org/project/pytz/) for datetime and timestamp commands (vts/vdt).
  - [chardet](https://pypi.org/project/chardet/) for file encoding commands (vfec).
- [git](https://git-scm.com/) for git commands (vgpl/vgps/etc).
- [bzip2](https://www.sourceware.org/bzip2/), [unzip](https://linux.die.net/man/1/unzip), [p7zip](http://p7zip.sourceforge.net/) for compression commands (vzip/vunzip).
  - For Windows: [bzip2 for windows](http://gnuwin32.sourceforge.net/packages/bzip2.htm), [unzip for Windows](http://gnuwin32.sourceforge.net/packages/unzip.htm), [7-zip](https://www.7-zip.org/download.html).
- [openssh](https://www.openssh.com/) for SSH commands (vsshgen).
- [cmake](https://cmake.org/) for language server protocol commands (vlsp).

#### For UNIX/Linux/MacOS

Install [git](https://git-scm.com/) as a pre-request, additionally install [homebrew](https://brew.sh/) for MacOS.

```bash
$ git clone https://github.com/linrongbin16/vcmd ~/.vcmd && bash ~/.vcmd/install
```

The install script will add `~/.vcmd/.vcmdrc` to `~/.bashrc` file.
For other shells, manually add `[ -f ~/.vcmd/.vcmdrc ] && source ~/.vcmd/.vcmdrc` to local rc file, for example `~/.zshrc` on zsh.

#### For Windows

1. Install [python3](https://www.python.org/downloads/).
2. Install [64-bit Git for Windows Setup](https://git-scm.com/downloads) with these options (this will enable `git.exe` on environment variable `$env:Path`, with most linux shell commands such as `bash`, `cp`, `mv`, `cd`, etc):
   1. In the 3rd step **_Select Components_**, enable **_Associate .sh files to be run with Bash_**
   2. In the 7th step **_Adjusting your PATH environment_**, choose **_Use Git and optional Unix tools from the Command Prompt_**
   3. In the 11th step **_Configuring the terminal emulator to use with Git Bash_**, choose **_Use Windows's default console window_**
3. Run command: `git clone https://github.com/linrongbin16/vcmd ~/.vcmd && bash ~/.vcmd/install.ps1`.
4. Manually add `$env:USERPROFILE/.vcmd` to environment variable `$env:Path`.
5. Optionally install below for compression/extraction commands (vzip/vunzip):
   - [bzip2 for windows](http://gnuwin32.sourceforge.net/packages/bzip2.htm).
   - [unzip for Windows](http://gnuwin32.sourceforge.net/packages/unzip.htm).
   - [7-zip](https://www.7-zip.org/download.html).

# Introduction

#### ls

- l - Alias for `ls -lh --color=auto`, list items per line, exclude hidden items.
- ll - Alias for `ls -lah --color=auto`, list items per line, include hidden items.

#### DateTime/Timestamp

- ts - Convert ISO8601 format datetime to unix timestamp.
- dt - Convert unix timestamp to ISO8601 format datetime.

#### File Operations

- fec - File encoding operations such as detection and convertion.
- fty - File operations by file types.

#### Git Operations

- gs - Short for `git status`.
- gp - Short for `git pull`.
- gps - Short for `git push`.
- gb - Short for `git branch`.
- ga - Short for `git add`.
- gc - Short for `git commit`.
- gck - Short for `git checkout`.
- grs - Short for `git reset`.
- grv - Short for `git revert`.

#### Search

- Suggest use [ripgrep](https://github.com/BurntSushi/ripgrep).

#### Encode/Decode

- ec - Encode with [base64](https://en.wikipedia.org/wiki/Base64) and [URL-encoding](https://en.wikipedia.org/wiki/Percent-encoding).
- dc - Decode with [base64](https://en.wikipedia.org/wiki/Base64) and [URL-encoding](https://en.wikipedia.org/wiki/Percent-encoding).

#### IP Address

- ip - IP Address validation and convertion.

#### Compression and Extraction

- cmpr - Compression.
- extr - Extraction.

#### Proxy

- prx - Proxy management tools for multiple OS platforms such as Linux/MacOS/Windows, also support git proxy.

#### Language Service Protocol

- lsp - Generate files for [language server protocol](https://microsoft.github.io/language-server-protocol/) tools, such as [clangd](https://clangd.llvm.org/).

#### SSH Key Helper

- vsshgen - Generate SSH Keys.
