from setuptools import find_packages, setup

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="oc4idskit",
    version="0.0.2",
    author="Open Contracting Partnership",
    author_email="data@open-contracting.org",
    url="https://github.com/open-contracting/oc4idskit",
    description="A suite of command-line tools for working with OC4IDS data",
    license="BSD",
    packages=find_packages(exclude=["tests", "tests.*"]),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=[
        "jsonpointer",
        "ocdskit>=1",
        'ocdsmerge>=0.6',
    ],
    extras_require={
        "test": [
            "coveralls",
            "pytest",
            "pytest-cov",
            "pytest-vcr",
        ],
        "docs": [
            "furo",
            "sphinx",
            "sphinx-autobuild",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    entry_points={
        "console_scripts": [
            "oc4idskit = oc4idskit.cli.__main__:main",
        ],
    },
)
