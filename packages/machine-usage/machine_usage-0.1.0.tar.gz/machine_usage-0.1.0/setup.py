from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="machine_usage",
    version="v0.1.0",
    author="Jan A. Stevens",
    author_email="stevens.jan.adriaan@gmail.com",
    description="Display the available resources on our local cluster.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marrink-lab/machine_usage",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'machine_usage = src.machine_usage.argparse:main'
        ]
    },
    python_requires=">=3.7",
    install_requires=[
        'click', 'textual',
        'distro'
    ],
)
