from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dblpct",
    version="20220114.2",
    description="double the % to two.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mollinaca/dblpct",
    author="mollinaca",
    author_email="mail@mollinaca.dev",
    license="CC0",
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      dblpct = dblpct.dblpct:main
    """,
)
