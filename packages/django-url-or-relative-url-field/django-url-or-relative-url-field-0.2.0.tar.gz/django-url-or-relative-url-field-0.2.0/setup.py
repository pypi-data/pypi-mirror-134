# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['url_or_relative_url_field']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2.25']

setup_kwargs = {
    'name': 'django-url-or-relative-url-field',
    'version': '0.2.0',
    'description': 'This package provides a Django model field that can store both absolute and relative URLs',
    'long_description': "# Django URL or Relative URL Field\n\nThis package extends default Django URLField to support relative URLs.\n\n\n## Installation\n\n1. Install the python package django-url-or-relative-url-field from pip:\n\n    ``pip install django-url-or-relative-url-field``\n\n    Alternatively, you can install download or clone this repo and call ``pip install -e .``.\n  \n2. Add to INSTALLED_APPS in your **settings.py**:\n\n    `'url_or_relative_url_field',`\n  \n## Usage  \n  \nAdd field to the model:\n\n```python\nfrom django.db import models\nfrom url_or_relative_url_field.fields import URLOrRelativeURLField\n\nclass Redirect(models.Model):\n   url = URLOrRelativeURLField()\n```\n\nNow your model will accept both absolute and relative URLs into the ``url`` field.\n",
    'author': 'Tim Kamanin',
    'author_email': 'tim@timonweb.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/timonweb/django-url-or-relative-url-field',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
