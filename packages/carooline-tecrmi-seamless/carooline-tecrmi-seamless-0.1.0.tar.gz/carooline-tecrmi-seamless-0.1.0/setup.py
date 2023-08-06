# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['carooline_tecrmi_seamless']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.19.2,<0.20.0', 'typer>=0.4.0,<0.5.0', 'zeep>=4.1.0,<5.0.0']

entry_points = \
{'console_scripts': ['carooline-tecrmi-seamless = '
                     'carooline_tecrmi_seamless.main:app']}

setup_kwargs = {
    'name': 'carooline-tecrmi-seamless',
    'version': '0.1.0',
    'description': '',
    'long_description': '# TecRMI Seamless login APP\n\nTecRMI Seamless catalog login URL generation\n\n## Installation\n\n```\npip install carooline-tecrmi-seamless\n```\n\n## Configuration\n\nCreate a `.env` file for the TecRMI credentials:\n\n```\nTECRMI_WEBCAT_URL = "https://web.tecalliance.net"\nTECRMI_WEBCAT_WSDL = \'https://webservice.tecalliance.services/webcat30/v1/services/WebCat30WS.soapEndpoint?wsdl\'\nTECRMI_CATALOG = "rmi-iazduih-2"\nTECRMI_USERNAME = "username"\nTECRMI_PASSWORD = "password"\nTECRMI_DEFAULT_TTL = 31536000\nTECRMI_LANG = "fr"\n```\n\n## Usage\n\nCommand should be installed \n\n```\nwich carooline-tecrmi-seamless\n````\n\n### Help\n\n```\ncarooline-tecrmi-seamless\n```\n\n### Generate API Key\n```\ncarooline-tecrmi-seamless get-api-key \n```\n\n### Get Seamless link\n```\ncarooline-tecrmi-seamless get-api-key \n```',
    'author': "Philippe L'ATTENTION",
    'author_email': 'philippe.lattention@hotmail.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
