# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['serverless',
 'serverless.aws',
 'serverless.aws.alerts',
 'serverless.aws.features',
 'serverless.aws.functions',
 'serverless.aws.iam',
 'serverless.service',
 'serverless.service.plugins']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'stringcase>=1.2.0,<2.0.0', 'troposphere>=3.2,<3.3']

setup_kwargs = {
    'name': 'serverless-builder',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Epsy',
    'author_email': 'engineering@epsyhealth.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
