from pathlib import Path
from setuptools import setup

current_dir = Path(__file__).parent.resolve()

with open(current_dir / 'README.md', encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name="kivi",
    version = "0.0.1",
    packages = ["kivi"],
    description = "It calculates the creation time and size of objects.",
    author = "furkanonder",
    author_email = 'furkanonder@protonmail.com',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    keywords = ["class", "time", "size", "objects"],
    license = "MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],
)