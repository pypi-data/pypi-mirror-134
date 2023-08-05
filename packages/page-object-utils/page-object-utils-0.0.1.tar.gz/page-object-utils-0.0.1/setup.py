import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="page-object-utils",
    version="0.0.1",
    author="Matthew Bahloul",
    author_email="matthew.bahloul@gmail.com",
    description="Base classes and utilities for use with browser automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matthew-bahloul/browser-utils",
    project_urls={
        "Bug Tracker": "https://github.com/matthew-bahloul/browser-utils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)