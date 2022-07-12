#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright 2018- <linrongbin16@gmail.com>

import os
import datetime
import sys

sys.path.append(".")


def list_files(directory, include_hidden=False, depth=99):
    saved = os.getcwd()
    os.chdir(directory)
    start = os.getcwd()
    results = []
    for root, ds, fs in os.walk(start):
        if not include_hidden:
            fs[:] = [f for f in fs if not f.startswith(".")]
            ds[:] = [d for d in ds if not d.startswith(".")]
        start_slashes = start.count("/") + start.count("\\")
        root_slashes = root.count("/") + root.count("\\")
        if root_slashes - start_slashes > depth:
            continue
        results.extend([os.path.join(root, f) for f in fs])
    if os.path.exists(saved):
        os.chdir(saved)
    return results


def list_dirs(directory, include_hidden=False, depth=99):
    saved = os.getcwd()
    os.chdir(directory)
    start = os.getcwd()
    results = []
    for root, ds, fs in os.walk(start):
        if not include_hidden:
            fs[:] = [f for f in fs if not f.startswith(".")]
            ds[:] = [d for d in ds if not d.startswith(".")]
        start_slashes = start.count("/") + start.count("\\")
        root_slashes = root.count("/") + root.count("\\")
        if root_slashes - start_slashes > depth:
            continue
        results.extend([os.path.join(root, d) for d in ds])
    if os.path.exists(saved):
        os.chdir(saved)
    return results


def valid_dir(d):
    return os.path.exists(d) and os.path.isdir(d)


def valid_file(f):
    return os.path.exists(f) and os.path.isfile(f)


def backup(src):
    if not os.path.exists(src):
        return
    dst = f"{src}.{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
    os.rename(src, dst)

    import msg
    msg.echo(f"Backup from {src} to {dst}")
