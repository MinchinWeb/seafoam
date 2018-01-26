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

  # Generate 404 error page
  TEMPLATE_PAGES = {
      '404.html':     '404.html',
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
- `neighbors <https://pypi.python.org/pypi/pelican-neighbors>`_ -- provides post-article links to the next and previous  article on your blog and the next and previous article in that category. Available on PyPI as ``pelican-neighours``.
- `pelican_comment_system <https://bernhard.scheirle.de/posts/2014/March/29/static-comments-via-email/>`_ -- add static comments to your blog. Available in the `Pelican Plugins collection <https://github.com/getpelican/pelican-plugins/>`_.
- `Related Posts <https://github.com/getpelican/pelican-plugins/tree/master/related_posts>`_ -- adds the related_posts variable to the article's context.
- Tipue Search


Additional Settings
-------------------

These settings can be set in your ``pelicanconf.py`` file (your Pelican settings
file) to alter the behavior of the theme.

If a value is given below, this represents the effective default value. If no
value is given, the effective default value is `None`.

If you are using this theme on a sub-site (i.e a directory of the "main site"),
look at ``MENUITEMS_2``, ``MENUITEMS_2_AT``, and ``MENUITEMS_2_AT_LINK``
settings.

If you are using this theme on a subdomain, look at the ``SITE_ROOT_URL``
setting.

This documentation has to be manually updated. If the settings no longer match
the theme's behavior, or a setting is missing from here, please open a ticket
on `GitHub <https://github.com/MinchinWeb/seafoam/issues>`_.

.. use the ".. data::" directive here for Sphinx output, but on GitHub, that just causes everything to disappear

ABOUT_ME
  You can show a short blurb of text about yourself and a picture. This setting
  is the paragraph. Raw HTML is accepted. See the ``AVATAR`` setting to set the
  picture.
ADAM
  These ADAM settings were originally set up to support my genealogy sub-site
  (the original name of the the pre-processor I was using as called "Adam"). If
  this is set to ``False``, the rest of the ADAM_* settings won't be active.
  These settings are probably generic enough that you could use these for any
  generator or outside program used to help generate your site.
ADAM_COPY_DATE
  Override the copyright date in the footer. (Provide a string).
ADAM_FOOTER
  An extra "page footer" to apply to all pages. (Provide an HTML string.)
ADAM_LINK
  Link target for the Adam version text.
ADAM_UPDATED
  Override the updated date.
ADAM_VERSION
  Reported name and version of "Adam". 
ADDTHIS_PROFILE
  You can enable sharing buttons through `AddThis <http://www.addthis.com/>`_
  by this setting to your AddThis profile-id. This will display a Tweet,
  Facebook Like and Google +1 button under each post.
ARCHIVES_URL
  Same as the regular Pelican setting.
ASSET_CSS
  Set to ``True`` if you want the ``asset`` plugin to compile your CSS.
ASSET_JS
  Set to ``True`` if you want the ``asset`` plugin to compile your Javascript.
AUTHOR
  Who to list as the copyright belonging to in the site footer.
AUTHORS_URL
  Same as the regular Pelican setting.
AVATAR
  You can show a short blurb of text about yourself and a picture. This setting
  is the path to the picture. See the ``ABOUT_ME`` setting to set the
  descriptive paragraph.
BOOTSTRAP_NAVBAR_INVERSE = False
  Apply inverse CSS setting to Navbar.
BOOTSTRAP_THEME
  Set this to `seafoam`. Other values (including leaving this unset) are not
  expected to work correctly.
CATEGORIES_URL
  Same as the regular Pelican setting.
CATEGORY_IMAGES
  Provide a default featured image by category. If an image is set in the
  article metadata, that will override this.

  Provide a dictionary where the key is the category name and the value is the
  path of the image, relative to the SITEURL.
CC_ATTR_MARKUP
  Optionally, you can include attribution markup in the CC license mark by
  setting this to ``True``.
CC_LICENSE
  Set a site-wide Creative Commons License by specify the "short name" of the
  license (like ``CC_BY``, or ``CC-BY-NC-ND``). Alternately, use
  ``CC_LICENSE_COMMERCIAL`` and ``CC_LICENSE_DERIVATIVES`` to "build a
  license".
CC_LICENSE_COMMERCIAL
  "yes" if commercial use is permitted, "no" otherwise. Use this in lieu of
  ``CC_LICENSE`` and in combination with ``CC_LICENSE_DERIVATIVES`` to "build a
  license".
CC_LICENSE_DERIVATIVES
  "yes" is derivatives are permitted, "no" otherwise. Use this in lieu of
  ``CC_LICENSE`` and in combination with ``CC_LICENSE_COMMERCIAL`` to "build a
  license".
CUSTOM_CSS
  Link, relative to SITEURL, to a custom CSS file.
CUSTOM_CSS_LIST
  Custom CSS to load; can be either absolute links, or relative links. If the
  listed item starts with ``//``, ``http://``, ``https://``, it is assumed to
  be absolute link and added as-is to the markup. Otherwise, the link is
  assumed to be relative to SITEURL.
CUSTOM_JS_LIST
  Custom Javascript to load; can be either scripts, absolute links, or relative
  links. If the listed item starts with ``<script``, then the item is assumed
  to be the contents of a script, including opening and closing tags, and so
  added to the pages' markup directly. If the listed item starts with ``//``,
  ``http://``, ``https://``, it is assumed to be absolute link and added as-is
  to the markup. Otherwise, the link is assumed to be relative to SITEURL.
DEFAULT_LANG
  .
DISPLAY_BREADCRUMBS = False
  Display Breadcrumbs on site.

  See also ``MENUITEMS_2_AT`` and ``MENUITEMS_2_AT_LINK`` settings.
DISPLAY_CATEGORIES_ON_MENU
  Include categories on the main site menu.
DISPLAY_CATEGORIES_ON_SIDEBAR
  Include a listing of categories on the sidebar (assuming the sidebar is
  active; see ``HIDE_SIDEBAR`` setting)
DISPLAY_PAGES_ON_MENU
  Include a listing of pages on the sidebar (assuming the sidebar is active;
  see ``HIDE_SIDEBAR`` setting)
DISPLAY_RECENT_POSTS_ON_SIDEBAR
  Include a listing of recent posts on the sidebar (assuming the sidebar is
  active; see ``HIDE_SIDEBAR`` setting). Also see the ``RECENT_POST_COUNT``
  setting.
DISPLAY_TAGS_INLINE
  .
DISPLAY_TAGS_ON_SIDEBAR = True
  Include a listing of tags on the sidebar (assuming the sidebar is active;
  see ``HIDE_SIDEBAR`` setting)
DISQUS_DISPLAY_COUNTS
  Display the number of comments (assuming Disqus comments are active; see
  ``DISQUS_SITENAME`` settings)
DISQUS_ID_PREFIX_SLUG
  Set this to ``True`` if you have configured your article URLs such that the
  slug alone will likely not be unique. Ignored if ``DISQUS_NO_ID`` is ``True``.
DISQUS_NO_ID
  This theme sets identifiers for each article's comment threads. If you are
  switching from a theme that doesn't (such as the Pelican built-in default)
  this will result in existing comments getting lost. To prevent this, set
  this setting to ``True``.
DISQUS_SITENAME
  Set to your Disqus sitename to activate Disqus comments on your site.

  You can also enable Disqus comments for pages. This is a per-page setting you
  can control by adding a field comments to you pages' metadata. Set it to
  enabled to enable comments for that page. Comment-threads for pages will have
  an id that is prefixed by ``page-``.

  You will probably only use this or the Pelican Comment System; odd results
  may come if you try to use both together. See the ``PELICAN_COMMENT_SYSTEM``
  setting.
DOCUTIL_CSS
  If you're using reStructuredText for writing articles and pages, you can
  include the extra CSS styles that are used by the docutils-generated HTML by
  setting this to ``True``. This can be done as a global setting or setting it
  in the metadata of a specific article or page.
FAVICON
  The location of your site's FavIcon, relative to the SITEURL.
FEED_ALL_ATOM
  Same as the regular Pelican setting. If set, a link to your Atom feed will
  appear in the site's HTML header and as a link in the footer of the site.
FEED_ALL_RSS
  Same as the regular Pelican setting. If set, a link to your RSS feed will
  appear in the site's HTML header.
GITHUB_REPO_COUNT = 5
  See ``GITHUB_USER`` setting.
GITHUB_SHOW_USER_LINK
  See ``GITHUB_USER`` setting.
GITHUB_SKIP_FORK = False
  See ``GITHUB_USER`` setting.
GITHUB_USER
  The theme can show your most recently active GitHub repos in the sidebar. To
  enable, set this to you GitHub username. Appearance and behavior can be
  controlled using the ``GITHUB_REPO_COUNT``, ``GITHUB_SKIP_FORK``, and 
  ``GITHUB_SHOW_USER_LINK`` variables.
GOOGLE_ANALYTICS
  Used to activate "classic" Google Analytics. Set this to your account's Google
  Analytics ID. Although this setting doesn't conflict with
  ``GOOGLE_ANALYTICS_UNIVERSAL``, you will in most cases only use one or the
  other.
GOOGLE_ANALYTICS_UNIVERSAL
  Used to activate "universal" Google Analytics (this is the new version). Set
  this to your account's ID (a number). Also set
  ``GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY``. Although this setting doesn't
  conflict with ``GOOGLE_ANALYTICS``, you will in most cases only use one or
  the other.
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY
  Set this to the Google Analytics "property" this site represents. See also
  (and set) ``GOOGLE_ANALYTICS_UNIVERSAL``.
HIDE_SIDEBAR = False
  Hide the sidebar, and all it's contents. Also review the settings
  ``DISPLAY_CATEGORIES_ON_SIDEBAR``, ``DISPLAY_RECENT_POSTS_ON_SIDEBAR``,
  ``DISPLAY_TAGS_ON_SIDEBAR``, ``GITHUB_USER``, ``LINKS``, and
  ``TWITTER_USERNAME`` variables.
HIDE_SITENAME = False
  Hide the sitename in the site navbar.
INDEX_COPY_DATE
  Copyright date to display on the index page (homepage) of the site.
JQUERY_JS_IN_HEAD = False
  Bootstrap depends on JQuery. Typically, good practice is to load all your
  Javascript from the end of your page. However, in certain cases, I've needed
  to load JQuery sooner. So this moves loading JQuery from the end of the page
  to the header.
LINKS
  Extra links to display sidebar. Provide a list of tuples of the form
  ``('name', 'link')``.
MENUITEMS
  Extra items to add to the menu. Provide a list of tuples of the form
  ``(title, link, icon)``. ``link`` is absolute, so build them using SITEURL, 
  if needed. ``icon`` here is of the form of the CSS classes to be used; e.g.
  ``'fa fa-fw fa-pencil'``. ``icon`` can be set to ``None``.

  If this is set, the working assumption is that the site you are generating is
  a "sub-site".
MENUITEMS_2
  Extra items you want added as a sub-menu. Use in conjunction with the
  ``MENUITEMS_2_AT`` setting. Provide a list of tuples of the form
  ``(title, link, icon)``. ``link`` is absolute, so build them using SITEURL, 
  if needed. ``icon`` here is of the form of the CSS classes to be used; e.g.
  ``'fa fa-fw fa-pencil'``. ``icon`` can be set to ``None``.

  This setting is working on the assumption that your generated site in going
  into a subdirectory of your "main" site.
MENUITEMS_2_AT
  If ``MENUITEMS_2`` is set, under which (main) menu item are these to be
  displayed. This should match a "name" of one of the items on ``MENUITEMS``;
  if no match is found, these sub-menu items will not be displayed.

  When set and Breadcrumbs are enabled, all items on the site are shown to be
  under both "home" (linked to at the ``SITE_ROOT_URL``) and ``MENUITEMS_2_AT``
  (linked to at ``MENUITEMS_2_AT_LINK``).
MENUITEMS_2_AT_LINK
  When set and Breadcrumbs are enabled, all items on the site are shown to be
  under both "home" (linked to at the ``SITE_ROOT_URL``) and ``MENUITEMS_2_AT``
  (linked to at ``MENUITEMS_2_AT_LINK``).
NAVBAR_ON_TOP
  If True, the navigation menu is on top. If False, the navigation menu is
  vertical on the left side of the page. Default is False.
NEIGHBORS
  Activates the links to the next and previous articles, both in the "all
  posts" index and the category-specific index. Requires the
  `neighbors <https://pypi.python.org/pypi/pelican-neighbors>`_ to be both
  installed and activated (i.e. listed under ``PLUGINS``).
OPEN_GRAPH_FB_APP_ID
  You can use this setting to provide a Facebook *app id*. See the
  ``USE_OPEN_GRAPH`` setting.
OPEN_GRAPH_IMAGE
  A default image to use with Open Graph. This is a filepath relative to your
  SITEURL. See the ``USE_OPEN_GRAPH`` setting.
PAGINATOR_LIMIT = 8
  Number of page number links to appear of the main "index" page of your
  blog. The default of 8 results in showing a link to page 1, links the
  three previous pages (8 divided by 2 and rounded down), a number
  representing the current page, links to the next three pages, and a link
  to the last page.
PDF_PROCESSOR
  .
PELICAN_COMMENT_SYSTEM = False
  Set this to ``True`` to active the
  `pelican_comment_system <https://bernhard.scheirle.de/posts/2014/March/29/static-comments-via-email/>`_.

  The Pelican Comment System has
  `further settings <https://github.com/Scheirle/pelican_comment_system/blob/master/doc/installation.md>`_
  that are not used directly by the theme.

  You will probably only use this or Disqus; odd results may come if you try to
  use both together. See the ``DISQUS_SITENAME`` setting.
PELICAN_COMMENT_SYSTEM_DISPLAY_COUNTS = True
  Whether to display the number of comments
PELICAN_COMMENT_SYSTEM_EMAIL_DOMAIN
  The domain name of the email where you want the comments to be emailed to
  (i.e. the part after the ``@`` sign). See the
  ``PELICAN_COMMENT_SYSTEM_EMAIL_USER`` and ``PELICAN_COMMENT_SYSTEM``
  settings.
PELICAN_COMMENT_SYSTEM_EMAIL_USER
  The username of the email where you want the comments to be emailed to (i.e.
  the part before the ``@`` sign). See the
  ``PELICAN_COMMENT_SYSTEM_EMAIL_DOMAIN`` and ``PELICAN_COMMENT_SYSTEM``
  setting.
PELICAN_COMMENT_SYSTEM_FEED, PELICAN_COMMENT_SYSTEM_FEED_ALL
  Used internally to generate links to the Comment RSS/Atoms feeds.
PELICAN_COMMENT_SYSTEM_IDENTICON_SIZE = 72
  The size of the Identicons generated by the Pelican Comment System.
PIWIK_SITE_ID
  Used for Piwik site analytics.
PIWIK_SSL_URL = PIWIK_URL
  Used for Piwik site analytics.
PIWIK_URL
  Used for Piwik site analytics.
PLUGINS
  Same as the regular Pelican setting.
PRJCT
  Set to ``TRUE`` to active `prjct <https://github.com/MinchinWeb/prjct>`_
  support. Recommended segment to include in your ``pelicanconf.py``:

  ```
  import prjct

  PRJCT = True
  PRJCT_TODO, PRJCT_DONE = prjct.todo_export.to_html_dicts()
  PRJCT_PROJECTS = prjct.multi_source.project_list()
  PRJCT_ACTIVE_PROJECTS = prjct.multi_source.active_project_list()
  PRJCT_SOMEDAY_PROJECTS = prjct.config.someday_projects()
  PRJCT_COMPLETED_PROJECTS = prjct.config.completed_projects()
  PRJCT_DESC = prjct.descriptions.to_html_dict(markdown_extension_config=MARKDOWN['extension_configs'])
  PRJCT_VERSION = prjct.__version__
  PRJCT_FOOTER_URL = prjct.__url__
  ```

  Also add prjct to our direct templates list.
PRJCT_ACTIVE_PROJECTS
  A list of *active* projects. Used to sort projects on the main prjct page.
  See the ``PRJCT`` setting.
PRJCT_COMPLETED_PROJECTS
  A list of *active* projects. Used to sort projects on the main prjct page.
  See the ``PRJCT`` setting.
PRJCT_DESC
  A dictionary of descriptions for each project, where the key is the name of
  the project, and will match the *tag* page where the output appears. The
  return value is assumed to be a valid HTML segment. See the ``PRJCT``
  setting.
PRJCT_DONE
  A dictionary of done to-do items for each project, where the key is the name
  of the project, and will match the *tag* page where the output appears. The
  return value is assumed to be a valid HTML segment. See the ``PRJCT``
  setting.
PRJCT_FOOTER_URL = 'https://github.com/MinchinWeb/prjct'
  *prjct* URL used for link displayed in footer. See the ``PRJCT`` setting.
PRJCT_SOMEDAY_PROJECTS
  A list of *active* projects. Used to sort projects on the main prjct page.
  See the ``PRJCT`` setting.
PRJCT_TODO
  A dictionary of open to-do items for each project, where the key is the name
  of the project, and will match the *tag* page where the output appears. The
  return value is assumed to be a valid HTML segment. See the ``PRJCT``
  setting.
PRJCT_VERSION = ''
  *prjct* version displayed in footer. See the ``PRJCT`` setting.
PYGMENTS_STYLE = 'native'
  This setting is currently ignored, and my preferred Pygments style is
  included directly into the Seafoam CSS.
RECENT_POST_COUNT = 5
  Number of recent posts to display on the sidebar. See the
  ``DISPLAY_RECENT_POSTS_ON_SIDEBAR`` setting.
RELATED_POSTS_TEXT = 'Related Posts:'
  Header for related posts listing. Requires that the
  `Related Posts Plugin <https://github.com/getpelican/pelican-plugins/tree/master/related_posts>`_
  be active.
SITELOGO
  Link to the site logo (displayed in the navbar). This is relative to the
  SITEURL.
SITELOGO_SIZE
  The width of the site logo in the navbar. Can be set to any valid CSS value
  (i.e. %, em, px, etc). I have had good luck setting this to ``100%``.
SITENAME
  The name of your site, displayed in the navbar.
SITEURL
  Same as the Pelican setting. Set this to where this Pelican site is actually
  hosted. Also see the ``SITE_ROOT_URL`` setting.
SITE_ROOT_URL = SITEURL
  Use this if you're hosting a subsite of some sort. This is where the links in
  logo in the navbar and the home icon in the breadcrumbs will point to. See
  also the ``MENUITEMS_2_AT`` setting.
SOCIAL
  A list of your social media sites to be listed in the sidebar. Should he a
  list of tuples in the form ('social network name', 'full link to profile').
  The theme will display the logo of the network. See the ``HIDE_SIDEBAR``
  setting.
TAGS_URL
  Same as the Pelican setting.
THEME_STATIC_DIR
  Same as the Pelican setting.
TWITTER_USERNAME
  You can optionally provide a this which will be used to set the Twitter
  username for the site and for the content creator.
TWITTER_WIDGET_ID
  The theme can show your twitter timeline in the sidebar. To enable, provide a
  ``TWITTER_USERNAME`` and a ``TWITTER_WIDGET_ID``.

  To get a ``TWITTER_WIDGET_ID``, go to:
  `https://twitter.com/settings/widgets <https://twitter.com/settings/widgets>`_
  and select *Create new*. You'll find the ``TWITTER_WIDGET_ID`` under the html
  or in the site url:

  https://twitter.com/settings/widgets/TWITTER_WIDGET_ID/edit
TYPOGRIFY
  Whether to activate Typography. Tyopgraphy is a library that automatically
  adds a number of typographical flourishes. The necessary CSS is automatically
  included in the *seafoam* CSS.

  The Typography Python library will needs to be installed, which is
  installable via pip: ``pip install typogrify``

  Note that with Pelican 3.6, activating both the Pelican Comment System and
  Typography at the same time cause issues. This issue was fixed in Pelican
  3.7.
USE_OPEN_GRAPH = True
  In order to make the Facebook "like" button and other social sharing options
  work better, the template contains Open Graph metatags like
  ``<meta property="og:type" content="article"/>``. You can disable them by
  setting this to ``False``.

  See also ``OPEN_GRAPH_FB_APP_ID``, and ``OPEN_GRAPH_FB_APP_ID``
  settings.

It may also be helpful to review the
`settings for Pelican itself <http://docs.getpelican.com/en/3.7.1/settings.html>`_.

On articles, the theme also looks for the ``image`` metadata setting to provide
the "featured image* for the article.


Known Issues
------------

- the ``setup.py`` file for this project does not run on Python 2.7. However,
  wheels of this project are "universal" and so can be generated by Python 3
  and subsequently installed by Python 2.7.
- when installing on versions of Python before 3.4 (when the ``pathlib`` module
  was added to the standard library), `pathlib2
  <https://pypi.python.org/pypi/pathlib2>`_ is an additional dependency. This,
  in turn, depends on `scandir <https://pypi.python.org/pypi/scandir>`_,
  which requires a C compiler to install. If you (like I), don't have a C
  compiler already set up on your Windows machines, you sidestep that issue by
  downloading a pre-build wheel from `Christoph Gohlke
  <http://www.lfd.uci.edu/~gohlke/pythonlibs/#scandir>`_ and installing
  ``scandir`` this way before you try and install ``seafoam``.
- activating both Typogrify and the Pelican Comment System on Pelican 3.6
  causes issues. This issue has been fixed in Pelican 3.7.

Credits
-------

Original theme developed by `Daan Debie <http://dandydev.net/>`_.

The idea that a theme could be installed as a Python package by `Jeff
Forcier <http://bitprophet.org/>`_'s `Alabaster theme
<https://github.com/bitprophet/alabaster>`_ for Sphinx.
