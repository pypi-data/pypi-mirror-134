# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['migu_music_dl']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0', 'prettytable>=3.0.0,<4.0.0', 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['migu-music-dl = migu_music_dl.cli: download']}

setup_kwargs = {
    'name': 'migu-music-dl',
    'version': '0.1.1',
    'description': 'Migu music downloader',
    'long_description': "\n# MIGU-Music-dl   \n\n![Publish Action](https://github.com/swim2sun/migu-music-dl/actions/workflows/publish.yml/badge.svg)\n\nDownload Migu Lossless Music\n\n## Installation\n\n```shell\n$ pip install migu-music-dl\n```\n    \n\nUsage\n-----\n\n```shell\n$ migu-music-dl [OPTIONS] SEARCH_KEYWORD OUTPUT_DIR\n```\n\n\nFor example:\n\n```\n➜  migu-music-dl '周杰伦' .\n\n+-----+-----------------------------------+--------+---------------+\n| No. | Title                             | Artist |     Album     |\n+-----+-----------------------------------+--------+---------------+\n|  1  | 花海                              | 周杰伦 |     魔杰座    |\n|  2  | 我是如此相信 (电影《天火》主题曲) | 周杰伦 |  我是如此相信 |\n|  3  | 七里香                            | 周杰伦 |   Initial J   |\n|  4  | 反方向的钟                        | 周杰伦 | Partners 拍档 |\n|  5  | 晴天                              | 周杰伦 |     叶惠美    |\n|  6  | 一路向北 (电影《头文字Ｄ》插曲)   | 周杰伦 |  十一月的萧邦 |\n|  7  | 明明就                            | 周杰伦 |               |\n|  8  | 稻香                              | 周杰伦 |     魔杰座    |\n|  9  | 夜曲                              | 周杰伦 |  十一月的萧邦 |\n|  10 | 爱在西元前                        | 周杰伦 | Partners 拍档 |\n|  11 | 搁浅                              | 周杰伦 |     七里香    |\n|  12 | 半岛铁盒                          | 周杰伦 |    八度空间   |\n|  13 | 兰亭序                            | 周杰伦 |     魔杰座    |\n|  14 | 枫                                | 周杰伦 |  十一月的萧邦 |\n|  15 | 给我一首歌的时间                  | 周杰伦 |     魔杰座    |\n|  16 | 以父之名                          | 周杰伦 |   Initial J   |\n|  17 | 轨迹(电影《寻找周杰伦》主题曲)    | 周杰伦 |               |\n|  18 | 等你下课(with 杨瑞代)             | 周杰伦 |    等你下课   |\n|  19 | 蒲公英的约定                      | 周杰伦 |     我很忙    |\n|  20 | 夜的第七章                        | 周杰伦 |   依然范特西  |\n+-----+-----------------------------------+--------+---------------+\ninput No. to download (split with , for download multiple songs, for example: 1,3,5): 14,16\nselected: 枫, 以父之名\n枫.flac  [####################################]  100%\n以父之名.flac  [####################################]  100%\n\n```\n",
    'author': 'swim2sun',
    'author_email': 'xiangyangyou@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/swim2sun/migu-music-dl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
