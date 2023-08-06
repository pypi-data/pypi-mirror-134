"""Setup script for the python-act library module"""

from os import path

from setuptools import setup

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), "rb") as f:
    long_description = f.read().decode("utf-8")

setup(
    name="aep-web",
    version="0.0.5",
    author="mnemonic AS",
    zip_safe=True,
    author_email="opensource@mnemonic.no",
    description="Adversary Emulation Planner (AEP) Web Frontend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="aep,attack,mnemonic,web",
    entry_points={
        "console_scripts": [
            "aep-web= aep.web.server:main",
        ]
    },
    # https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages
    namespace_packages=["aep"],
    packages=["aep.web"],
    package_data={"aep.web": ["static/*", "templates/*"]},
    url="https://github.com/mnemonic-no/aep-web",
    install_requires=[
        "python-multipart",
        "caep",
        "fastapi",
        "uvicorn",
        "aiofiles",
        "jinja2",
        "aep>=0.1.4",
    ],
    python_requires=">=3.6, <4",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: ISC License (ISCL)",
    ],
)
