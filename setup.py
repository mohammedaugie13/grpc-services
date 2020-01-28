from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Template Python",
    version="0.0.1",
    description="Bitwyre Python Repo Template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bitwyre/template-python",
    author="Bitwyre Technologies LLC",
    author_email="dev@bitwyre.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU GPLv3 License",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="financial exchange cryptocurrency",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    python_requires=">=3.7.*, <4",
    install_requires=["matplotlib", "numpy", "grpcio", "grpcio-tools"],  # Optional
    extras_require={"dev": ["check-manifest", "pycodestyle", "mypy", "pre-commit"], "test": ["coverage", "pytest"]},
    entry_points={"console_scripts": ["template_python=template_python:cli"]},
    project_urls={
        "Bug Reports": "https://github.com/bitwyre/template-python/issues",
        "Funding": "https://bitwyre.com",
        "Say Thanks!": "http://bitwyre.gives",
        "Source": "https://github.com/bitwyre/template-python",
    },
)
