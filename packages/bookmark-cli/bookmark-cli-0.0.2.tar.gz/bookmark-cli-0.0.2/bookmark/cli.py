#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
"""

"""

import argparse
from .bookmark import add_bookmark
from .bookmark import list_bookmarks
from .bookmark import delete_bookmark

def init_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', nargs='?')
    parser.add_argument('text', nargs='?', default='')
    parser.add_argument('--tags', nargs='+')
    return parser

def add(arg):
    add_bookmark(arg.text, arg.tags)
    print(f'Created bookmark {arg.text}')
    return

def ls(arg):
    bookmarks = list_bookmarks(arg.tags) or []
    for bm in bookmarks:
        print(bm.text)

def list(arg):
    bookmarks = list_bookmarks(arg.tags) or []
    for bm in bookmarks:
        print(bm.text, ','.join(bm.tags))

def delete(arg):
    count = delete_bookmark(arg.text)
    print(f'Delete {arg.text}')

def main():
    import sys
    parser = init_argparse()
    arg = parser.parse_args()

    cmd = arg.cmd
    if not cmd:
        cmd = 'list'

    func = getattr(sys.modules[__name__], cmd)
    func(arg)

if __name__ == "__main__":
    main()
