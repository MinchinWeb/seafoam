Changelog
=========

.. Added, Changed, Depreciated, Removed, Fixed, Security

- :release:`2.2.1 <2017-11-13>`
- :bug:`-` fix reference to ``python-dateutil`` in project metadata
- :release:`2.2.0 <2017-11-13>`
- :feature:`-` include prjct template
- :feature:`15` include 404 template
- :feature:`-` use ``NAVBAR_ON_TOP`` to move the menu from the left side of the
  page to the top (Bootstrap default)
- :bug:`- major` respect Pelican's ``THEME_STATIC_DIR`` setting
- :support:`-` use ``minchin.releaser`` to put out releases
- :release:`2.1.5 <2017-05-31>`
- :bug:`11` indent definition list items
- :bug:`-` note that Image Processing v1.1.2 is broken (see
  [issue 32](https://github.com/MinchinWeb/minchin.pelican.plugins.image_process/issues/2))
- :release:`2.1.4 <2017-04-09>`
- :bug:`-` ``Framework :: Pelican :: Themes`` trove classifier on PyPI now
  available.
- :release:`2.1.3 <2017-03-19>`
- :support:`2 (==2.1.3)` document most theme options
- :release:`2.1.2 <2017-03-08>`
- :bug:`-` provide universal wheels. On versions of Python before 3.4 (when the
  ``pathlib`` module was added to the standard library), we now depend on
  `pathlib2 <https://pypi.python.org/pypi/pathlib2>`_.
- :bug:`-` provide an absolute path.
- :release:`2.1.1 <2017-03-08>`
- :bug:`-` fix pagination links on category and tag pages. See `this issue
  <https://github.com/MinchinWeb/blog.minchin.ca/issues/6>`_.
- :bug:`13` remove unused code in pagination template. Thanks
  `@jorgesumle <https://github.com/jorgesumle>`_
- :release:`2.1.0 <2017-02-20>`
- :feature:`-` add support for
  `readtime <https://pypi.python.org/pypi/pelican-readtime>` plugin in
  preference to the ``post-stats`` plugin to get article reading time. The
  former is available on PyPI (as ``pelican-readtime``), while the latter is
  not.
- :support:`2` document optionally supported plugins
- :release:`2.0.4 <2017-01-11>`
- :bug:`10` fix archive page template code to work with Jinja2 v2.9.0
- :release:`2.0.3 <2017-01-11>`
- :bug:`-` fix link colour in body area of panel-primary (fixes regression
  from version 2.0.2)
- :release:`2.0.2 <2017-01-11>`
- :bug:`-` fix link colour on panel-primary
- :bug:`-` improve layout of generated HTML
- :release:`2.0.1 <2017-01-10>`
- :bug:`8` pluralization of "1 comment" now correct
- :bug:`9` fix pagination template code to work with Jinja2 v2.9.0
- :release:`2.0.0 <2017-01-09>`
- :feature:`-` add Seafoam logo
- :support:`-` [BREAKING] rename from
  ``minchin.pelican.themes.minchindotca`` to ``seafoam``
- :feature:`-` add support for reading time via `post stats
  <https://github.com/getpelican/pelican-plugins/tree/master/post_stats>`_
  plugin
- :bug:`6 major` restyle comments with bootstrap's ``media`` class (much
  cleaner template code)
- :feature:`-` add support for `pelican comment system
  <https://github.com/getpelican/pelican-plugins/tree/master/pelican_comment_system>`_
- :feature:`-` upgrade to FontAwesome 4.7.0
- :feature:`-` upgrade to jQuery 3.1.0
- :bug:`5 major` switch template variable from ``PAGES`` to ``pages`` to
  support Pelican v3.7 
- :feature:`-` switch to ``minchin.pelican.jinja_filters`` to provide
  the required Jinja filters, rather than requiring them to be manually
  added to the user's configuration file
- :bug:`-` don't print section for next and previous posts in a category if
  the article is the only one in that category
- :feature:`-` add support for Pelican Blog System
- :release:`1.1.0 <2016-09-12>`
- :feature:`-` include (thumbnail of) featured image on article listing
- :support:`-` start documentation with the changelog (this file)
- :bug:`-` Better handling for copyright and modified dates in `footer.html`
- :feature:`-` add breadcrumbs to main blog post listing page
- :support:`-` add release machinery
- :release:`1.0.0 <2016-08-15>`
- :feature:`-` add 'setup.py', 'README.rst', 'CHANGELOG.rst'
- :support:`-` move package to 'minchin.pelican.themes.minchindotca'
- :support:`-` pull code out of main Minchin.ca website repo
