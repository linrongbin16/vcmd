# Lin Rongbin's dot files

Lin Rongbin's dot files

# Install

```bash
$ git clone https://github.com/linrongbin16/dotfiles ~/.dotfiles
$ cp ~/.dotfiles/.mydotfiles ~/.mydotfiles
$ echo "[ -f ~/.mydotfiles ] && source ~/.mydotfiles" >> ~/.bashrc
```

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
