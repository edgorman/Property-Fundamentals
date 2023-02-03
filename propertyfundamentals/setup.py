from setuptools import setup
from setuptools import find_packages

setup(
    name='propertyfundamentals',
    version='1.0.0',
    description='Extract, transform and load UK housing data.',
    author='',
    author_email='',
    packages=find_packages('.'),
    install_requires=[
        "autopep8",
        "coverage",
        "regex",
        "requests",
        "pandas",
        "flake8",
        "pytest",
        "pytest-cov",
    ]
)
