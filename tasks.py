
from pathlib import Path

from invoke import run, task
# also requires `lessc` to be installed and available from the commandline

# TODO: provide for alternative shell on something other than Windows
INVOKE_SHELL = 'C:\Windows\system32\cmd.EXE'

p = Path(__file__).parent  # directory holding this file

@task
def build(ctx):
    p2 = p / 'minchin' / 'pelican' / 'themes' / 'minchindotca'
    source = p2 / 'static' / 'less' / 'bootstrap.minchindotca.less'
    dest = p2 / 'static' / 'css' / 'bootstrap.minchindotca.min.css'
    run('lessc {} > {}'.format(source, dest), shell=INVOKE_SHELL)
    # TODO -- minimize css!

@task
def test(ctx):
    p3 = p / 'test' / 'pelicanconf.py'
    run('pelican -s {}'.format(p3), shell=INVOKE_SHELL)

@task
def serve_test(ctx, port='8000'):
    # call using:
    # invoke serve_test --port 8001

    p4 = p / 'test' / 'output'
    run('cd {} && start python -m http.server {}'.format(p4, port), shell=INVOKE_SHELL)
