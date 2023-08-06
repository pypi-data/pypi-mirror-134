# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['opensecrets_senators_industries']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'lxml>=4.7.1,<5.0.0',
 'pandas>=1.3.5,<2.0.0',
 'python-dotenv>=0.19.2,<0.20.0',
 'requests>=2.26.0,<3.0.0',
 'unittest>=0.0,<0.1']

setup_kwargs = {
    'name': 'opensecrets-senators-industries',
    'version': '0.1.0',
    'description': 'Python package using the OpenSecrets and ProPublica APIs to allow users to view information about their senators and the industries that fund them',
    'long_description': "# OpenSecrets_Senators_Industries\n\nPython package that allows users to view information about their senators and the industries that fund them.\n\n## Installation\n\n```bash\n$ pip install OpenSecrets_Senators_Industries\n```\n\n## Usage\n\n```\nfrom OpenSecrets_Senators_Industries import OpenSecrets_Senators_Industries\n\nProPublica = ProPublicaAPIKey('insert ProPublica API Key here')\nOpenSecrets = OpenSecretsAPIKey('insert OpenSecrets API Key here')\n\ntop_20_industries_ids(year)\nProPublica.senate_members(congress_sitting)\nOpenSecrets.top_senators_each_industry(propublica_api_key, industry_id, congress_sitting)\n\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`OpenSecrets_Senators_Industries` was created by Jade Qiu. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`OpenSecrets_Senators_Industries` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n",
    'author': 'Jade Qiu',
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
