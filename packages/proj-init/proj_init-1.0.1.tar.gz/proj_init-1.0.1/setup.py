from pathlib import Path

from setuptools import find_packages, setup

# The directory containing this file
ROOT_DIR = Path(__file__).parent

with open(ROOT_DIR / "README.md", "r") as readme_file:
    long_description = readme_file.read()

with open(ROOT_DIR / "requirements.txt", "r") as requirements_file:
    all_reqs = requirements_file.readlines()


setup(
    name="proj_init",
    description="Automate your workflow with proj_init command.",
    version="1.0.1",
    packages=find_packages(),
    install_requires=all_reqs,
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["proj_init=proj_init.create:proj_init"]
    },
    author="Thales Nunes",
    keyword="git, github, project, automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/thalesnunes/proj_init",
    author_email="thalesaknunes22@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
