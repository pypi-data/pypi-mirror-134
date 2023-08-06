# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['afrr_remuneration']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.3.4,<2.0.0',
 'poetry-dynamic-versioning>=0.13.1,<0.14.0',
 'pytest>=6.2.5,<7.0.0']

setup_kwargs = {
    'name': 'afrr-remuneration',
    'version': '0.0.1',
    'description': 'Calculate aFRR remuneration in resolution of seconds',
    'long_description': '<a href="https://www.e2m.energy/"><img src="https://user-images.githubusercontent.com/8255114/148765040-975650b6-1db2-4537-aac4-0840f28bf678.png" alt="e2m logo" title="e2m" height="50" align="right"></a>\n\n# aFRR remuneration\n\nA tool to calculate the aFRR remuneration for the european energy market.\n\n## About\n\nThis project was initiated with the start of aFRR remuneration in temporal resolution of seconds on October 1st 2021 \nwhich is one further step to fulfill the EU target market design.\nThe motivation for creating this python package is to provide a tool for evaluating remuneration of aFRR activation \nevents by TSOs.\nTherefore, it provides an implementation of the calculation procedure described in the \n[model description](https://www.regelleistung.net/ext/download/Modellbeschreibung_aFRR-Abrechnung_ab_01.10.2021) as \npython code.\n\n\n## Installation \n\nWe aim to release a package on PyPi soonish. Until then, please see in \n[development installation](#Development-installation) how to install the package from sources.\n\n## Usage\n\nHere is some example code that shows how use functionality of this package. \nMake sure you have a file at hand with data about setpoints and actual values of an aFRR activation event. See the \nexample files from \n[regelleistung.net](https://www.regelleistung.net/ext/download/Beispieldateien_aFRR-Abrechnung_ab_01.10.2021) to \nunderstand the required file format.\nNote, you have to make sure that data starts at the beginning of an aFRR activation event.\n\n````python \nfrom afrr_renumeration.aFRR import calc_acceptance_tolerance_band, calc_underfulfillment_and_account\nfrom afrr_renumeration.data import parse_tso_data\n\n# load the setpoint and the measured value for example by reading the tso data\nfile = "20211231_aFRR_XXXXXXXXXXXXXXXX_XXX_PT1S_043_V01.csv"\ntso_df = parse_tso_data(file)\n\n# calculate the tolerance band \nband_df = calc_acceptance_tolerance_band(\n    setpoint=tso_df["setpoint"], measured=tso_df["measured"]\n    )\n\n# calculate acceptance values and other relevant serieses like the under-/overfulfillment \nunderful_df = calc_underfulfillment_and_account(\n    setpoint=band_df.setpoint,\n    measured=band_df.measured,\n    upper_acceptance_limit=band_df.upper_acceptance_limit,\n    lower_acceptance_limit=band_df.lower_acceptance_limit,\n    lower_tolerance_limit=band_df.lower_tolerance_limit,\n    upper_tolerance_limit=band_df.upper_tolerance_limit,\n)\n\n\n````\n\n## Next Steps\n\nWe plan to\n\n- [ ] Add a testfile with artificial data\n- [ ] Add an example with a valid MOL\n\nFeel free to help us here!\n\n## Contributing\n\nContributions are highly welcome. For more details, please have a look in to \n[contribution guidelines](https://github.com/energy2market/afrr-remuneration/blob/main/CONTRIBUTING.md).\n\n### Development installation\n\nFor installing the package from sources, please clone the repository with\n\n```bash\ngit clone git@github.com:energy2market/afrr-remuneration.git\n```\n\nThen, in the directory `afrr-remuneration` (the one the source code was cloned to), execute\n\n```bash\npoetry install\n```\n\nwhich creates a virtual environment under `./venv` and installs required package and the package itself to this virtual environment.\nRead here for more information about <a href="https://python-poetry.org/">poetry</a>.',
    'author': 'Guido Pleßmann',
    'author_email': 'guido.plessmann@e2m.energy',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/energy2market/afrr-remuneration',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
