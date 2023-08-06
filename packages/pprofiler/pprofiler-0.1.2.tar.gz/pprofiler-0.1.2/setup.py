# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['pprofiler']
setup_kwargs = {
    'name': 'pprofiler',
    'version': '0.1.2',
    'description': 'Python Decorator for Profiling Function or Method',
    'long_description': '# pprofiler\n\nSimple Python Decorator to Profiling Function or Method\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install pprofiler.\n\n```bash\npip install pprofiler\n```\n\n## Usage\n\n\n```\nPython 3.8.10 (default, Jun 23 2021, 11:56:21)\nType \'copyright\', \'credits\' or \'license\' for more information\nIPython 7.24.1 -- An enhanced Interactive Python. Type \'?\' for help.\n\nIn [1]: from pprofiler import pprof\n\nIn [2]: @pprof(sort_by=["cumulative", "ncalls"])\n   ...: def test():\n   ...:     arr = []\n   ...:     for i in range(0, 100_000):\n   ...:         arr.append(i)\n   ...:\n\nIn [3]: test()\n         100002 function calls in 0.018 seconds\n\n   Ordered by: cumulative time, call count\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.012    0.012    0.018    0.018 <ipython-input-4-87325251511f>:1(test)\n   100000    0.005    0.000    0.005    0.000 {method \'append\' of \'list\' objects}\n        1    0.000    0.000    0.000    0.000 {method \'disable\' of \'_lsprof.Profiler\' objects}\n```\n\n\n# pprofiler 0.1.2 Release Notes\n## January 12, 2022\n\n## Changelog\n\n* Add `line_to_print` parameter - to reduce output for large profiler output\n* Add `strip_dirs` parameter - to reduce output for large profiler output\n* `sort_by` parameter now accept `tuple` or `list`\n\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Ngalim Siregar',
    'author_email': 'ngalim.siregar@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nsiregar/pprof',
    'package_dir': package_dir,
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
