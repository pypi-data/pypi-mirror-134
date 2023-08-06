# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wordcounts']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0']

setup_kwargs = {
    'name': 'wordcounts',
    'version': '0.1.0',
    'description': 'This package helps count the number of words in a given text',
    'long_description': '# wordcounts\n\nThis package helps count the number of words in a given text\n\n## Installation\n\n```bash\n$ pip install wordcounts\n```\n\n## Usage\n\n`wordcounts` can be used to count words in a text file and plot results\nas follows:\n\n```python\nfrom wordcounts.wordcounts import count_words\nfrom wordcounts.plotting import plot_words\nimport matplotlib.pyplot as plt\n\nfile_path = "test.txt"  # path to your file\ncounts = count_words(file_path)\nfig = plot_words(counts, n=10)\nplt.show()\n```\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`wordcounts` was created by valli akella. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`wordcounts` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'valli akella',
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
