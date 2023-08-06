# -*- coding: utf-8 -*-

__author__ = 'Marek Wywiał'
__email__ = 'onjinx@gmail.com'
__version__ = '0.1.1'

import sys
import subprocess
import os


def run(*args):
    if not args:
        args = sys.argv[1:]

    if len(args) < 2:
        print('Usage: runenv <envfile> <command> <params>')
        sys.exit(0)
    environ = create_env(args[0])

    return subprocess.check_call(
        args[1:], env=environ
    )


def create_env(env_file):
    environ = os.environ
    with open(env_file, 'r') as f:
        for line in f.readlines():
            key, value = line.split('=', 1)
            environ[key] = value
    return environ
