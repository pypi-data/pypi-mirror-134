from setuptools import setup, find_packages

setup(
    name="dsa_utilities",
    version="0.6",
    description="Utilities functions for DSA",
    author="Nischal Lal Shrestha",
    author_email="aakrist666@gmail.com",
    url="https://github.com/theonlynischal/dsa_utils_package",
    packages=find_packages(
        exclude=("tests*",)
    ),
)