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
    version='0.1.0',
    description='A hello world package',
    long_description=read('README.rst'),
    url='https://github.com/vitorbaptista/pyconuk_helloworld',
    author='Vitor Baptista',
    author_email='vitor@vitorbaptista.com',
    license='MIT',
    packages=find_packages(exclude='tests'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'helloworld=helloworld.cli:main'
        ],
    },
)
