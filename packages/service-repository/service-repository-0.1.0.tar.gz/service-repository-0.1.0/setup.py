# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['service_repository',
 'service_repository.interfaces',
 'service_repository.repositories']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'service-repository',
    'version': '0.1.0',
    'description': 'Simple service layer with repository to SQLAlchemy or MongoDB',
    'long_description': '# Service layer and repository for SQLAlchemy or MongoDB (asynchronous)\n\nSimple service layer with repository to SQLAlchemy with SQLModel or MongoDB with Motor.',
    'author': 'Fernando Miranda',
    'author_email': 'fndmiranda@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fndmiranda/service-repository',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
