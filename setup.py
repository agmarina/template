from setuptools import find_packages, setup

setup(
    name="template",
    packages=find_packages(where=["src"]),
    version="0.1.0",
    description="template",
    author="minsait",
    license="",
    package_dir={"": "src"},
)
