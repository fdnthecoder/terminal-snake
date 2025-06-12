#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

# Read the README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Read version from __init__.py
def get_version():
    with open(os.path.join(this_directory, 'terminal_snake', '__init__.py')) as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('"')[1]
    return "1.0.0"

version = get_version()

setup(
    name="terminal-snake",
    version=version,
    author="Amadou Diallo",
    author_email="aodiallo324@gmail.com",
    description="🐍 A fun snake game for your terminal - perfect for quick breaks!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/terminal-snake",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment :: Arcade",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Environment :: Console :: Curses",
    ],
    python_requires=">=3.6",
    keywords="snake game terminal console curses cli fun break arcade",
    entry_points={
        "console_scripts": [
            "snake=terminal_snake.cli:main",
            "terminal-snake=terminal_snake.cli:main",
        ],
    },
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black",
            "flake8",
            "twine",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/fdnthecoder/terminal-snake/issues",
        "Source": "https://github.com/fdnthecoder/terminal-snake",
        "Documentation": "https://github.com/fdnthecoder/terminal-snake/blob/main/README.md",
    },
)

