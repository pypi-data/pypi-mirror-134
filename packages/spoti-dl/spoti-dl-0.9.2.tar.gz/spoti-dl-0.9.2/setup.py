# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spotidl']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.19.2,<0.20.0',
 'spotipy>=2.19.0,<3.0.0',
 'yt-dlp>=2021.12.27,<2022.0.0']

entry_points = \
{'console_scripts': ['spotidl = spotidl.cli:controller']}

setup_kwargs = {
    'name': 'spoti-dl',
    'version': '0.9.2',
    'description': 'spotidl: download songs, albums and playlists using Spotify links',
    'long_description': '# Introduction\n\nyet Another Song Downloader, yASD for short(I couldn\'t think of a better name, sorry!), is a song downloader app that accepts Spotify links, fetches individual song—and basic album—metadata from Spotify, downloads the song from Youtube. The metadata is then written onto the downloaded song file using the trusty Mutagen library, this includes the album/song cover art as well. \n\nThe app currently supports downloading songs, albums and playlists in the mp3, flac and m4a formats(the m4a format right now does not have full textual metadata support but I\'m working on it 😅). \n\nI got the inspiration for the project from my friend Swapnil\'s [spotify-dl](https://github.com/SwapnilSoni1999/spotify-dl) app written in JavaScript. This seemed like the perfect pet project to make and consequently learn from :)\n\n\n# Setup\n\nyASD needs two things to work: [FFmpeg](https://ffmpeg.org/download.html) and a Spotify developer account.\n\nSteps to make a Spotify developer account:\n1. Go to [Spotify Dev Dashboard](https://developer.spotify.com/dashboard/applications)\n2. Login with your credentials and click on "create an app".\n3. Enter any name of choice, app description, tick the checkbox and proceed.\n4. Now you have access to your client ID. Click on "Show client secret" to get your client secret.\n5. From here, click on "edit settings" and in the "redirect URIs" section add any localhost URL. I personally use ```http://localhost:8080/callback```\n\nFinally, copy your client ID, client secret and the redirect URI and paste them in the .env.example file opposite the appropriate variables. Rename the .env.example file to .env and you\'re good to go!\n\n\n# Usage\n\nWIP\n',
    'author': 'Dhruv',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/good-times-ahead/spoti-dl/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
