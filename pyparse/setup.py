from setuptools import setup, find_packages

setup(
    name='PyParse',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pyparse=pyparse.cli:main',
        ],
    },
    author='Abdul Rafey',
    author_email='abdulrafey38@gmail.com',
    description='A simple utility for converting CSV to JSON and vice versa',
    keywords='CSV JSON conversion',
    url='http://github.com/abdulrafey38/pyparse'
)
