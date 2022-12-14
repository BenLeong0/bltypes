import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bltypes",
    version="0.0.1",
    author="Ben Leong",
    author_email="benleong0@gmail.com",
    description="Shared types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benleong0/bltypes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
