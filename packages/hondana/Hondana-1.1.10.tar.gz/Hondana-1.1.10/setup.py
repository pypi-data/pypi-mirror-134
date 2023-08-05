# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hondana', 'hondana.types']

package_data = \
{'': ['*'], 'hondana': ['extras/*']}

modules = \
['py', 'tags']
install_requires = \
['aiofiles>=0.7.0,<0.8.0', 'aiohttp>=3.7.4,<4.0.0']

extras_require = \
{'docs': ['sphinx>=4.0.0,<5.0.0', 'sphinxcontrib-trio', 'furo']}

entry_points = \
{'console_scripts': ['version = hondana.__main__:show_version']}

setup_kwargs = {
    'name': 'hondana',
    'version': '1.1.10',
    'description': 'An asynchronous wrapper around the MangaDex v5 API',
    'long_description': '<div align="center">\n    <h1><a href="https://jisho.org/word/%E6%9C%AC%E6%A3%9A">Hondana 『本棚』</a></h1>\n    <a href=\'https://hondana.readthedocs.io/en/latest/?badge=latest\'>\n        <img src=\'https://readthedocs.org/projects/hondana/badge/?version=latest\' alt=\'Documentation Status\' />\n    </a>\n    <a href=\'https://github.com/AbstractUmbra/Hondana/actions/workflows/build.yaml\'>\n        <img src=\'https://github.com/AbstractUmbra/Hondana/workflows/Build/badge.svg\' alt=\'Build status\' />\n    </a>\n    <a href=\'https://github.com/AbstractUmbra/Hondana/actions/workflows/coverage_and_lint.yaml\'>\n        <img src=\'https://github.com/AbstractUmbra/Hondana/workflows/Lint/badge.svg\' alt=\'Linting and Typechecking\' />\n    </a>\n</div>\n<div align="center">\n    <a href=\'https://api.mangadex.org/\'>\n        <img src=\'https://img.shields.io/website?down_color=red&down_message=offline&label=API%20Status&logo=MangaDex%20API&up_color=lime&up_message=online&url=https%3A%2F%2Fapi.mangadex.org%2Fping\' alt=\'API Status\'/>\n    </a>\n</div>\n<br>\n\nA lightweight and asynchronous wrapper around the [MangaDex v5 API](https://api.mangadex.org/docs.html).\n\n## Features\nAs it stands, we have 100% API coverage.\nI will update this if it ever changes.\n\n\n## Note about authentication\nSadly (thankfully?) I am not an author on MangaDex, meaning I cannot test the creation endpoints for things like scanlators, artists, authors, manga or chapters.\nI have followed the API guidelines to the letter for these, but they may not work.\n\nAny help in testing them is greatly appreciated.\n\n## Note about upload/creation\nFollowing the above, this means I also cannot test manga creation or chapter creation/upload.\nThese are currently implemented but untested.\n\n## Examples\nPlease take a look at the [examples](./examples/) directory for working examples.\n\n**NOTE**: More examples will follow as the library is developed.\n\n### API caveats to note\n\n- There are no API endpoints for Artist. It seems they are not differentiated from Author types except in name only.\n  - I have separated them logically, but under the hood all Artists are Authors and their `__eq__` reports as such.\n- The tags are locally cached since you **must** pass UUIDs to the api (and I do not think you\'re going to memorize those), there\'s a convenience method for updating the local cache as `Client.update_tags`\n  - I have added [an example](./examples/updating_local_tags.py) on how to do the above.\n',
    'author': 'Alex Nørgaard',
    'author_email': 'Umbra@AbstractUmbra.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/AbstractUmbra/hondana',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
