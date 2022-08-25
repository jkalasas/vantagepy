"""
PyVantage
---------

PyVantage is a API client for Alpha Vantage
"""

from setuptools import setup

setup(
    name="PyVantage",
    version="0.0.1",
    url="https://github.com/jkalasas/pyvantage",
    license="MIT",
    author="John Kyle Alas-as",
    author_email="alasasjohnkyle@gmail.com",
    description="API client for Alpha Vantage",
    long_description=__doc__,
    keywords=[
        "api",
        "alphavantage",
        "client",
    ],
    packages=[
        "pyvantage",
    ],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developer",
        "License :: OSI Approved :: MIT Liecense",
        "Programming Language :: Python :: 3",
    ],
)
