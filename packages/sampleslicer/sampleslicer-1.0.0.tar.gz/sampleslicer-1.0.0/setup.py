from setuptools import setup, find_packages

import os
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='sampleslicer',
      version='1.0.0',
      description='Graphically slice up 4-dimensional datasets using quaternions.',
      long_description=long_description,
      long_description_content_type="text/x-rst",
      url='https://doi.org/10.5281/zenodo.5523256',
      author='John W',
      license='GPLv3',
      packages=find_packages(),
      package_data={'sampleslicer': ['template/*.py']},
      install_requires=install_requires,
      entry_points={
          "console_scripts": [
              "sslice = sampleslicer.cli:main",
          ]
      }
      )
