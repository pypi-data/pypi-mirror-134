import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="invalid",
    version="0.0.1",
    license="MIT",
    author="Ryan Moore",
    description="Simple command line input validator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryan-mooore/invalid",
    download_url="https://github.com/ryan-mooore/invalid/archive/refs/tags/v0.0.1.tar.gz",
    keywords=["cli", "input", "validation"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pick", "python-dateutil"],
    include_package_data=True,
)
