# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hag', 'hag.displays', 'hag.extractors', 'hag.extractors.sources']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['hag = hag.__main__:main']}

setup_kwargs = {
    'name': 'hag',
    'version': '0.1.1',
    'description': 'A hotkey aggregator. All your hotkeys in one place.',
    'long_description': '<h1 align="center">hag</h1>\n<h5 align="center">A Hotkey AGgregator.</h5>\n<p align="center">\n  <a href="https://pypi.org/project/hag/"><img src="https://img.shields.io/pypi/v/hag"></a>\n  <a href="./LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>\n  <img src="https://img.shields.io/badge/platform-linux-informational">\n</p>\n\n`hag` is a a hotkey aggregator, it tries its best to extract the hotkeys of your software and display them.\n\nIt does so by parsing the config files, man pages, command outputs, ... depending on the software.\n\n## Programs\n\nBellow is a list of implemented software:\n\n- Lazygit\n- Lf\n- Mpv\n- Neovim\n- Qutebrowser\n- Rofi\n- Sxhkd\n- Sxiv\n- Termite\n- Vim\n- Vimiv\n- Zathura\n- Zsh\n\n## Installation\n\n`hag` is meant to be relatively minimal, as such it doesn\'t have any dependencies.\n\n```\npip install hag\n```\n\nIf you just want to use the CLI interface, consider using [`pipx`](https://github.com/pypa/pipx).\n\n```\npipx install hag\n```\n\n## Usage\n\n```\n$ hag --help\nusage: hag [-h] [-le | -ld] [-d {json,text}] [-m MODES] [-v] [{lazygit,lf,mpv,neovim,qutebrowser,rofi,sxhkd,sxiv,termite,vim,vimiv,zathura,zsh}]\n\nHotkey aggregator. All your hotkeys in one place.\n\npositional arguments:\n  {lazygit,lf,mpv,neovim,qutebrowser,rofi,sxhkd,sxiv,termite,vim,vimiv,zathura,zsh}\n                        Extract hotkeys using extractor.\n\noptions:\n  -h, --help            show this help message and exit\n  -le, --list-extractors\n                        List available hotkey extractors.\n  -ld, --list-displays  List available display methods.\n  -d {json,text}, --display {json,text}\n                        Display method.\n  -m MODES, --modes MODES\n                        Filter by mode, if supported by extractor.\n  -v, --version         Show hag version and exit.\n```\n\n### Examples\n\nA few example uses:\n\n- List [`sxhkd`](https://github.com/baskerville/sxhkd) hotkeys:\n  ```sh\n  hag sxhkd\n  ```\n- Display `sxhkd` hotkeys in json format and format with [`jq`](https://github.com/stedolan/jq):\n\n  ```sh\n  hag sxhkd -d json | jq\n  ```\n\n- Show `vim` Normal and Visual mode hotkeys in [`rofi`](https://github.com/davatorium/rofi):\n  ```sh\n  hag vim -m Normal | rofi -dmenu\n  ```\n- Use `rofi` to select software and show hotkeys:\n  ```sh\n  extractor="$(hag -le | rofi -dmenu)" && hag "$extractor" | rofi -dmenu\n  ```\n\n# Contributing\n\nIf you want to add support for your favourite software, feel free to open issues/PRs!\n',
    'author': 'Loic Coyle',
    'author_email': 'loic.coyle@hotmail.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/loiccoyle/hag',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
