# -*- coding: utf-8 -*- #
"""
MinchinDotCa
=============

This is a Pelican theme. This is the helper code to go with it.
"""

import os


__version__ = '1.0.0'

def get_path():
    """
    Shortcut for users whose theme is not next to their pelicanconf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# TO-DO: add extension that adds theme version to Pelican metadata
