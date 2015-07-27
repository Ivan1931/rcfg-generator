config = {
    'description': 'Provides a dsl to generate random strings in forbidding context free grammars',
    'author': 'Jonah Hooper, Jeroen Schmidt',
    'url': '',
    'download_url': '',
    'author_email': 'jonah.graham.hooper@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'funcy'],
    'packages': [],
    'scripts': [],
    'name': 'rcfg',
    'licence': 'MIT'
}

try:
    from setuptools import setuptools
    setuptools.setup(**config)
except ImportError:
    from distutils.core import setup
    setup(**config)
