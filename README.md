# vcmd

A command line utilities implemented by python3.

Separated from [lin.vim](https://github.com/linrongbin16/lin.vim).

# Dependency

- [python3](https://www.python.org/)
- Optional [pytz](https://pypi.org/project/pytz/) for datetime and timestamp commands: vts, vdt.
- Optional [chardetect](https://pypi.org/project/chardet/) for file encoding commands: vfec.
- Optional [ripgrep](https://github.com/BurntSushi/ripgrep) for grep commands: vgrep.
- Optional [git](https://git-scm.com/) for git commands: vgpl, vgps, etc.
- Optional [p7zip](http://p7zip.sourceforge.net/) (or [7-Zip](https://www.7-zip.org/download.html) on Windows) for compression commands: vzip, vunzip.
- Optional [openssh](https://www.openssh.com/) for SSH commands: vsshgen.
- Optional [cmake](https://cmake.org/) for language server protocol commands: vlsp.

# Install

### For bash

```bash
$ git clone https://github.com/linrongbin16/vcmd ~/.vcmd
$ echo "[ -f ~/.vcmd/.vcmdrc ] && source ~/.vcmd/.vcmdrc " >> ~/.bashrc
```

### For other shells

Please manually add `source ~/.vcmd/.vcmdrc` to local rc file if you're using other shell: zsh, fish, etc.

### For non-posix systems

Please manually add `~/.vcmd` to environment variable **PATH**, for Windows it's `$env:Path`.

# Introduction

### ls

- l - Alias for `ls -lh --color=auto`, list items per line, exclude hidden items.
- ll - Alias for `ls -lah --color=auto`, list items per line, include hidden items.

### DateTime/Timestamp

- vts - Convert ISO8601 format datetime to unix timestamp.
- vdt - Convert unix timestamp to ISO8601 format datetime.

### File Operations

- vfec - File encoding operations such as detection and convertion.
- vft - File operations by file types.

### Grep

- vgrep - Grep wrapper for [ripgrep](https://github.com/BurntSushi/ripgrep).

### Interactively Git Operations

- vgpl - Git pull.
- vgps - Git push.
- vgbr - Git branch operations.
- vgdsc - Git discard.
- vgrst - Git reset.
- vgrvt - Git revert.

### Encode/Decode

- venc - Encode with [base64](https://en.wikipedia.org/wiki/Base64) and [URL-encoding](https://en.wikipedia.org/wiki/Percent-encoding).
- vdec - Decode with [base64](https://en.wikipedia.org/wiki/Base64) and [URL-encoding](https://en.wikipedia.org/wiki/Percent-encoding).

### IP Address

- vip - IP Address validation and convertion.

### Compression and Extraction

- vzip - Compression.
- vunzip - Extraction.

### Proxy

- vprx - Proxy management tools for multiple OS platforms such as Linux/MacOS/Windows, also support git proxy.

### Language Service Protocol

- vlsp - Generate files for [language server protocol](https://microsoft.github.io/language-server-protocol/) tools, such as [clangd](https://clangd.llvm.org/).

### SSH Key Helper

- vsshgen - Generate SSH Keys.
