# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pycounts_jacqann', 'pycounts_jacqann..ipynb_checkpoints']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0']

setup_kwargs = {
    'name': 'pycounts-jacqann',
    'version': '0.2.0',
    'description': 'Calculate word counts in a text file!',
    'long_description': '# pycounts_jacqann\n\nCalculate word counts in a text file!\n\n## Installation\n\n```bash\n$ pip install pycounts_jacqann\n```\n\n## Usage\n\n`pycounts_jacqann` can be used to count words in a text file and plot the results as follows:\n\n```bash\nfrom pycounts_jacqann.pycounts import count_words\nfrom pycounts_jacqann.plotting import plot_words\nimport mathplotlib.pyplot as plt\n\nfile_path = "test.txt"\ncounts = count_words(file_path)\nfig = plot_words(counts, n=10_\nplt.show()\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`pycounts_jacqann` was created by Jacqueline Chong. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`pycounts_jacqann` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Jacqueline Chong',
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
