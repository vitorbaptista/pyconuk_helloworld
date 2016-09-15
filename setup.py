import os
import codecs
from setuptools import setup, find_packages


def read(*parts):
    '''
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    '''
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(BASE_PATH, *parts), 'rb', 'utf-8') as f:
        return f.read()

setup(
    name='pyconuk_helloworld',
    version='0.0.1',
    description='A hello world package',
    long_description=read('README.rst'),
    url='https://github.com/vitorbaptista/helloworld',
    author='Vitor Baptista',
    author_email='vitor@vitorbaptista.com',
    license='MIT',
    packages=find_packages(exclude='tests'),
)
