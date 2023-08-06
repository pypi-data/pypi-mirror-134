# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fixations']

package_data = \
{'': ['*'],
 'fixations': ['fix_repository_2010_edition_20200402/*',
               'fix_repository_2010_edition_20200402/FIX.4.0/Base/*',
               'fix_repository_2010_edition_20200402/FIX.4.1/Base/*',
               'fix_repository_2010_edition_20200402/FIX.4.2/*',
               'fix_repository_2010_edition_20200402/FIX.4.2/Base/*',
               'fix_repository_2010_edition_20200402/FIX.4.3/Base/*',
               'fix_repository_2010_edition_20200402/FIX.4.4/Base/*',
               'fix_repository_2010_edition_20200402/FIX.5.0/Base/*',
               'fix_repository_2010_edition_20200402/FIX.5.0SP1/Base/*',
               'fix_repository_2010_edition_20200402/FIX.5.0SP2/Base/*',
               'fix_repository_2010_edition_20200402/FIXT.1.1/Base/*',
               'fix_repository_2010_edition_20200402/Unified/*',
               'fix_repository_2010_edition_20200402/schema/*',
               'fix_repository_2010_edition_20200402/xsl/*']}

install_requires = \
['dataclasses-json==0.5.6',
 'tabulate==0.8.9',
 'termcolor>=1.1.0,<1.2.0',
 'urwid>=2.1,<3.0']

entry_points = \
{'console_scripts': ['fix_parse_log = fixations:fix_parse_log.py',
                     'fix_tags = fixations:fix_tags.py']}

setup_kwargs = {
    'name': 'fixations',
    'version': '0.1.4',
    'description': 'This is a set of tools to handle FIX protocol data',
    'long_description': '# Fixations\n**This is a set of tools to handle FIX protocol data**\n\n## Data source\nThe data is extracted from the FIX specs available here: \n\nhttps://www.fixtrading.org/standards/fix-repository/fix_repository_2010_edition_20200402',
    'author': 'Jerome Provensal',
    'author_email': 'jeromegit@provensal.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jeromegit/fixations',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
