from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = 'cHaversine',
    packages = ['cHaversine'],
    version = '0.1.2',
    description = 'Fast haversine calculation',
    author = 'Eric Jiang',
    author_email = 'eric@doublemap.com',
    requires = 'cython',
    url = 'https://github.com/doublemap/cHaversine',
    keywords = ['math', 'geo', 'cython'],
    classifiers = ['License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'],
    ext_modules = cythonize("cHaversine/cHaversine.pyx")
)
