from fanstatic.config import convert_config
from fanstatic import make_injector


def test_convert_config():
    d = {
        'versioning': 't',
        'recompute_hashes': 'false',
        'bottom': 'True',
        'force_bottom': 'False',
        'rollup': 0,
        'somethingelse': 'True',
        }
    assert convert_config(d) == {
        'versioning': True,
        'recompute_hashes': False,
        'bottom': True,
        'force_bottom': False,
        'rollup': False,
        'somethingelse': 'True',
        }


def test_injector_config():
    d = {
        'versioning': 't',
        'recompute_hashes': 'false',
        'bottom': 'True',
        'force_bottom': 'False',
        'rollup': 0,
        }
    injector = make_injector(None, {}, **d)
    assert injector.app is None
    assert injector.config == {
        'versioning': True,
        'recompute_hashes': False,
        'bottom': True,
        'force_bottom': False,
        'rollup': False,
        }
