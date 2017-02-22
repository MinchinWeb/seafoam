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


Supported Plugins
-----------------

Seafoam works with several other plugins for Pelican, but none of those
listed in this section are required.

- `readtime <https://pypi.python.org/pypi/pelican-readtime>`_ -- provides estimated reading time for articles. Available from PyPI as ``pelican-readtime``.
- `post-stats <https://github.com/getpelican/pelican-plugins/tree/master/post_stats>`_ -- provides estimated reading time for articles if `readtime` is not available. Available in the `Pelican Plugins collection <https://github.com/getpelican/pelican-plugins/>`_.
- `neigbours <https://pypi.python.org/pypi/pelican-neighbors>`_ -- provides post-article links to the next and previous  article on your blog and the next and previous article in that category. Available on PyPI as ``pelican-neighours``.
- `pelican_comment_system <https://bernhard.scheirle.de/posts/2014/March/29/static-comments-via-email/>`_ -- add static comments to your blog. Available in the `Pelican Plugins collection <https://github.com/getpelican/pelican-plugins/>`_.


Additional Settings
-------------------

These settings can be set in your `pelicanconf.py` file (your Pelican settings
file) to alter the behaviour of the theme.

.. use the ".. data::" directive here for Sphinx output, but on GitHub, that just causes everything to disappear

PAGINATOR_LIMIT = 8
  Number of page number links to appear of the main "index" page of your
  blog. The default of 8 results in showing a link to page 1, links the
  three previous pages (8 divided by 2 and rounded down), a number
  representing the current page, links to the next three pages, and a link
  to the last page.

The above list is not yet complete. In the meantime, refer to the settings on
the `Bootstrap 3 theme <https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3>`_.

It may also be helpful to review the
`settings for Pelican itself <http://docs.getpelican.com/en/3.7.1/settings.html>`_.


Credits
-------

Original theme developed by `Daan Debie <http://dandydev.net/>`_.

The idea that a theme could be installed as a Python package by `Jeff
Forcier <http://bitprophet.org/>`_'s `Alabaster theme
<https://github.com/bitprophet/alabaster>`_ for Sphinx.
