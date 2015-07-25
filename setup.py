try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Provides a dsl to generate random strings in forbidding context free grammars',
    'author': 'Jonah Hooper, Jeroem Smith',
    'url': 'URL to get it at.',
    'download_url': '',
    'author_email': 'jonah.graham.hooper@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [],
    'scripts': [],
    'name': 'rcfg'
}

setup(**config)
