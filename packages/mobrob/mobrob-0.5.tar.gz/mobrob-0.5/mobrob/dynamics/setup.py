#from distutils.core import setup
from setuptools import find_packages, setup

setup(
    name='dynamics',
    version='0.3dev',
    author='68-6f-6c-67-69',
    author_email='68.6f.6c.67.69@gmail.com',
    url='https://github.com/68-6f-6c-67-69/mobrob',
    packages = find_packages(),
    py_modules=['dynamics.digital_filter'], 
    license='',
    long_description=open('README.txt').read(),
)





