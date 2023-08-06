import os
from setuptools import setup, find_packages

requirements = f'{os.path.dirname(os.path.realpath(__file__))}/requirements.txt'

install_requires = ['']
if os.path.isfile(requirements):
    with open(requirements) as f:
        install_requires = f.read().splitlines()

setup(
    name='gcs_basic',
    version='2.0.0',
    url='',
    license='',
    author='antonio',
    author_email='antonio258p@gmail.com',
    description='Gcs simple functions',
    install_requires=install_requires,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
