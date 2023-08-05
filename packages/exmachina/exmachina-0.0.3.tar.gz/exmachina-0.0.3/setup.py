# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['exmachina', 'exmachina.lib']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.71.0,<0.72.0']

setup_kwargs = {
    'name': 'exmachina',
    'version': '0.0.3',
    'description': 'botを作るためのフレームワークです',
    'long_description': '# Ex-Machina\n\n[![python-version](https://img.shields.io/pypi/pyversions/exmachina)](https://pypi.org/project/exmachina/)\n[![Test](https://github.com/agarichan/exmachina/actions/workflows/test.yaml/badge.svg)](https://github.com/agarichan/exmachina/actions/workflows/test.yaml)\n\npython で bot 書くためのフレームワークです。\n\n## インストール\n\nusing pip\n\n```\npip install exmachina\n```\n\nusing poetry\n\n```\npoetry add exmachina\n```\n\n## 開発\n\n### init\n\n```bash\npoetry install\npoetry shell\n```\n\n### fmt\n\n```\npoe fmt\n```\n\n### lint\n\n```\npoe lint\n```\n\n### test\n\n```\npoe test\n```\n',
    'author': 'agarichan',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/agarichan/exmachina',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
