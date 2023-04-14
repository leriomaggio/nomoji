import os
from setuptools import find_packages, setup

CURRENT_FOLDER = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURRENT_FOLDER, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="nomoji",
    author="Valerio Maggio",
    version="0.0.5",
    author_email="vmaggio@anaconda.com",
    description="Silly Python Package to print digits using emojis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leriomaggio/emoji-numbers/",
    packages=find_packages(exclude=[]),
    include_package_data=True,
)
