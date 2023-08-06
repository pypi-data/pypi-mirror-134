# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['annoworkcli',
 'annoworkcli.account',
 'annoworkcli.actual_working_time',
 'annoworkcli.annofab',
 'annoworkcli.common',
 'annoworkcli.expected_working_time',
 'annoworkcli.job',
 'annoworkcli.my',
 'annoworkcli.organization',
 'annoworkcli.organization_member',
 'annoworkcli.organization_tag',
 'annoworkcli.schedule']

package_data = \
{'': ['*'], 'annoworkcli': ['data/*']}

install_requires = \
['annofabapi>=0.52.4',
 'annofabcli>=1.55.0',
 'annoworkapi>=2.0',
 'isodate',
 'more-itertools',
 'pandas',
 'pyyaml']

entry_points = \
{'console_scripts': ['annoworkcli = annoworkcli.__main__:main']}

setup_kwargs = {
    'name': 'annoworkcli',
    'version': '2.0.2',
    'description': '',
    'long_description': None,
    'author': 'yuji38kwmt',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
