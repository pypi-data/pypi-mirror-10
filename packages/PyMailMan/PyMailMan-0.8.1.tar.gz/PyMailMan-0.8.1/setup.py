from setuptools import setup, find_packages

setup(
    name = 'PyMailMan',
    version = '0.8.1',
    keywords = ('mail'),
    description = 'A simple tool for sending mail by Python',
    license = 'MIT License',
    install_requires = [],
    long_description = file('README.rst').read(),
    author = 'kongkongyzt',
    author_email = 'kongkongyzt@gmail.com',
    
    packages = find_packages(),
    platforms = 'any',
)
