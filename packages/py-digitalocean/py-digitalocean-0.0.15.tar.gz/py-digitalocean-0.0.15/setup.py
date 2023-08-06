import setuptools

#
# XXX pull from a seperate file like usage
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-digitalocean",
    version="0.0.15",
    author="Alan Chester",
    author_email="amcheste@gmail.com",
    url="https://gitlab.com/camphotos/py-digitalocean",
    description="Digital Ocean Python Library",
    long_description="Coming Soon...",
    long_description_content_type="text/markdown",
    packages=['digitalocean'],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests']
)
