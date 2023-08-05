try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from Cython.Build import cythonize
import numpy

config = {
    'description': 'SimpleCNN',
    'author': 'Zhengxing Chen',
    'author_email': 'czxttkl@gmail.com',
    'install_requires': ['nose','numpy','scipy','cython'],
    'name':"SimpleCNN",
    'ext_modules':cythonize("simplecnn/pool.pyx"),
    'include_dirs':[numpy.get_include()],
    'version':'3.2',
    'packages': ['simplecnn'], 
    'package_data':{
    '': ['pool.pyx'],     # All files from folder A
    }
}

setup(**config)