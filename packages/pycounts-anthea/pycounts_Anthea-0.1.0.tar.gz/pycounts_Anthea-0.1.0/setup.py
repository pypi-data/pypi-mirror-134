# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pycounts_anthea']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0']

setup_kwargs = {
    'name': 'pycounts-anthea',
    'version': '0.1.0',
    'description': 'package for DSCI 524',
    'long_description': '# pycounts_Anthea\n\npackage for DSCI 524\n\n## Installation\n\n```bash\n$ pip install pycounts_Anthea\n```\n\n## Usage\n\n`pycounts_Anthea` can be used to count words in a text file and plot results\nas follows:\n\n```python\nfrom pycounts_Anthea.pycounts_Anthea import count_words\nfrom pycounts_Anthea.plotting import plot_words\nimport matplotlib.pyplot as plt\n\nfile_path = "test.txt"  # path to your file\ncounts = count_words(file_path)\nfig = plot_words(counts, n=10)\nplt.show()\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`pycounts_Anthea` was created by anthea. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`pycounts_Anthea` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n\n\n',
    'author': 'anthea',
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
