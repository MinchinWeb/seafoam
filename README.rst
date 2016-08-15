====================
Minchin dot CA Theme
====================

``Minchin dot CA`` is a theme for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

The ``Minchin dot CA`` theme is based on Bootstrap 3, and was first used at
`Minchin.ca <http://minchin.ca>`_. 

Installation
============

The easiest way to install the ``Minchin dot CA`` theme is through the use
of pip. This will also install the required dependencies automatically.

.. code-block:: sh

  pip install minchin.pelican.themes.minchindotca

Then, in your ``pelicanconf.py`` file, import the modele, and then use the
built in function to specify your theme location:

.. code-block:: python

  from minchin.pelican.themes import minchindotca

  THEME = minchindotca.get_path()


You will may also need to configure the theme through the use of additional
settings (see below).


Requirements
============

``Minchin dot ca`` requires Pelican.
This can be manually installed with pip:

.. code-block:: sh

   pip install pelican


Additional Settings
===================

Details coming. In the meantime, refer to the settings on the `Bootstrap 3
theme <https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3>`_.


Credits
-------

Original theme developed by `Daan Debie <http://dandydev.net/>`_.

The idea that a theme could be installed as a Python package by `Jeff
Forcier <http://bitprophet.org/>`_'s `Alabaster theme
<https://github.com/bitprophet/alabaster>`_ for Sphinx.
