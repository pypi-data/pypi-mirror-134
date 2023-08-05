import setuptools

with open('README.md') as fp:
    long_description = fp.read()

setuptools.setup(
    name="emily-test-pip",
    version="0.0.1",
    author="Anders Brams",
    author_email="abra@ambolt.io",
    description="Standard utility and boilerplate for Emily backend services.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://amboltio@dev.azure.com/amboltio/emily/_git/emily-shared",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)