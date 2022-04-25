# zsh theme

# Determines prompt modifier if and when a conda environment is active
my_precmd_info() {
    if [[ -n $CONDA_PREFIX ]]; then
        if [[ $(basename $CONDA_PREFIX) == "miniconda3" ]]; then
            # Without this, it would display conda version
            CONDA_ENV="(base) "
        else
            # For all environments that aren't (base)
            CONDA_ENV="($(basename $CONDA_PREFIX)) "
        fi
    else
        # When no conda environment is active, don't show anything
        CONDA_ENV=""
    fi
    if git status >/dev/null 2>&1; then
        GIT_BRANCH_ENV="(git:$((git symbolic-ref HEAD 2>/dev/null || echo "(unnamed branch)")|cut -d/ -f3-)) "
    else
        GIT_BRANCH_ENV=""
    fi
}

# Run the previously defined function before each prompt
precmd_functions+=( my_precmd_info )

setopt prompt_subst

export PROMPT='%F{yellow}${CONDA_ENV}%f%F{blue}%#%f %F{cyan}%n%f@%F{magenta}%M%f %F{blue}%~%f %F{magenta}${GIT_BRANCH_ENV}%f(%D{%y/%m/%d %a %H:%M}) [%(?.%F{green}√.%F{red}?%?)%f]
%F{blue}>%f '

