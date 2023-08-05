# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['can_show_you_anything_ai',
 'clip',
 'glide_text2im',
 'glide_text2im.clip',
 'glide_text2im.tokenizer',
 'show_anything',
 'tokenizer',
 'txt2img',
 'txt2img.utils']

package_data = \
{'': ['*']}

install_requires = \
['Pillow==9.0.0',
 'attrs==21.2.0',
 'filelock==3.4.0',
 'fire>=0.4.0,<0.5.0',
 'folium==0.2.1',
 'ftfy>=6.0.3,<7.0.0',
 'imgaug==0.2.6',
 'regex>=2021.11.10,<2022.0.0',
 'requests==2.23.0',
 'torch>=1.10.0+cu111,<2.0.0',
 'tqdm==4.62.3']

entry_points = \
{'console_scripts': ['show_me_a = txt2img:cli',
                     'showme = txt2img:cli',
                     'showmea = txt2img:cli']}

setup_kwargs = {
    'name': 'can-show-you-anything-ai',
    'version': '0.1.17',
    'description': '',
    'long_description': None,
    'author': 'Richard Brooker',
    'author_email': 'richard@anghami.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
