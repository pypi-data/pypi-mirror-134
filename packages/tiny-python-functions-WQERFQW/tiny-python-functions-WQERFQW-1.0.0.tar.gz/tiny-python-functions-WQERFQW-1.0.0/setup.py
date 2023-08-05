import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file

# This call to setup() does all the work
setup(
    name="tiny-python-functions-WQERFQW",
    version="1.0.0",
    description="This is an exercise to publish smth on pipy",
    long_description="no long description",
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="myself",
    author_email="info@myself.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["adder"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "realpython=adder.__main__:main",
        ]
    },
)