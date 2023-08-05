import setuptools
from pathlib import Path

setuptools.setup(
    name="moshpdfggkiller",
    version=1.1,
    description= Path("/Users/tanzimbinsaleh/Desktop/moshpdf/README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])
)