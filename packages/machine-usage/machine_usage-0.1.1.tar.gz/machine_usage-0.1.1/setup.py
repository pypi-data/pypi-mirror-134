import os
import os.path
from setuptools import setup, find_packages
import codecs

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# this comes form here https://packaging.python.org/guides/single-sourcing-package-version/
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="machine_usage",
    version=get_version("src/machine_usage/__init__.py"),
    author="Jan A. Stevens",
    author_email="stevens.jan.adriaan@gmail.com",
    description="Display the available resources on our local cluster.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marrink-lab/machine_usage",
    python_requires=">=3.7",
    install_requires=[
        'click', 'textual',
        'distro',
    ],
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'machine_usage = machine_usage.argparse:main',
        ],
    },
)
