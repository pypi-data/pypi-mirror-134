# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['givenergy_modbus', 'givenergy_modbus.model', 'tests', 'tests.model']

package_data = \
{'': ['*']}

install_requires = \
['click==8.0.1',
 'crccheck>=1.1,<2.0',
 'loguru>=0.5.3,<0.6.0',
 'pydantic>=1.8.2,<2.0.0',
 'pymodbus>=2.5.3,<3.0.0']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'doc': ['mkdocs>=1.1.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.15.2,<0.16.0',
         'mkdocs-autorefs>=0.2.1,<0.3.0'],
 'test': ['black>=21.5b2,<22.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=4.0.0,<5.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'mypy>=0.900,<0.901',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

entry_points = \
{'console_scripts': ['givenergy-modbus = givenergy_modbus.cli:main']}

setup_kwargs = {
    'name': 'givenergy-modbus',
    'version': '0.9.0',
    'description': 'A python library to access GivEnergy inverters via Modbus TCP, with no dependency on the GivEnergy Cloud.',
    'long_description': '# GivEnergy Modbus\n\n[![pypi](https://img.shields.io/pypi/v/givenergy-modbus.svg)](https://pypi.org/project/givenergy-modbus/)\n[![python](https://img.shields.io/pypi/pyversions/givenergy-modbus.svg)](https://pypi.org/project/givenergy-modbus/)\n[![Build Status](https://github.com/dewet22/givenergy-modbus/actions/workflows/dev.yml/badge.svg)](https://github.com/dewet22/givenergy-modbus/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/dewet22/givenergy-modbus/branch/main/graphs/badge.svg)](https://codecov.io/github/dewet22/givenergy-modbus)\n\nA python library to access GivEnergy inverters via Modbus TCP on a local network, with no dependency on the GivEnergy Cloud.\nThis extends [pymodbus](https://pymodbus.readthedocs.io/) by providing a custom framer, decoder and PDUs\nthat are specific to the GivEnergy implementation.\n\n> ⚠️ This project makes no representations as to its completeness or correctness. You use it at your own risk — if your inverter\n> mysteriously explodes because you accidentally set the `BOOMTIME` register, or you consume a MWh of electricity doing SOC calibration,\n> you really are on your own.\n\n* Documentation: <https://dewet22.github.io/givenergy-modbus>\n* GitHub: <https://github.com/dewet22/givenergy-modbus>\n* PyPI: <https://pypi.org/project/givenergy-modbus/>\n* Free software: Apache-2.0\n\n## Features\n\n* Reading all registers and decoding them into their representative datatypes\n* Writing data to individual holding registers that are deemed to be safe\n\n## How to use\n\nUse the provided client to interact with the device over the network:\n\n```python\nfrom datetime import time\nfrom givenergy_modbus.client import GivEnergyClient\nfrom givenergy_modbus.model.inverter import Model\n\nclient = GivEnergyClient(host="192.168.99.99")\nclient.enable_charge_target(80)\n# set a charging slot from 00:30 to 04:30\nclient.set_charge_slot_1((time(hour=0, minute=30), time(hour=4, minute=30)))\n\ninverter = client.update_inverter()\nassert inverter.serial_number == \'SA1234G567\'\nassert inverter.model == Model.Hybrid\nassert inverter.v_pv1 == 1.4000000000000001\nassert inverter.e_generated_day == 8.1\nassert inverter.enable_charge_target\nassert inverter.dict() == {\n    \'active_power_rate\': 100,\n    \'arm_firmware_version\': 449,\n    \'battery_charge_limit\': 50,\n    ...\n}\n\nbattery = client.update_battery(battery_number=0)\n\nassert battery.serial_number == \'BG1234G567\'\nassert battery.v_cell_01 == 3.117\nassert battery.dict() == {\n    \'bms_firmware_version\': 3005,\n    \'design_capacity\': 160.0,\n    ...\n}\n```\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.\n',
    'author': 'Dewet Diener',
    'author_email': 'givenergy-modbus@dewet.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dewet22/givenergy-modbus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
