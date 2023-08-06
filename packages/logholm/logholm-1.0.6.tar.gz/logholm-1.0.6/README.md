<div align="center">
    <img alt="Logholm Banner" src="media/banner.svg" style="width: 65%"><br>
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/stockholmdev/logholm-python?style=for-the-badge">
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/stockholmdev/logholm-python?style=for-the-badge">
    <img alt="License" src="https://img.shields.io/github/license/stockholmdev/logholm-python?style=for-the-badge">
    <img alt="Platforms" src="https://img.shields.io/badge/Platforms-Windows%20%7C%20Linux-blue?style=for-the-badge">
    <img alt="Python Versions" src="https://img.shields.io/badge/Python%20-3.7%2F8%2F9%2F10-blue?style=for-the-badge"><br><br>
    The most powerful and easy to code logging library. It can work with asyncio <br>
    library for async programs. It have a realization for different programing languages. <br><br>
    <a href="https://github.com/stockholmdev/logholm-python/wiki"><b>Wiki</b></a>&nbsp;&nbsp;&nbsp;
    <a href="https://github.com/stockholmdev/logholm-python/issues"><b>Issues</b></a>&nbsp;&nbsp;&nbsp;
    <a href="https://teletype.in/@stockholm/+logholm-python-library"><b>Blog</b></a>&nbsp;&nbsp;&nbsp;
    <a href="https://github.com/stockholmdev/logholm-python/releases"><b>Releases</b></a>&nbsp;&nbsp;&nbsp;
    <a href="https://pypi.org/project/logholm/"><b>PyPi</b></a>&nbsp;&nbsp;&nbsp;<br><br>
</div>

## Installation
### Installation via PyPi (pip)
You can see package here: https://pypi.org/project/logholm/

To install it - run this in cmd:
```
pip install logholm
```
## Note to library building
### How to build and publish lib to PyPi
You need to install 2 packages - setuptools, twine.
```
pip install setuptools
pip install twine
```
Use first command to build library and second to publish it to PyPi:
```
python setup.py sdist
twine upload dist/*
```
