import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="aliver",
    version="1.0.4",
    description="A module made for repl.it users",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/alshahriah/aliver",
    author="Al-Shahriah",
    author_email="alshahriah2007@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["aliver"],
    include_package_data=True,
    install_requires=["flask"],
    entry_points={
        "console_scripts": [
            "aliver=aliver.__main__:main",
        ]
    },
)