from pathlib import Path
import shutil

from invoke import run, task
from minchin.releaser import make_release

# also requires `lessc` to be installed and available from the commandline

# TODO: provide for alternative shell on something other than Windows

p = Path(__file__).parent  # directory holding this file


@task
def build(ctx, mimify=True, watch=False, update=False):
    """Compile the theme SASS files to CSS."""
    # install "sass" via Chocolately
    # install postcss, autoprefixer via npm

    p2 = p / 'seafoam'
    source_folder = p2 / 'src'
    dest_folder = p2 / 'static' / 'css'
    postcss_config = source_folder / "bootstrap" / "postcss.config.js"
    font_dest_folder = p2 / 'static' / 'fonts'

    for style in ["base",
                #   "seafoam",
                  ]:
        if style:
            source = source_folder / "{}.scss".format(style)
            dest = dest_folder / "seafoam.{}.css".format(style)
        else:
            source = source_folder / "base.scss"
            dest = dest_folder / "seafoam.css"

        opts = ""
        if mimify:
            opts += " --style=compressed"
            dest = dest.with_suffix(".min.css")
        else:
            opts += " --style=expanded"

        if watch:
            opts += " --watch"

        if update:
            opts += " --update"

        # compile SASS
        run('sass {} {}{}'.format(source, dest, opts))
        # add vender prefixes
        run('postcss --config {} --replace {}'.format(postcss_config, dest))

        """
        optimize further

        cleancss --level 1 --source-map --source-map-inline-sources
        --output dist/css/bootstrap.min.css dist/css/bootstrap.css &&

        cleancss --level 1 --source-map --source-map-inline-sources --output
        dist/css/bootstrap-grid.min.css dist/css/bootstrap-grid.css &&

        cleancss --level 1 --source-map --source-map-inline-sources --output
        dist/css/bootstrap-reboot.min.css dist/css/bootstrap-reboot.css
        """
    print("Seafoam SASS compiled to CSS!")

    for fn in (p2 / 'src' / 'fontawesome' / 'webfonts').iterdir():
        if fn.is_file():
            shutil.copy(fn, font_dest_folder)
    print("FontAwesome font files copied!")

    for fn in (p2 / 'src' / 'glyphicons' / 'webfonts').iterdir():
        if fn.is_file():
            shutil.copy(fn, font_dest_folder)
    print("Glyphicons font files copied!")


@task
def test(ctx):
    """Generate the test Pelican site."""
    p3 = p / 'test' / 'pelicanconf.py'
    run('pelican -s {}'.format(p3))


@task
def serve_test(ctx, port='8000'):
    """Serve the generated test site."""
    # call using:
    # invoke serve_test --port 8001

    p4 = p / 'test' / 'output'
    run('cd {} && start python -m http.server {}'.format(p4, port))
