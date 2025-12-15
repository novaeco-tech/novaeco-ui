import os
from setuptools import setup, find_packages

# Read version from file
with open("VERSION", "r", encoding="utf-8") as f:
    version = f.read().strip()

setup(
    name="novaeco-ui",
    version=version,  # <--- Dynamic
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=3.0.0",
    ],
)