import pytest

from .path import Path


def test_subpaths():
    path = Path('a.b.c.d')
    assert list(path.subpaths()) == [
        Path('c.d'),
        Path('b.c.d'),
        Path('a.b.c.d')
    ]


def test_add():
    assert Path('a') + Path('b') == Path('a.b')


def test_lt():
    assert Path('a') < 'b'


def test_repr():
    assert repr(Path('a')) == '<Path a>'


def test_init_error():
    with pytest.raises(TypeError):
        Path(1)
