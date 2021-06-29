from pathlib import Path

from invoke import run, task
try:
    from minchin.releaser import make_release
except ImportError:
    print("[WARN] minchin.releaser not installed")

# also requires `lessc` to be installed and available from the commandline

# TODO: provide for alternative shell on something other than Windows

p = Path(__file__).parent  # directory holding this file


@task
def build(ctx):
    """Compile the theme LESS files to CSS."""
    p2 = p / 'pelican' / 'plugins' / 'seafoam'
    source = p2 / 'static' / 'less' / 'bootstrap.seafoam.less'
    dest = p2 / 'static' / 'css' / 'bootstrap.seafoam.min.css'
    run('lessc {} > {}'.format(source, dest))
    print("Seafoam LESS compiled to CSS!")
    # TODO -- minimize css!
    #   consider css-html-js-minify


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
    print(p4)
    run('cd {} && start python -m http.server {}'.format(p4, port))
