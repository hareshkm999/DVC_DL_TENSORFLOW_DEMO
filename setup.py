   
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="hareshkm999",
    description="A small package for dvc DL pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hareshkm999/DVC_DL_TENSORFLOW_DEMO",
    author_email="hareshkm999@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "dvc",
        "tensorflow",
        "pandas",
        "numpy",
        "matplotlib",
        "tqdm",
        "pyYAML",
        "boto3"
       ]
)