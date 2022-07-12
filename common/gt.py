#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright 2018- <linrongbin16@gmail.com>


def repo_root():
    import common.sys as csys

    outs, _ = csys.run("git rev-parse --show-toplevel")
    return outs[0].strip() if (len(outs) > 0) else None


def check_repo():
    import common.msg as cmsg

    if repo_root() is None:
        cmsg.error("not a git repository, exit...")
        exit(1)


def current_branch():
    import common.sys as csys

    lines, _ = csys.run("git status")
    return lines[0].split(" ")[2].strip()


def modified_files():
    import common.sys as csys

    result, _ = csys.run("git ls-files -m")
    return [modified_file.strip() for modified_file in result]


def untract_files():
    import common.sys as csys

    result, _ = csys.run("git ls-files --others --exclude-standard")
    return [untract_file.strip() for untract_file in result]


def remote_repo_count():
    import common.sys as csys

    repos, _ = csys.run("git remote")
    return len([x.strip() for x in repos])


def remote_repo():
    import common.sys as csys
    import common.msg as cmsg
    import common.util as cutil

    repos, _ = csys.run("git remote")
    repos = [x.strip() for x in repos]
    if len(repos) <= 0:
        return None
    repos_str = ", ".join([f"'{repos[i]}'[{i}]" for i in range(len(repos))])
    select_repo = cmsg.get_input(
        f"choose remote repository {repos_str} (by default 0): ")
    if cutil.str_empty(select_repo):
        repos_str = list(repos)[0]
    else:
        try:
            repos_str = repos[int(select_repo)]
        except:
            cmsg.error(f"unknown selected repository: {select_repo}, exit...")
            exit(1)
    return repos_str


def get_remote_branch():
    import common.sys as csys
    import common.msg as cmsg
    import common.util as cutil

    branches, _ = csys.run("git status")
    branches = [x.strip() for x in branches]
    branch = branches[0].split(" ")[2].strip()
    select_branch = cmsg.get_input(f"choose branch (by default {branch}): ")
    return branch if cutil.str_empty(select_branch) else select_branch


def get_last_commit(n):
    import common.sys as csys

    commits, _ = csys.run("git log --pretty=oneline")
    return commits[n].split(" ")[0]
