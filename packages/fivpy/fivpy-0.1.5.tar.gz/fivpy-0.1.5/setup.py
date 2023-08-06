# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fivpy', 'fivpy.data']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3.5,<2.0.0', 'scipy>=1.7.3,<2.0.0']

setup_kwargs = {
    'name': 'fivpy',
    'version': '0.1.5',
    'description': 'A package for calculating forest inventories in python.',
    'long_description': "# fivpy\n\nA python package to calculate forest inventories.\n\n## Installation\n\n```bash\n$ pip install fivpy\n```\n  \n## Usage\n\n- 'fivpy' can be used to perform forest inventories for a dataset containing the columns units (with the sampled units), dbh or cbh (with the diameter or circunference of   the sampled tress) and height (with the height of the sampled trees).\n\n## Examples\n``` python\nimport pandas as pd\nfrom fivpy import RandomSample\n\n# Loading the data\ndata = pd.read_csv('../src/fivpy/data/data_2.csv', sep=';', decimal=',')\n\n# Creating a inventory instance\ninventory_1 = RandomSample(data,\n                            unit_area=0.02,\n                            sampling_area=11,\n                            significance=90,\n                            sampling_error=10)\n\n# Calculating inventory atributes\ninventory_1.srs_inventory()\n```\nFor more infos and examples of usage please visit **https://fivpy.readthedocs.io/**\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`fivpy` was created by Theilon Macedo. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`fivpy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).  \n\nThe metodology used here is based on the book 'Dendrometria e Inventário Florestal'. **SOARES, C.P.B.; PAULA NETO. F.; SOUZA, A.L. Dendrometria e inventário florestal. 2. Ed. Viçosa: Editora UFV. 2011. 272 p.**",
    'author': 'Theilon Macedo',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
