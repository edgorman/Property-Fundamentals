from setuptools import setup
from setuptools import find_packages

setup(
    name='backend',
    version='1.0.0',
    description='Host the FastAPI backend for propertyfundamentals.',
    author='',
    author_email='',
    packages=find_packages('.'),
    install_requires=[
        "propertyfundamentals",
        "gunicorn",
        "uvicorn",
        "fastapi"
    ]
)
