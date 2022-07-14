#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright 2018- <linrongbin16@gmail.com>

import platform
import subprocess
import os


def is_Windows():
    return platform.system().lower().startswith("win")


def is_MacOS():
    return platform.system().lower().startswith("darwin")


def run(cmd):
    proc = subprocess.Popen(cmd.split(),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out_bytes = iter(proc.stdout.readline, b"")
    err_bytes = iter(proc.stderr.readline, b"")
    out_lines = [x.decode() for x in out_bytes if len(x) > 0]
    err_lines = [x.decode() for x in err_bytes if len(x) > 0]
    return out_lines, err_lines


def str_empty(s):
    return s is None or len(s.strip()) == 0
