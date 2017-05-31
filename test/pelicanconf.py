import seafoam

THEME = seafoam.get_path()
BOOTSTRAP_THEME = 'seafoam'
PATH = 'content'


PLUGINS = [
        'minchin.pelican.jinja_filters',
        'minchin.pelican.plugins.image_process',
        ]

CACHE_CONTENT = False
LOAD_CACHE_CONTENT = False
