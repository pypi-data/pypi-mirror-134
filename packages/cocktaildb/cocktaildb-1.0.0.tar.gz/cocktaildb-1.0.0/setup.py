import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cocktaildb",
    version="1.0.0",
    author="XXIV",
    description="TheCocktailDB API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thexxiv/cocktaildb-py",
    project_urls={
        "Bug Tracker": "https://github.com/thexxiv/cocktaildb-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)