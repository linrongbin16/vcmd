# vcmd

A command line utilities separated from [lin.vim](https://github.com/linrongbin16/lin.vim).

# Dependency

python3

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

- l/ll - Alias for `ls`, `l` will exclude hidden files/directories, `ll` will include hidden ones.
- vlsp - Generate files for [language server protocol](https://microsoft.github.io/language-server-protocol/) tools, such as [clangd](https://clangd.llvm.org/).
- vsshgen - Generate SSH Keys.
- venc/vdec - Text encode/decode tool for [base64](https://en.wikipedia.org/wiki/Base64) and [URL-encoding](https://en.wikipedia.org/wiki/Percent-encoding).
- vgp - Grep wrapper for [ripgrep](https://github.com/BurntSushi/ripgrep).
