from pelican.plugins import seafoam

# THEME = seafoam.get_path()
# BOOTSTRAP_THEME = "seafoam"
PATH = "content"
STATIC_PATHS = [
    "images",
]
TIMEZONE = "America/Edmonton"
OUTPUT_PATH = "output"

PLUGINS = [
    "pelican.plugins.seafoam",
    # "pelican.plugins.jinja_filters",
    # "pelican.plugins.image_process",
]

CACHE_CONTENT = False
LOAD_CACHE_CONTENT = False

# TEMPLATE_PAGES = {
#     "404.html": "404.html",
# }

# Set URL's
TAG_URL = "tags/{slug}/"
TAG_SAVE_AS = "tags/{slug}/index.html"
TAGS_URL = "tags/"
TAGS_SAVE_AS = "tags/index.html"
CATEGORY_URL = "categories/{slug}/"
CATEGORY_SAVE_AS = "categories/{slug}/index.html"
CATEGORIES_URL = "categories/"
CATEGORIES_SAVE_AS = "categories/index.html"
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = ARTICLE_URL
AUTHORS_URL = "authors/"
AUTHORS_SAVE_AS = "authors/index.html"
ARCHIVES_URL = "posts/"
ARCHIVES_SAVE_AS = "posts/index.html"
YEAR_ARCHIVE_URL = "posts/{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = "posts/{date:%Y}/index.html"
MONTH_ARCHIVE_URL = "posts/{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = "posts/{date:%Y}/{date:%m}/index.html"
DAY_ARCHIVE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/"
DAY_ARCHIVE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/index.html"
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = PAGE_URL


MENUITEMS = (
    ("Dev Blog", "https://blog.minchin.ca/label/seafoam/", "fa fa-fw fa-pencil"),
)

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
