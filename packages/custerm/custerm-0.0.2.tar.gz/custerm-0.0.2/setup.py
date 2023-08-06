import os
from setuptools import setup
import runpy

def read(fname):
    f = open(os.path.join(os.path.dirname(__file__), fname))
    r = f.read()
    f.close()
    return r

setup(
    name="custerm",
    version=runpy.run_path("./custerm/__version__.py")["__version__"],
    packages=["custerm"],
    license="MIT",
    description="CusTERM is a Python library for making your own bootleg command line!",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author="obfuscatedgenerated",
    author_email="pip@obfuscatedgenerated.ml",
    url="https://github.com/obfuscatedgenerated/CusTERM",
    repo_url="https://github.com/obfuscatedgenerated/CusTERM",
    keywords=["terminal", "tkinter", "ui"],
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
