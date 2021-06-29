# -*- coding: utf-8 -*- #
"""
Seafoam.

This is a Pelican theme. This module is the helper code to go with it.
"""

from pathlib import Path

from pelican import signals

from .initialize import seafoam_version


def get_path():
    """
    Shortcut for users whose theme is not next to their pelicanconf.py.

    Returns
    -------
        str: filepath to folder containing theme

    """
    # Theme directory is defined as our parent directory
    return str(Path(__file__).resolve().parent)


def register():
    """Register the plugin pieces with Pelican."""
    signals.initialized.connect(seafoam_version)
