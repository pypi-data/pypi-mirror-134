import os
from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='gcs_basic',
    version='2.0.1',
    url='',
    license='',
    author='antonio',
    author_email='antonio258p@gmail.com',
    description='Gcs simple functions',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
