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

### Install For Windows

1. Create `$PROFILE` (possibly `$env:UserProfile\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`)
2. Add `l` and `ll` functions implement by [fd-find](https://github.com/sharkdp/fd):

```powershell

function l {
     fd -l -I --max-depth=1
}

function ll {
     fd -l -IH --max-depth=1
}

```
