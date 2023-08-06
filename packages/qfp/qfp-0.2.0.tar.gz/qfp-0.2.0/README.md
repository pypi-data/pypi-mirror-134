# Qfp
Qfp is a python library for creating audio fingerprints that are robust to alterations in pitch and speed. This method is ideal for ID'ing music from recordings such as DJ sets where the tracks are commonly played at a different pitch or speed than the original recording. Qfp is an implementation of the audio fingerprinting/recognition algorithms detailed in a 2016 academic paper by Reinhard Sonnleitner and Gerhard Widmer [[1]](http://www.cp.jku.at/research/papers/Sonnleitner_etal_DAFx_2014.pdf).

**NOTE**: This is a fork of https://github.com/mbortnyck/qfp/ which incorporates:
* multiple bug fixes
* Python 3 compatibilty
* modern packaging with Poetry

This is all in service of having a convient audio fingerprinting service
for a website I'm working on.
---

## Quickstart
Install by downloading it from PyPI.

```bash
pip install qfp
```

You can create a fingerprint from your reference audio...

```python
from qfp import ReferenceFingerprint

fp_r = ReferenceFingerprint("Prince_-_Kiss.mp3")
fp_r.create()
```

...or a query fingerprint from an audio clip that you wish to identify.

```python
from qfp import QueryFingerprint

fp_q = QueryFingerprint("unknown_audio.wav")
fp_q.create()
```

The QfpDB can store reference fingerprints...
```python
from qfp.db import QfpDB

db = QfpDB()
db.store(fp_r, "Prince - Kiss")
```

... and look up query fingerprints.
```python
fp_q = QueryFingerprint("kiss_pitched_up.mp3")
fp_q.create()
db.query(fp_q)
print(fp_q.matches)
```
```python
[Match(record=u'Prince - Kiss', offset=0, vScore=0.7077922077922078)]
```


Qfp currently accepts recordings in [any format that FFmpeg can handle](http://www.ffmpeg.org/general.html#File-Formats).

## Dependencies

FFmpeg - [https://github.com/FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)<br>
NumPy - [https://github.com/numpy/numpy](https://github.com/numpy/numpy)<br>
Pydub - [https://github.com/jiaaro/pydub](https://github.com/jiaaro/pydub)<br>
SciPy - [https://github.com/scipy/scipy](https://github.com/scipy/scipy)<br>
SQLite - [https://www.sqlite.org/](https://www.sqlite.org/)<br>

***
*<sub>[1]	R. Sonnleitner and G. Widmer, "Robust quad-based audio fingerprinting," IEEE/ACM Transactions on Audio, Speech and Language Processing (TASLP), vol. 24, no. 3, pp. 409–421, Jan. 2016. [Online]. Available: [http://ieeexplore.ieee.org/abstract/document/7358094/](http://ieeexplore.ieee.org/abstract/document/7358094/). Accessed: Nov. 15, 2016.<sub>*
