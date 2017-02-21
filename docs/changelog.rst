Changelog
=========

- :feature:`-` add support for
  `readtime <https://pypi.python.org/pypi/pelican-readtime>` plugin in
  preference to the ``post-stats`` plugin to get artivle reading time. The
  former is availabe on PyPI (as ``pelican-readtime``), while the latter is
  not.
- :support:`2` document optionally supported plugins
- :release:`2.0.4 <2017-01-11>`
- :bug:`10` fix archive page template code to work with Jinja2 v2.9.0
- :release:`2.0.3 <2017-01-11>`
- :bug:`-` fix link color in body area of panel-primary (fixes regression
  from version 2.0.2)
- :release:`2.0.2 <2017-01-11>`
- :bug:`-` fix link color on panel-primary
- :bug:`-` improve layout of generated HTML
- :release:`2.0.1 <2017-01-10>`
- :bug:`8` pluarization of "1 comment" now correct
- :bug:`9` fix pagation template code to work with Jinja2 v2.9.0
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
