# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['slotscheck']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<9']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1,<5']}

entry_points = \
{'console_scripts': ['slotscheck = slotscheck.cli:root']}

setup_kwargs = {
    'name': 'slotscheck',
    'version': '0.4.0',
    'description': 'Check the usage of __slots__.',
    'long_description': '🎰 Slotscheck\n=============\n\n.. image:: https://img.shields.io/pypi/v/slotscheck.svg?color=blue\n   :target: https://pypi.python.org/pypi/slotscheck\n\n.. image:: https://img.shields.io/pypi/l/slotscheck.svg\n   :target: https://pypi.python.org/pypi/slotscheck\n\n.. image:: https://img.shields.io/pypi/pyversions/slotscheck.svg\n   :target: https://pypi.python.org/pypi/slotscheck\n\n.. image:: https://img.shields.io/readthedocs/slotscheck.svg\n   :target: http://slotscheck.readthedocs.io/\n\n.. image:: https://github.com/ariebovenberg/slotscheck/actions/workflows/build.yml/badge.svg\n   :target: https://github.com/ariebovenberg/slotscheck/actions/workflows/build.yml\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n\nAdding ``__slots__`` to a class in Python is a great way to reduce memory usage.\nBut to work properly, all base classes need to implement it.\nIt turns out it\'s easy to forget one class in complex inheritance trees.\nWhat\'s worse: there is nothing warning you that you messed up.\n\n✨ *Until now!* ✨\n\nSee my `blog post <https://dev.arie.bovenberg.net/blog/finding-broken-slots-in-popular-python-libraries/>`_\nfor the longer story behind ``slotscheck``.\n\nQuickstart\n----------\n\nUsage is quick from the command line:\n\n.. code-block:: bash\n\n   slotscheck [MODULE]\n\n\nFor example:\n\n.. code-block:: bash\n\n   $ slotscheck pandas\n   ERROR: \'pandas.core.internals.array_manager:BaseArrayManager\' has slots but inherits from non-slot class.\n   ERROR: \'pandas.core.internals.array_manager:SingleArrayManager\' defines overlapping slots.\n   ERROR: \'pandas.core.internals.array_manager:SingleArrayManager\' has slots but inherits from non-slot class.\n   ERROR: \'pandas.core.internals.blocks:Block\' has slots but inherits from non-slot class.\n   ERROR: \'pandas.core.internals.blocks:CategoricalBlock\' has slots but inherits from non-slot class.\n   ERROR: \'pandas.core.internals.blocks:DatetimeLikeBlock\' has slots but inherits from non-slot class.\n   ERROR: \'pandas.core.internals.blocks:NumericBlock\' has slots but inherits from non-slot class.\n   ERROR: \'pandas.core.internals.blocks:ObjectBlock\' has slots but inherits from non-slot class.\n   ERROR: \'pandas.core.internals.managers:BaseBlockManager\' has slots but inherits from non-slot class.\n   ERROR: \'pandas.core.internals.managers:SingleBlockManager\' has slots but inherits from non-slot class.\n   Oh no, found some problems!\n\nNow get to fixing --\nand add ``slotscheck`` to your CI pipeline to prevent mistakes from creeping in again!\n\nUse the ``--help`` option to find out more.\n\n\nCould this be a flake8 plugin?\n------------------------------\n\nMaybe. But it\'d be a lot of work.\n\nThe problem is that flake8 plugins need to work without running the code.\nMany libraries use conditional imports, star imports, re-exports,\nand define slots with decorators or metaclasses.\nThis all but requires running the code to determine the class tree and slots.\n\nThere\'s `an issue <https://github.com/ariebovenberg/slotscheck/issues/6>`_\nto track any progress on the matter.\n\nNotes\n-----\n\n- ``slotscheck`` will try to import all submodules of the given package.\n  If there are scripts without ``if __name__ == "__main__":`` blocks,\n  they may be executed.\n- Even in the case that slots are not inherited properly,\n  there may still be an advantage to using them\n  (i.e. attribute access speed and *some* memory savings).\n  However, I\'ve found in most cases this is unintentional.\n- Limited to the CPython implementation for now.\n- Non pure-Python classes are currently assumed to have slots.\n  This is not necessarily the case, but it is nontrivial to determine.\n\nInstallation\n------------\n\nIt\'s available on PyPI.\n\n.. code-block:: bash\n\n  pip install slotscheck\n',
    'author': 'Arie Bovenberg',
    'author_email': 'a.c.bovenberg@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ariebovenberg/slotscheck',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.0,<4',
}


setup(**setup_kwargs)
