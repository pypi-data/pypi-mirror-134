from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.4'
DESCRIPTION = 'Log Creator package'

# Setting up
setup(
    name="log_creator",
    version=VERSION,
    author="lUckYtHRteeN13 (Nethan Quinn Jael) ",
    author_email="<nethanquinnjael13@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'log', 'logs', 'log creator'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)