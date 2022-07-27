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
    import common.msg as cmsg

    if not os.path.exists(src):
        return
    dst = f"{src}.{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}"
    if cmsg.confirm(
            f"'{src}' already exist, move it to {dst} [y(es) - move, n(o) - overwrite]?"
    ):
        os.rename(src, dst)
        cmsg.echo(f"Backup from {src} to {dst}")


def read_file(name):
    fp = open(name, "r")
    data = fp.read()
    fp.close()
    return data


def read_file_by_lines(name):
    fp = open(name, "r")
    lines = fp.readlines()
    fp.close()
    return lines


def write_file(name, text):
    fp = open(name, "w")
    if isinstance(text, list):
        fp.writelines(text)
    else:
        fp.write(text)
    fp.close()


def append_file(name, text):
    fp = open(name, "a+")
    if isinstance(text, list):
        fp.writelines(text)
    else:
        fp.write(text)
    fp.close()


def purge_file(name):
    fp = open(name, "w")
    fp.close()
