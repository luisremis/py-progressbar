import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="progressbar",
    version="0.0.1",
    author="Luis Remis",
    author_email="luis@remis.io",
    description="Minimalistic Progress Bar",
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luisremis/py-progressbar",
    license="Apache",
    packages=setuptools.find_packages(),
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
