import pathlib

import pytest
from click.testing import CliRunner

from linesieve import cli
from linesieve import paths_to_modules
from linesieve import shorten_paths


ROOT = pathlib.Path(__file__).parent


DATA_PATHS = sorted(ROOT.glob('data/*.in'))


@pytest.fixture(params=DATA_PATHS, ids=lambda p: p.name)
def data(request):
    inp = request.param
    outp = inp.with_suffix('.out')
    with inp.open() as inf, outp.open() as outf:
        return next(inf).rstrip(), inf.read(), outf.read()


def test_data(data):
    args, input, output = data
    runner = CliRunner()
    result = runner.invoke(cli, args, input, catch_exceptions=False)
    assert result.output == output


SHORTEN_DATA = [
    {
        'm1': 'm1',
        'src/p1/m1.py': 'src/p1/m1.py',
        'src/p1/p2/m1.py': 'src/.../p2/m1.py',
        'src/p1/p2/m2.py': 'src/.../p2/m2.py',
        'src/p1/p3/m2.py': 'src/.../p3/m2.py',
        'tst/m1.py': 'tst/m1.py',
        'tst/m2.py': 'tst/m2.py',
        'tst/mt.py': '.../mt.py',
    },
    {
        'double.py': 'double.py',
        'src/one/mod.py': 'src/one/mod.py',
        'src/one/two/mod.py': 'src/.../two/mod.py',
        'tst/one/mod.py': 'tst/.../mod.py',
        'tst/single.py': '.../single.py',
    },
    {
        'a/x': 'a/x',
        'a/b/x': '.../b/x',
    },
    {
        'a/d/b/x': '.../b/x',
        'a/d/c/x': '.../c/x',
    },
]


@pytest.mark.parametrize('output', SHORTEN_DATA)
def test_shorten_paths(output):
    assert shorten_paths(output, '/', '...') == output


MODULE_PATHS = """
src/one/mod.py
src/one/two/mod.py
tst/mod.py
root.py
""".split()


@pytest.mark.parametrize(
    'skip, recursive, output',
    [
        (0, False, "src.one.mod src.one.two.mod tst.mod"),
        (1, False, "one.mod one.two.mod"),
        (0, True, "src.one.mod src.one src.one.two.mod src.one.two tst.mod"),
        (1, True, "one.mod one.two.mod one.two"),
    ],
)
def test_paths_to_modules(skip, recursive, output):
    assert paths_to_modules(MODULE_PATHS, skip=skip, recursive=recursive) == set(
        output.split()
    )
