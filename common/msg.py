#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright 2018- <linrongbin16@gmail.com>

import sys
import traceback


def echo(msg):
    print(f"[vcmd] {msg}")


def debug(msg):
    print(f"[vcmd-debug] {msg}")


def error(msg):
    print(f"[vcmd] Error: {msg}")


def exception(msg):
    print(f"[vcmd] Exception: {msg}")
    traceback.print_exc()


def unknown_option():
    echo(
        f"Unknown option, please try `{sys.argv[0]} --help` for more information"
    )


def from_to(src, dst):
    echo(f"`{src}` => `{dst}`")
