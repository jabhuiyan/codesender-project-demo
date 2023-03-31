"""
A setuptools based setup file for the codeserver project.
implemented by: jabhuiyan
"""
from setuptools import setup, find_packages

setup(#metadata
    name='codeserver',
    version='0.3.0',
    description='A server that can be used to practice python codes.',
    
    #packages needed
    packages=find_packages(include=['main', 'main.*']), #include everything in main file
    
    #check packages required for install
    install_requires = ['pylint', 'flask>=1.0.2', 'numpy>=1.14.5'], #PyPI packages
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
