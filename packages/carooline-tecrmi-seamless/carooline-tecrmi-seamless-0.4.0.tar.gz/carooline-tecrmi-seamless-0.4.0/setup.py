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
    'version': '0.4.0',
    'description': '',
    'long_description': '# TecRMI Seamless login APP\n\nTecRMI Seamless catalog login URL generation\n\n## Installation\n\n```\npip install carooline-tecrmi-seamless\n```\n\n## Configuration\n\nCreate a `.tecrmi.env` file in your `~/` or Home folder with global TecRMI credentials:\n\n```\nTECRMI_WEBCAT_URL = "https://web.tecalliance.net"\nTECRMI_WEBCAT_WSDL = \'https://webservice.tecalliance.services/webcat30/v1/services/WebCat30WS.soapEndpoint?wsdl\'\nTECRMI_CATALOG = "rmi-iazduih-2"\nTECRMI_USERNAME = "username"\nTECRMI_PASSWORD = "password"\nTECRMI_DEFAULT_TTL = 31536000\nTECRMI_LANG = "fr"\n```\n\nThis is not mandatory, you can also pass each arguments directly to the command line.\n\n## Usage\n\nCommand should be installed \n\n```\nwich carooline-tecrmi-seamless\n````\n\nShow version:\n```\ncarooline-tecrmi-seamless --version\n```\n\n### Help\n\nTo see the different options and commands available:\n\n```\ncarooline-tecrmi-seamless --help\n```\n\nShould output \n```shell\nUsage: carooline-tecrmi-seamless [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -v, --version                   Show the application\'s version and exit.\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n  --help                          Show this message and exit.\n\nCommands:\n  get-api-key  Get Api Key\n  get-link     Get API Key and generate TecRMI seamless deeplink for...\n```\n\n### Generate API Key\n```\ncarooline-tecrmi-seamless get-api-key \n```\n\nThis will output your APIKey in the shell.\n\n### Get Seamless link\n\n#### Basic command to get a link\n\n```\ncarooline-tecrmi-seamless get-link \n```\n\n#### Get RMI webapp link directly on vehicle with KType:\n\nGiving a *car* id (KType):\n\n```\ncarooline-tecrmi-seamless get-link --type-id=9465\n```\n\nGiving a *truck* id (NType):\n\n```\ncarooline-tecrmi-seamless get-link --vehicle-type=trucks --type-id=13290\n```\n\n#### Options\n```shell\nOptions:\n  --catalog TEXT                  [env var: TECRMI_CATALOG; default:\n                                  TecrmiCatalog]\n  --username TEXT                 [env var: TECRMI_USERNAME; default:\n                                  TecrmiUsername]\n  --password TEXT                 [env var: TECRMI_PASSWORD; default:\n                                  TecrmiPassword]\n  --default-ttl INTEGER           Living duration of the generated TecRMI API\n                                  Key  [env var: TECRMI_DEFAULT_TTL; default:\n                                  31536000]\n  --wsdl TEXT                     [env var: TECRMI_WEBCAT_WSDL; default: https\n                                  ://webservice.tecalliance.services/webcat30/\n                                  v1/services/WebCat30WS.soapEndpoint?wsdl]\n  --lang TEXT                     [env var: TECRMI_LANG; default: fr]\n  --url TEXT                      [env var: TECRMI_WEBCAT_URL; default:\n                                  https://web.tecalliance.net]\n  --module [rmi|parts|home]       [default: TecRMIModule.rmi]\n  --vehicle-type [cars|trucks]    [default: VehicleType.cars]\n  --type-id TEXT                  KType or NType (Without the 100 prefix)\n  --display [modules|components]  [default: Display.modules]\n  --siv TEXT                      SIV search is subject to the access rights\n                                  of the credentials\n  --vin TEXT                      VIN search is subject to the access rights\n                                  of the credentials\n  --help                          Show this message and exit.\n```',
    'author': "Philippe L'ATTENTION",
    'author_email': 'philippe.lattention@hotmail.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
