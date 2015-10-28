#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
from arguman import Arguman
from models import Argument, User


def main():
    arguman = Arguman()
    arguments = arguman.get_arguments()
    for argument in arguments:
        print('%s: %s' % (argument.user.username, argument.title))


if __name__ == '__main__':
    main()
