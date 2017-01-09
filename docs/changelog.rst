Changelog
=========

- :feature:`-` add Seafoam logo
- :support:`-` rename from ``minchin.pelican.themes.minchindotca`` to
  ``seafoam``
- :feature:`-` upgrade to FontAwesome 4.7.0
- :feature:`-` upgrade to jQuery 3.1.0
- :bug:`5` switch template variable from ``PAGES`` to ``pages`` to support
  Pelican v3.7 
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
- :support:`-` pull code out of main Minchin.ca repo
