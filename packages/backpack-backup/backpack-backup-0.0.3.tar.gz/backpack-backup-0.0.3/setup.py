#!/usr/bin/python3
""" Setup module for the backpack backup project
"""
from setuptools import setup, find_packages

with open("README.md") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    requirements = fh.readlines()

setup(
    name="backpack-backup",
    version="0.0.3",
    description="A tool to sign, encrypt and, backup a file or directory using GPG.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab.com/unkwn1/backpack-backup",
    project_urls={
        "Issues": "https://gitlab.com/unkwn1/backpack-backup/-/issues",
        "Source": "https://gitlab.com/unkwn1/backpack-backup/-/tree/main",
    },
    author="unkwn1",
    author_email="unkwn1@tutanota.com",
    license="GPLv3",
    keywords="dorking, google dork, web parser, web scraping",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=requirements,
    packages=find_packages(),
    entry_points={"console_scripts": ["backpack=backpack.cli:main"]},
)
