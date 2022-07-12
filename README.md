# vcmd

A command line utilities separated from [lin.vim](https://github.com/linrongbin16/lin.vim).

# Install

### For bash

```bash
$ git clone https://github.com/linrongbin16/vcmd ~/.vcmd
$ echo "[ -f ~/.vcmd/.vcmdrc ] && source ~/.vcmd/.vcmdrc " >> ~/.bashrc
```

### For other shell

Please manually add `source ~/.vcmd/.vcmdrc` to local rc file if you're using other shell: zsh, fish, etc.

### For non-posix shell (Windows)

Please manually add `~/.vcmd` to environment variable **PATH**, for Windows it's `$env:Path`.
