# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qfp']

package_data = \
{'': ['*']}

install_requires = \
['bitstring>=3.1.9,<4.0.0',
 'numpy>=1.22.1,<2.0.0',
 'pydub>=0.25.1,<0.26.0',
 'scipy>=1.7.3,<2.0.0']

setup_kwargs = {
    'name': 'qfp',
    'version': '0.2.0',
    'description': 'Quad-based audio fingerprinting (fork of https://github.com/mbortnyck/qfp)',
    'long_description': '# Qfp\nQfp is a python library for creating audio fingerprints that are robust to alterations in pitch and speed. This method is ideal for ID\'ing music from recordings such as DJ sets where the tracks are commonly played at a different pitch or speed than the original recording. Qfp is an implementation of the audio fingerprinting/recognition algorithms detailed in a 2016 academic paper by Reinhard Sonnleitner and Gerhard Widmer [[1]](http://www.cp.jku.at/research/papers/Sonnleitner_etal_DAFx_2014.pdf).\n\n**NOTE**: This is a fork of https://github.com/mbortnyck/qfp/ which incorporates:\n* multiple bug fixes\n* Python 3 compatibilty\n* modern packaging with Poetry\n\nThis is all in service of having a convient audio fingerprinting service\nfor a website I\'m working on.\n---\n\n## Quickstart\nInstall by downloading it from PyPI.\n\n```bash\npip install qfp\n```\n\nYou can create a fingerprint from your reference audio...\n\n```python\nfrom qfp import ReferenceFingerprint\n\nfp_r = ReferenceFingerprint("Prince_-_Kiss.mp3")\nfp_r.create()\n```\n\n...or a query fingerprint from an audio clip that you wish to identify.\n\n```python\nfrom qfp import QueryFingerprint\n\nfp_q = QueryFingerprint("unknown_audio.wav")\nfp_q.create()\n```\n\nThe QfpDB can store reference fingerprints...\n```python\nfrom qfp.db import QfpDB\n\ndb = QfpDB()\ndb.store(fp_r, "Prince - Kiss")\n```\n\n... and look up query fingerprints.\n```python\nfp_q = QueryFingerprint("kiss_pitched_up.mp3")\nfp_q.create()\ndb.query(fp_q)\nprint(fp_q.matches)\n```\n```python\n[Match(record=u\'Prince - Kiss\', offset=0, vScore=0.7077922077922078)]\n```\n\n\nQfp currently accepts recordings in [any format that FFmpeg can handle](http://www.ffmpeg.org/general.html#File-Formats).\n\n## Dependencies\n\nFFmpeg - [https://github.com/FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)<br>\nNumPy - [https://github.com/numpy/numpy](https://github.com/numpy/numpy)<br>\nPydub - [https://github.com/jiaaro/pydub](https://github.com/jiaaro/pydub)<br>\nSciPy - [https://github.com/scipy/scipy](https://github.com/scipy/scipy)<br>\nSQLite - [https://www.sqlite.org/](https://www.sqlite.org/)<br>\n\n***\n*<sub>[1]\tR. Sonnleitner and G. Widmer, "Robust quad-based audio fingerprinting," IEEE/ACM Transactions on Audio, Speech and Language Processing (TASLP), vol. 24, no. 3, pp. 409–421, Jan. 2016. [Online]. Available: [http://ieeexplore.ieee.org/abstract/document/7358094/](http://ieeexplore.ieee.org/abstract/document/7358094/). Accessed: Nov. 15, 2016.<sub>*\n',
    'author': 'Michael Bortnyck',
    'author_email': 'michael.bortnyck@gmail.com',
    'maintainer': 'Kyle Anthony Williams',
    'maintainer_email': 'kyle.anthony.williams2@gmail.com',
    'url': 'https://github.com/SuperSonicHub1/qfp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
