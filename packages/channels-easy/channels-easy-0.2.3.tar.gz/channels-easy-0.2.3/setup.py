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
    'version': '0.2.3',
    'description': 'A thin wrapper around channels consumer to make things EASY',
    'long_description': '[![codecov](https://codecov.io/gh/namantam1/channels-easy/branch/main/graph/badge.svg?token=QGazPv0Bcj)](https://codecov.io/gh/namantam1/channels-easy)\n[![Release](https://github.com/namantam1/channels-easy/actions/workflows/release.yaml/badge.svg)](https://github.com/namantam1/channels-easy/actions/workflows/release.yaml)\n[![Test](https://github.com/namantam1/channels-easy/actions/workflows/python-package.yml/badge.svg)](https://github.com/namantam1/channels-easy/actions/workflows/python-package.yml)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n# Channels Easy <!-- omit in toc -->\nA thin wrapper around channel consumers to make things **EASY**\n\n***Note***: This library currently support only text data which is JSON serializable.\n\n**What problem does this library solve?**\nThis library simplifies two tasks for now\n1. Parse incoming text data as JSON and vice versa.\n2. Generate event on the basis of type passed from client side.\n\n**Table of Contents**\n- [Installation](#installation)\n- [Example](#example)\n- [API Usage](#api-usage)\n- [Contribute](#contribute)\n\n## Installation\n\nTo get the latest stable release from PyPi\n\n```bash\npip install channels-easy\n```\nTo get the latest commit from GitHub\n\n```bash\npip install -e git+git://github.com/namantam1/channels-easy.git#egg=channels-easy\n```\n\nAs `channels-easy` is a thin wrapper around `channels` so channels must be in your `INSTALLED_APPS` in `settings.py`.\n\n```bash\nINSTALLED_APPS = (\n    ...,\n    \'channels\',\n)\n```\n\n## Example\n\nAll the naming convention used to implement this library is inspired from [socket.io](https://socket.io/) to make server implementation simple.\n\nGet full example project [here](./example).\n\n**Server side**\n```python\n# consumers.py\nfrom channels_easy.generic import AsyncWebsocketConsumer\n\n\nclass NewConsumer(AsyncWebsocketConsumer):\n    async def connect(self):\n        # join room on connect\n        await self.join("room1")\n        await self.accept()\n\n    async def disconnect(self, close_code):\n        # Leave room on disconnect\n        await self.leave("room1")\n\n    async def on_message(self, data):\n        print("message from client", data)\n        # output:\n        # message from client {\'text\': \'hello\'}\n\n        await self.emit("message", "room1", {"message": "hello from server"})\n\n```\n\n**Client side**\n\n```javascript\n// client.js\nconst socket = new WebSocket("ws://localhost:8000/ws/test/");\n\nsocket.onmessage = function ({ data }) {\n    const parsed_data = JSON.parse(data);\n    console.log(parsed_data);\n    // output:\n    // {\n    //     data: {message: \'hello from server\'}\n    //     type: "message"\n    // }\n};\n\nsocket.onopen = () => {\n    console.log("websocket connected...");\n\n    // send message from client after connected\n    // send with type `message` to receive from subscribed\n    // `on_message` event on server side\n    socket.send(\n        JSON.stringify({\n            type: "message",\n            data: {\n                text: "hello",\n            },\n        })\n    );\n};\n\n```\n\n## API Usage\n\n**Subscribing to events**\nWe can simply subscribe to a message type as\n\n```python\ndef on_<type>(self, data):\n    ...\n    pass\n```\n\nso if client send data as\n```json\n{\n    "type": "message",\n    "data": "Hello!"\n}\n```\nWe can subscribe to message event as\n\n```python\ndef on_message(self, data):\n    ...\n    pass\n```\n\n**Emitting Message**\n\nWe can emit message to client using same schema that we used above\n\n```python\ndef on_message(self, data):\n    ...\n    # some code here\n    ...\n\n    self.emit(\n        "message",          # type\n        ["room1"],          # room list or string\n        {"text": "hello"}   # message dict | str | int | list\n    )\n```\n\nCheck all APIs [here](https://namantam1.github.io/channels-easy/apis/).\n\n## Contribute\n\nIf you want to contribute to this project, please perform the following steps\n\n```bash\n# Fork this repository\n# Clone your fork\npoetry install\n\ngit checkout -b feature_branch master\n# Implement your feature and tests\ngit add . && git commit\ngit push -u origin feature_branch\n# Send us a pull request for your feature branch\n```\n\nIn order to run the tests, simply execute `poetry run pytest`. This will run test created inside\n`test` directory.\n',
    'author': 'Naman Tamrakar',
    'author_email': 'namantam1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://namantam1.github.io/channels-easy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
