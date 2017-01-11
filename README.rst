=======
Seafoam
=======

.. image:: https://raw.githubusercontent.com/MinchinWeb/seafoam/master/docs/seafoam-logo-4x.png
    :align: center
    :alt: Seafoam Logo

``Seafoam`` is a theme for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

The ``seafoam`` theme is based on Bootstrap 3, and was first used at
`Minchin.ca <http://minchin.ca>`_. 

Installation
------------

The easiest way to install the ``seafoam`` theme is through the use
of pip. This will also install the required dependencies automatically.

.. code-block:: sh

  pip install seafoam

Then, in your ``pelicanconf.py`` file, import the module, use the
built in function to specify your theme location, set the default
colour scheme (more options coming soon), add the required plugins, and set
the image processing patterns used:

.. code-block:: python

  import seafoam

  THEME = seafoam.get_path()
  BOOTSTRAP_THEME = 'seafoam'

  PLUGINS = ['minchin.pelican.jinja_filters',
             'minchin.pelican.plugins.image_process',
             # others, as desired...
             ]

  IMAGE_PROCESS = {
    'article-feature': ["scale_in 848 848 True"],
    'index-feature': ["scale_in 263 263 True"],
  }

  # the rest of the your configuration file...


You will may also need to configure the theme through the use of additional
settings (see below).


Requirements
------------

``Seafoam`` requires Pelican and the ``image_process`` and
the ``jinja filters`` plugin. If the theme is installed from pip, these
should be automatically installed. If needed they can be manually
installed with pip:

.. code-block:: sh

   pip install pelican
   pip install minchin.pelican.plugins.image_process
   pip install minchin.pelican.jinja_filters


Additional Settings
-------------------

Details coming. In the meantime, refer to the settings on the `Bootstrap 3
theme <https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3>`_.


Credits
-------

Original theme developed by `Daan Debie <http://dandydev.net/>`_.

The idea that a theme could be installed as a Python package by `Jeff
Forcier <http://bitprophet.org/>`_'s `Alabaster theme
<https://github.com/bitprophet/alabaster>`_ for Sphinx.
