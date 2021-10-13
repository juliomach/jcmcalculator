import setuptools

with open("README.md", "r") as rdm:
    description = rdm.read()

setuptools.setup(
    name="jcmcalculator",
    version="1.0.0",
    author="Julio Cesar Machado",
    author_email="juliomach@gmail.com",
    desc="My first calculator",
    description=description,
    description_content_type="text/markdown",
    url="https://github.com/juliomach/jcmcalculator",
    packages=setuptools.find_packages(),
    scripts=['bin/jcmcalculator'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
