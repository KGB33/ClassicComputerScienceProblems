import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="CCSP",
    version="0.1",
    author="Kelton Bassingthwaite",
    author_email="github@kgb33.dev",
    description="Code from 'Classic Computer Science Problems in Python' by David Kopec",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3.8",],
)
