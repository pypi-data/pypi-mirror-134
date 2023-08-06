import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythia-uq",
    version="2.0.0",
    author="Nando Farchmin",
    author_email="nando.farchmin@ptb.de",
    description=("Package for solving inverse problems and quantifying their "
                 + "uncertainties via general polynomial chaos."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab1.ptb.de/pythia/pythia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy>=1.19.0",
        "scipy>=1.5.0",
        "psutil>=5.0",
    ],
)
