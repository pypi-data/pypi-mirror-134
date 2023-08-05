# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notion2md', 'notion2md.convertor']

package_data = \
{'': ['*']}

install_requires = \
['notion-client>=0.7.1']

entry_points = \
{'console_scripts': ['notion2md = notion2md.cli:run']}

setup_kwargs = {
    'name': 'notion2md',
    'version': '2.2.6',
    'description': 'Notion Markdown Exporter with Python Cli',
    'long_description': '![Notion2Md logo - an arrow pointing from "N" to "MD"](Notion2md.jpg)\n\n<br/>\n\n## About Notion2Md\n\n[![PyPI version](https://badge.fury.io/py/notion2md.svg)](https://badge.fury.io/py/notion2md)\n\n- Notion Markdown Exporter using **official notion api** by [notion-sdk-py](https://github.com/ramnes/notion-sdk-py)\n\n## API Key(Token)\n\n- Before getting started, create [an integration and find the token](https://www.notion.so/my-integrations). → [Learn more about authorization](https://developers.notion.com/docs/authorization).\n\n- Then save your api key(token) as your os environment variable\n\n```Bash\n$ export NOTION_TOKEN="{your integration token key}"\n```\n\n## Install\n\n```Bash\n$ pip install notion2md\n```\n\n## Useage: Shell Command\n\n![Terminal output of the `notion2md -h` command](notion2md-options.png)\n\n```Bash\nnotion2md -p ~/MyBlog/content/posts -u https://notion.so/...\n```\n\n## Usage: Python\n```Python\nfrom notion2md.exporter import block_exporter\n\n#output_path is optional\nblock_exporter("id of notion page","OutPut Path(Relative)")\n```\n\n## To-do\n\n- [ ] Page Exporter\n- [ ] Database Exporter\n- [ ] export file object(image and files)\n- [ ] export child page\n \n## Contribution\nPull requests are welcome. \n1. folk this repo\'s **develop** branch into yours\n2. make changes and push to your **develop** branch repo\n3. send pull request from your **develop** branch to this develop branch\n\n"This will be only way to give pull request to this repo. Thank you\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'echo724',
    'author_email': 'eunchan1001@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/echo724/notion2md.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
