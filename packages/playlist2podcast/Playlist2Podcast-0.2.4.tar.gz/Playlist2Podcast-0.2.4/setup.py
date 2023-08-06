# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['playlist2podcast']
install_requires = \
['Pillow>=9.0.0,<10.0.0',
 'arrow>=1.2.1,<2.0.0',
 'feedgen>=0.9.0,<0.10.0',
 'httpx>=0.19,<1.0',
 'rich>=11.0.0,<12.0.0',
 'youtube_dl>=2021.12.17,<2022.0.0']

setup_kwargs = {
    'name': 'playlist2podcast',
    'version': '0.2.4',
    'description': 'Creates podcast feed from playlist URL',
    'long_description': '# Playlist2Podcast\n\nPlaylist2Podcast is a command line tool that takes a Youtube playlist and creates a podcast feed from this.\n\nPlaylist2Podcast is not mature yet and might fail with uncaught errors. If you encounter an error, please create an\n[issue](https://codeberg.org/PyYtTools/Playlist2Podcasts/issues)\n\nCurrently, Playlist2Podcast:\n1) downloads and converts the videos in one or more playlists to opus audio only files,\n2) downloads thumbnails and converts them to JPEG format, and\n3) creates a podcast feed with the downloaded videos and thumbnails.\n\nBefore running, install [Python Poetry](https://python-poetry.org/) and run `poetry install`.\n\nPlaylist2Podcast will ask for all necessary parameters when run for the first time and store them in `config.json`\nfile in the current directory.\n\nRun Playlist2Podcast with the command `poetry run python playlist2podcast.py`\n\nPlaylist2Podcast is licences under licensed under\nthe [GNU Affero General Public License v3.0](http://www.gnu.org/licenses/agpl-3.0.html)\n',
    'author': 'marvin8',
    'author_email': 'marvin8@tuta.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://codeberg.org/PyYtTools/Playlist2Podcasts',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
