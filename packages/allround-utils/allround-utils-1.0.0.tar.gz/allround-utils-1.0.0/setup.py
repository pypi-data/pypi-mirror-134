from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'allround utils'
LONG_DESCRIPTION = 'master package for utils for allround ecosystem'

# Setting up
setup(
        name="allround-utils",
        version=VERSION,
        author="allround",
        author_email="biz@allround.club",
        url="https://allroundclub.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests'],
        keywords=['python', 'utils', 'requests', 'allround'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
