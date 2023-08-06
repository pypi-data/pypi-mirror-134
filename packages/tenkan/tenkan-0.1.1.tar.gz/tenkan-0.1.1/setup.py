# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tenkan']

package_data = \
{'': ['*']}

install_requires = \
['DateTime>=4.3,<5.0',
 'feedgen>=0.9.0,<0.10.0',
 'feedparser>=6.0.8,<7.0.0',
 'markdownify>=0.10.0,<0.11.0',
 'md2gemini>=1.8.1,<2.0.0',
 'prettytable>=3.0.0,<4.0.0',
 'readability-lxml>=0.8.1,<0.9.0',
 'requests>=2.26.0,<3.0.0',
 'rich>=10.16.2,<11.0.0']

entry_points = \
{'console_scripts': ['tenkan = tenkan.cli:main']}

setup_kwargs = {
    'name': 'tenkan',
    'version': '0.1.1',
    'description': 'RSS/atom feed converter from html to gemini',
    'long_description': "# tenkan\n\nCommand line tool to convert HTTP RSS/Atom feeds to gemini format.\n\n## Installation\n```shell script\npip install tenkan\n```\n\n## Usage\n\nAdd a feed\n```shell script\n# Any valid RSS/Atom feed\ntenkan add feedname url\n```\n\nUpdate content of feed list\n```shell script\ntenkan update\n```\n\nDelete feed\n```shell script\ntenkan delete feedname\n```\n\nList subscripted feeds\n```shell script\ntenkan list\n```\n## Options\nA debug mode is avaible via --debug option.\nIf you want to use your configuration or feeds file in another place than default one, you can use --config and --feedsfile options.\n\n\n## Configuration\ntenkan searches for a configuration file at the following location:\n\n`$XDG_CONFIG_HOME/tenkan/tenkan.conf`\n\n### Example config\nThis can be found in tenkan.conf.example.\n\n```ini\n[tenkan]\ngemini_path = /usr/local/gemini/\ngemini_url = gemini://foo.bar/feeds/\n# will purge feed folders having more than defined element count\n# purge_feed_folder_after = 100\n\n[filters]\n# authors we don't want to read\n# authors_blacklist = foo, bar\n# blacklist of article titles, if provided, it won't be processed\n# titles_blacklist = foo, bar\n# blacklist of article links, if provided, it won't be processed\n# links_blacklist = foo/bar.com, bar/foo, bla\n\n[formatting]\n# maximum article title size, 120 chars if not provided\n# title_size = 120\n\n# feeds with a truncated content\n# will be fetched and converted using readability\n# truncated_feeds = foo, bar\n```\n\n## Todolist\n- [ ] Add a edit command\n- [ ] Add a --feedname option to update command, to update a single feed\n- [ ] Rewrite configuration checks\n- [ ] Improve tests\n- [ ] Refactor needed parts like write_article\n- [ ] (not sure if relevant) migrate images too, for gemini clients that can handle it\n\n## Development\nI recommend using pre-commit. The pre-commit configuration I use is located in .pre-commit-config.yamlfile.\n\nRun pre-commit command before every pull request and fix the warnings or errors it produces.\n",
    'author': 'Quentin Ferrand',
    'author_email': 'quentin.ferrand@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git.fqserv.eu/takaoni/tenkan',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
