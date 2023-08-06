from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
  name = 'datagod',
  packages = ['datagod'], # this must be the same as the name above
  version = '0.1',
  description = 'A library focused on faking data',
  author = 'gaocegege',
  author_email = 'gaocegege@hotmail.com',
  url = 'https://github.com/gaocegege/Data-God', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
  keywords = ['graph', 'data'], # arbitrary keywords
  classifiers = [],
  install_requires = ['scipy', 'numpy', 'matplotlib'],
  long_description=long_description,
  license='MIT',
)