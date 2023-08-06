# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ackack']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.20.31,<2.0.0',
 'fastapi>=0.71.0,<0.72.0',
 'requests>=2.27.1,<3.0.0',
 'uvicorn>=0.16.0,<0.17.0',
 'weback-unofficial>=0.3.5,<0.4.0']

setup_kwargs = {
    'name': 'ackack',
    'version': '0.1.0',
    'description': '',
    'long_description': '.. figure:: ./docs/ackack.jpg\n   :width: 200px\n\n   (Creative Commons Attribution-Noncommercial-No Derivative Works 3.0 License, Author Wonder Waffle https://www.deviantart.com/wonder-waffle/art/ACK-ACK-Mars-Attacks-359710975 )\n\n\n\n|pypi| |release| |downloads| |python_versions| |pypi_versions| |actions|\n\n.. |pypi| image:: https://img.shields.io/pypi/l/ackack\n.. |release| image:: https://img.shields.io/librariesio/release/pypi/ackack\n.. |downloads| image:: https://img.shields.io/pypi/dm/ackack\n.. |python_versions| image:: https://img.shields.io/pypi/pyversions/ackack\n.. |pypi_versions| image:: https://img.shields.io/pypi/v/ackack\n.. |actions| image:: https://github.com/XayOn/ackack/workflows/CI%20commit/badge.svg\n    :target: https://github.com/XayOn/ackack/actions\n\n\n**Have fun with your vaccuum robot!**\n\nAckAck is a simple control API to manually controll weback vacuum robots.\nPaired with its web interface, and a RTPS (in my case, I\'m using an old yi ants\ncamera with `yi-hack <https://github.com/fritz-smh/yi-hack>`_)\n\nThis way you can remotely-scare your cats! \n\n.. image:: ./docs/screenshot.png\n\n\nKeys\n----\n\nUse your arrow keys to move the robot left, right, go front or turn backwards.\nEnter will start cleaning and backspace will stop.\n\n\nEnvironment variables\n---------------------\n\nYou\'ll need to setup your weback username and password.\nUsually, this will be your phone + the password you use on the control app.\nBesides that, only RTSP_URL is required.\n\n\n===============  =====================================\nKEY               Description\n===============  =====================================\nRTSP_URL         Yi camera\'s RTSP stream URL \nWEBACK_USERNAME  Your weback\'s username (phone number)\nWEBACK_PASSWORD  Your weback\'s password\nBASE_URL         Base URL, for reverse proxies\n===============  =====================================\n\n\nInstallation\n------------\n\nDocker\n++++++\n\nWith docker, just setup the specified env vars and launch the image.\nYou can use the following docker-compose.yml example.\nSetting base_url is useful in reverse proxy scenarios (like traefik).\n\n.. code:: yaml\n\n    version: "3.3"\n    services:\n      ackack:\n        image: XayOn/ackack\n        restart: unless-stopped\n        ports:\n          - 8080:8080\n        environment:\n          RTSP_URL: http://192.168.1...\n          WEBACK_USERNAME: +33-123123123\n          WEBACK_PASSWORD: yourpassword \n          BASE_URL: /ackack\n\n\nManual setup\n++++++++++++\n\nInstall the project, set your environment variables, launch ffmpeg to create a\nm3u8 file in static/playlist.m3u8 from your rtsp.\n\nRequires ffmpeg. Check your distro\'s instructions on how to install ffmpeg\nYou can checkout docker-entrypoint.sh and use its ffmpeg command\n\n.. code:: bash\n\n   pip install ackack\n   WEBACK_USERNAME="+34-XXXX" WEBACK_PASSWORD="XXXX" poetry run uvicorn ackack:app\n\n\nHow does it work?\n-----------------\n\nAckack is simply an API for movement commands on python\'s `weback unofficial\nlibrary <https://github.com/opravdin/weback-unofficial>`_, with an interface in\nplain html + js (with just videojs, minimal), paired with an ffmpeg command\nthat converts the rtsp output of the yi camera to a format playable by your\nbrowser.\n',
    'author': 'David Francos',
    'author_email': 'opensource@davidfrancos.net',
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
