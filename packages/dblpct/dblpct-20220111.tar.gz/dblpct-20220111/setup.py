from setuptools import setup, find_packages

setup(
    name="dblpct",
    version="20220111",
    description="doble the % to two.",
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
