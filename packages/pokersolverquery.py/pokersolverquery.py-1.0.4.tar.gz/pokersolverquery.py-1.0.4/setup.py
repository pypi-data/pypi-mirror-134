import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="pokersolverquery.py",
    version="1.0.4",
    description="A Poker BaseSolver Query package for interacting with UPI engines such as PioSOLVER and jesolver",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mitchr1598/pokersolverquery",
    author="mitchr1598",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    packages=["pokersolverquery"],
    python_requires=">=3.9.0",
    install_requires=[
        'texasholdem1598',
        'numpy',
    ],
)
