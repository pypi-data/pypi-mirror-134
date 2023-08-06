# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pycounts_gf']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0']

setup_kwargs = {
    'name': 'pycounts-gf',
    'version': '1.0',
    'description': 'Count the number of occurrences of a word in a text file',
    'long_description': '# pycounts_gf\n\nCalculate word counts in a text file!\n\n## Installation\n\n```bash\n$ pip install pycounts_gf\n```\n\n## Usage\n\n`pycounts_gf` can be used to count words in a text file and plot results\nas follows:\n\n```python\nfrom pycounts_gf.pycounts_gf import count_words\nfrom pycounts_gf.plotting import plot_words\nimport matplotlib.pyplot as plt\n\nfile_path = "test.txt"  # path to your file\ncounts = count_words(file_path)\nfig = plot_words(counts, n=10)\nplt.show()\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. \nPlease note that this project is released with a Code of Conduct. \nBy contributing to this project, you agree to abide by its terms.\n\n## License\n\n`pycounts_gf` was created by Gabe Fairbrother. It is licensed under the terms\nof the MIT license.\n\n## Credits\n\n`pycounts_gf` was created with \n[`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and \nthe `py-pkgs-cookiecutter` \n[template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\npackage originally based on this [tutorial](https://py-pkgs.org/03-how-to-package-a-python)',
    'author': 'Gabriel Fairbrother',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
