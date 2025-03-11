from setuptools import setup, find_packages

setup(
    name='K-Chain',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask==2.0.1',
        'pytest==6.2.4',
    ],
)
