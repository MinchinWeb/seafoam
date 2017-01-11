# -*- coding: utf-8 -*- #
"""
Seafoam
=======

This is a Pelican theme. This is the helper code to go with it.
"""

from pathlib import Path

__version__ = "2.0.3"


def get_path():
    """
    Shortcut for users whose theme is not next to their pelicanconf.py.
    """
    # Theme directory is defined as our parent directory
    return(str(Path(__file__).parent))

# TO-DO: add extension that adds theme version to Pelican metadata
