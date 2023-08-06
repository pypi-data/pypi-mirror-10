# setuptools installation of Hop
# Copyright (c) 2007-2014 Oliver Beckstein <orbeckst@gmail.com>
# Released under the GNU Public License 3 (or higher, your choice)
# See the file COPYING for details.
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

summary = open("README.rst")
try:
    long_description = summary.read()
finally:
    summary.close()

setup(name="GridDataFormats",
      version="0.2.5",    # keep in sync with __init__.py: __version__ and docs/source/conf.py
      description="Reading and writing of data on regular grids in Python",
      long_description=long_description,
      author="Oliver Beckstein",
      author_email="orbeckst@gmail.com",
      license="LGPLv3",
      url="https://github.com/MDAnalysis/GridDataFormats",
      download_url = "https://github.com/MDAnalysis/GridDataFormats/releases",
      keywords="science array density",
      classifiers = ['Development Status :: 4 - Beta',
                     'Environment :: Console',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                     'Programming Language :: Python',
                     'Topic :: Scientific/Engineering',
                     'Topic :: Software Development :: Libraries :: Python Modules',
                     ],
      packages=find_packages(exclude=[]),
      package_data = {},
      install_requires=['numpy>=1.0.3',
                        ],
      # extras can be difficult to install through setuptools and/or
      # you might prefer to use the version available through your
      # packaging system
      extras_require={'remapping':  ['scipy',          # for remapping/interpolation
                                     ],
                      },
      zip_safe=True,
)
