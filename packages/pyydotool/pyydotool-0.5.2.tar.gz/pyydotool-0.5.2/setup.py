# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ydotool']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyydotool',
    'version': '0.5.2',
    'description': 'Python bindings to ydotool',
    'long_description': '# PyYdotool\n\nPython bindings for [`ydotool`](https://github.com/ReimuNotMoe/ydotool)\n\nThis project was inspired by [pyxdotool](https://github.com/cphyc/pyxdotool)\n\nAll `ydotool` commands are chainable.\n\n# Example\n```python\nfrom ydotool import YdoTool\nydo = YdoTool().key("ctrl+alt+f1")\nydo.sleep(2000).type("echo \'foo bar\'")\n# execution is done here\nydo.exec()\n```\n\n# Requirements\nAccess to `/dev/uinput` device is required. It can be set by adding `udev` rules.<br>\nExample tested on Fedora:\n#### **`/etc/udev/rules.d/60-uinput.rules`**\n```shell\nKERNEL=="uinput", SUBSYSTEM=="misc", TAG+="uaccess", OPTIONS+="static_node=uinput"\n```\n\nThis rules will allow regular user logged in to the machine to access `uinput` device. ',
    'author': 'Jerzy Drozdz',
    'author_email': 'jerzy.drozdz@jdsieci.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/jdsieci/pyydotool',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
