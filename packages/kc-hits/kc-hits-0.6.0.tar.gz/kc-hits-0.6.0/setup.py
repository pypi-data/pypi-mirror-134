from setuptools import setup, find_packages
import pathlib
from glob import glob

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="kc-hits",
    version="0.6.0",
    description="A package to aid in the formal characterization and classification of chemical carcinogens",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/i1650/kc-hits.git",
    author="Brad Reisfeld",
    author_email="reisfeldb@iarc.fr",
    packages=find_packages(where="src"),
    python_requires=">=3.8, <4",
    install_requires=[
        "matplotlib",
        "numpy",
        "pandas",
        "openpyxl",
        "pyinstaller",
        "pysimplegui",
    ],
    data_files=[
        ("db", glob("src/db/*.pkl")),
        ("data", glob("src/data/*.csv")),
        ("resources", glob("src/resources/*.png")),
        ("docs", ["src/docs/instructions.txt"]),
        ("templates", glob("src/templates/*.xlsx")),
    ],
    entry_points={"console_scripts": ["kc_hits=kc_hits:main",],},
    project_urls={"Source": "https://gitlab.com/i1650/kc-hits.git"},
    license_files=("LICENSE",),
)

