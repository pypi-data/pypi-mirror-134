# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['django_security_keys',
 'django_security_keys.ext',
 'django_security_keys.ext.two_factor',
 'django_security_keys.migrations']

package_data = \
{'': ['*'],
 'django_security_keys': ['static/base64/*',
                          'static/django-security-keys/*',
                          'templates/django-security-keys/*']}

install_requires = \
['django-two-factor-auth>=1.13.1,<2.0.0', 'webauthn>=1,<2']

entry_points = \
{'markdown.extensions': ['pymdgen = pymdgen.md:Extension']}

setup_kwargs = {
    'name': 'django-security-keys',
    'version': '1.0.0',
    'description': 'Django webauthn security key integration',
    'long_description': '\n# django-security-keys\n\n[![PyPI](https://img.shields.io/pypi/v/django-security-keys.svg?maxAge=60)](https://pypi.python.org/pypi/django-security-keys)\n[![PyPI](https://img.shields.io/pypi/pyversions/django-security-keys.svg?maxAge=600)](https://pypi.python.org/pypi/django-security-keys)\n[![Tests](https://github.com/20c/django-security-keys/workflows/tests/badge.svg)](https://github.com/20c/django-security-keys)\n[![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/20c/django-security-keys)](https://lgtm.com/projects/g/20c/django-security-keys/alerts/)\n[![Codecov](https://img.shields.io/codecov/c/github/20c/django-security-keys/master.svg)](https://codecov.io/github/20c/django-security-keys)\n\nDjango webauthn security key support\n\nAllows using webauthn for passwordless login and two-factor authentication.\n\n2FA integration requires django-two-factor-auth and is handled by extending a custom django-otp device.\n\n## Changes\n\nThe current change log is available at <https://github.com/20c/django-security-keys/blob/master/CHANGELOG.md>\n\n## License\n\nCopyright 2021 20C, LLC\n\nLicensed under the Apache License, Version 2.0 (the "License");\nyou may not use this software except in compliance with the License.\nYou may obtain a copy of the License at\n\n   http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n',
    'author': '20C',
    'author_email': 'code@20c.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fullctl/django-security-keys',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
