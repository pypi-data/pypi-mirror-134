from setuptools import *
from os import path

this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, "README.md"), encoding = "utf-8") as f:
    long_description = f.read()

setup(
    name = "openseafloor",
    version = "1.1",
    author = "Sem Moolenschot",
    author_email = "sem@moolenschot.nl",
    description = "Scrape floor prices from OpenSea",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = find_packages(),
    include_package_data = True,
    py_modules=["osfloor"],
    license = "MIT",
    classifiers = [
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
    	"cloudscraper",
        "json"
    ],
)
