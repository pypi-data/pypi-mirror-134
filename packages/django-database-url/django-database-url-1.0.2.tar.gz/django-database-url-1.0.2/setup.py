# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.rst') as readme_rst:
    readme = readme_rst.read()

setup(
    name="django-database-url",
    version="1.0.2",
    url="https://github.com/tend/dj-database-url",
    license="BSD",
    author="Rati Matchavariani",
    author_email="rati.matchavariani@hellotend.com",
    description="Use Database URLs in your Django Application.",
    long_description=readme,
    py_modules=["dj_database_url"],
    install_requires=["Django>3.2"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
)
