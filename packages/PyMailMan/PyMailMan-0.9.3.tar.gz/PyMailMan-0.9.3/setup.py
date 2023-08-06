from setuptools import setup, find_packages

setup(
    name = 'PyMailMan',
    version = '0.9.3',
    keywords = ('mail', 'smtp'),
    description = 'A simple tool for sending mail by Python',
    license = 'MIT License',
    install_requires = [],
    long_description = file('README.rst').read(),
    author = 'kongkongyzt',
    url = 'https://github.com/kongkongyzt/PyMailMan',
    author_email = 'kongkongyzt@gmail.com',
    packages = find_packages(),
    platforms = 'any',
)
