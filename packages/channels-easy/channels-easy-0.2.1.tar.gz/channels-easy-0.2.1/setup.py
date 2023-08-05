# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['channels_easy']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.0', 'channels>=3.0']

setup_kwargs = {
    'name': 'channels-easy',
    'version': '0.2.1',
    'description': 'A thin wrapper around channels consumer to make things EASY',
    'long_description': 'channels-easy\n============\n\nA thin wrapper around channel consumers to make things **EASY**.\n\nInstallation\n------------\n\nTo get the latest stable release from PyPi\n\n```bash\npip install channels-easy\n```\nTo get the latest commit from GitHub\n\n```bash\npip install -e git+git://github.com/namantam1/channels-easy.git#egg=channels-easy\n```\n<!-- TODO: Describe further installation steps (edit / remove the examples below): -->\n\nAs `channels-easy` is a thin wrapper around `channels` so channels must be in your `INSTALLED_APPS` in `settings.py`.\n\n```bash\nINSTALLED_APPS = (\n    ...,\n    \'channels\',\n)\n```\n\nUsage\n-----\n\nAll the naming convention used to implement this library is inspired from [socket.io](https://socket.io/) to make server implementation simple.\n\n```python\n# consumers.py\nfrom channels_easy.generic import AsyncWebsocketConsumer\n\n\nclass NewConsumer(AsyncWebsocketConsumer):\n    async def connect(self):\n        # join room on connect\n        await self.join("room1")\n        await self.accept()\n\n    async def disconnect(self, close_code):\n        # Leave room on disconnect\n        await self.leave("room1")\n\n    async def on_message(self, data):\n        print("message from client", data)\n        await self.emit("message", "room1", {"message": "hello from server"})\n\n```\n\nContribute\n----------\n\nIf you want to contribute to this project, please perform the following steps\n\n````bash\n# Fork this repository\n# Clone your fork\npoetry install\n\ngit checkout -b feature_branch master\n# Implement your feature and tests\ngit add . && git commit\ngit push -u origin feature_branch\n# Send us a pull request for your feature branch\n````\n<!-- In order to run the tests, simply execute ``tox``. This will install two new\nenvironments (for Django 1.8 and Django 1.9) and run the tests against both\nenvironments. -->\n',
    'author': 'Naman Tamrakar',
    'author_email': 'namantam1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/namantam1/channels-easy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
