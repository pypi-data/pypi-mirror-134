# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lexy', 'lexy.core']

package_data = \
{'': ['*']}

install_requires = \
['cattrs>=1.10.0,<2.0.0', 'pandas>=1.3.5,<2.0.0', 'spacy>=3.2.1,<4.0.0']

setup_kwargs = {
    'name': 'lexy',
    'version': '0.1.0',
    'description': 'Lexy enables you to easily build and share data dictionaries to explain and document your data terminology using code.',
    'long_description': '# Lexy \n![test](https://github.com/aminekaabachi/lexy/workflows/test/badge.svg?branch=main) \n[![codecov](https://codecov.io/gh/aminekaabachi/lexy/branch/main/graph/badge.svg)](https://codecov.io/gh/aminekaabachi/lexy) \n[![PyPI](https://img.shields.io/pypi/v/lexy?style=flat-square)](https://pypi.org/project/lexy/)\n[![Downloads](https://img.shields.io/pypi/dm/lexy?style=flat-square)](https://pypi.org/project/lexy/)\n[![Docs](https://readthedocs.org/projects/lexy/badge/?version=latest&style=flat-square)](https://lexy.readthedocs.io/en/latest/)\n[![GitHub](https://img.shields.io/github/license/aminekaabachi/lexy?style=flat-square)](https://github.com/aminekaabachi/lexy/blob/main/LICENSE)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n✨ ***Lexy** enables you to easily build and share data dictionaries to explain and document your data terminology using code.* The name "Lexy" is inspired from [lexicographer (/ˌlɛksɪˈkɒɡrəfə/)](https://www.lexico.com/definition/lexicographer), the person who compiles dictionaries.\n\n\n-----------------\n\nEasily document your data objects and generate beautiful data dictionaries:\n```python\nimport lexy as xy\nglossary = xy.Glossary()\n\n#Defining glossary terms\nglossary("name", "name of the student")\nglossary("lastname", "lastname of the student")\nglossary("age", "age of the student", sensitivity="private")\n\n#Using the glossary to define pandas dataframe\nimport pandas as pd\ndata = [[\'tom\', \'bird\', 10], [\'nick\', \'star\', 15], [\'juli\', \'aston\', 14]] \ndf = pd.DataFrame(data, columns = [glossary(\'name\'), glossary(\'lastname\'), glossary(\'age\')]) \n\nxy.display_docs(glossary)\n```\n\n![Displayed docs](demo.png?raw=true "lexy Documentation")\n\n\n## Beloved Features\n\n✨ **Lexy** will be soon ready for your use-case:\n\n- ✔ Clear standard way to define data dictionaries using code.\n- ✔ Tracking of glossary usage throughout the code.\n- ✔ Display / Generate of documentation pages for your data glossaries.\n- ✔ Detection of similarity between the terms and warning about possible data dictionary issues.\n- Validation of data dictionaries using defined templates and tools.\n- ✔ Import / export data dictionary from different formats (csv, excel, etc)\n- AI Suggesting of metadata based on name and definition (personal data, data types, ...)\n- Support for multiple backends (Memory, File, Redis, CloudFile...)\n- Integration with Apache Atlas and Azure Purview.\n- Publish data dictionary to lexyHub using the cli.\n',
    'author': 'Amine Kaabachi',
    'author_email': 'ping@kaabachi.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aminekaabachi/lexy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
