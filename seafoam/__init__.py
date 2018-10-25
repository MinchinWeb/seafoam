# -*- coding: utf-8 -*- #
"""
Seafoam.

This is a Pelican theme. This module is the helper code to go with it.
"""

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path

__version__ = "2.4.1"


def get_path():
    """
    Shortcut for users whose theme is not next to their pelicanconf.py.

    Returns:
        str: filepath to folder containing theme
    """
    # Theme directory is defined as our parent directory
    return str(Path(__file__).resolve().parent)

# TODO: add extension that adds theme version to Pelican metadata
