from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='swagger_ui',
    version='0.1',
    install_requires=requirements,
    packages=find_packages()
)

from distutils.core import setup
setup(
  name = 'swagger_ui',
  packages = find_packages(),
  version = '0.1',
  license='GPL-3.0',
  description = 'An extension to flask_restplus that can convert back-end objects into APIs',
  author = 'Alireza Davoudi',
  author_email = 'davoudialireza@gmail.com',
  url = 'https://github.com/Faraadid/swagger_ui',
  download_url = 'https://github.com/Faraadid/swagger_ui/archive/v0.1.tar.gz',
  keywords = ['flask_restplus', 'swagger', 'swagger ui'],
  install_requires=requirements,
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
  ],
)
