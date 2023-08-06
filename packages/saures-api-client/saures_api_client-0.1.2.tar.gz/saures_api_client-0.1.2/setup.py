# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['saures_api_client']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0']

setup_kwargs = {
    'name': 'saures-api-client',
    'version': '0.1.2',
    'description': 'SAURES API client',
    'long_description': 'SAURES API Client\n=================\n\n[SAURES](https://saures.ru) API client\n\nStage: Alpha\n\nInstallation\n------------\n\n1. From this repository (`poetry` required)\n* `git clone https://github.com/Yurzs/saures_api_client.git`\n* `cd saures_api_client`\n* `poetry install --no-dev`\n\n2. From PyPi\n* `pip install saures_api_client`\n\nUsage\n-----\n\n1. You can use all the api methods like they are named in [SAURES API docs](https://api.saures.ru/doc/):\n```python\nfrom saures_api_client import SauresAPIClient\n\nasync def main():\n    client = SauresAPIClient("your email", "your password")\n\n    objects = await client.user_objects()\n\n...\n```\n\n2. Or you can use more user-friendly wrapper around the client:\n```python\nfrom saures_api_client import SauresAPIClient\nfrom saures_api_client import types\n\nasync def main():\n    user = SauresAPIClient.get_user("your email", "your password")\n    \n    locations = await user.get_locations()\n    # returns typing.List[types.Location]\n    \n    location = locations[0]\n    location_controllers = await location.get_controllers()\n    # returns typing.List[types.Controller]\n    # so you can easily propagate deeper in entities without\n    # specifically providing their IDs to the client.\n\n```\n',
    'author': 'Yury Sokov',
    'author_email': 'yury@yurzs.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Yurzs/saures_api_client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4',
}


setup(**setup_kwargs)
