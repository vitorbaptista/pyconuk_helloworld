from setuptools import setup, find_packages

setup(
    name='pyconuk_helloworld',
    version='0.0.1',
    description='A hello world package',
    url='https://github.com/vitorbaptista/helloworld',
    author='Vitor Baptista',
    author_email='vitor@vitorbaptista.com',
    license='MIT',
    packages=find_packages(exclude='tests'),
)
