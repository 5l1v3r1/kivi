# python
from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="kivi",
    version = "0.0.1",
    packages = ["kivi"],
    description = "It calculates the creation time and size of objects.",
    author = "furkanonder",
    author_email = "furkantahaonder@gmail.com",
    url = "https://www.github.com/furkanonder/kivi",
    python_requires='>=3',
    py_modules=[],
    long_description=read('README.md'),
    include_package_data = True,
    install_requires = [],
    keywords = ["class", "time", "size", "objects"],
    license = "MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],
)

