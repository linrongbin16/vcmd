#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright 2018- <linrongbin16@gmail.com>

import traceback


def echo(msg):
    print(f"[vcmd] {msg}")


def debug(msg):
    print(f"[vcmd-debug] {msg}")


def exception(msg):
    print(f"[vcmd-exception] {msg}")
    traceback.print_exc()
