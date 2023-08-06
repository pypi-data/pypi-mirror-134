from setuptools import setup

setup(
    name="pyprodir",
    version="2.0.0",
    description="prepend directory of importer's pyproject.toml to sys.path",
    long_description=open("README.md", encoding="utf_8").read(),
    long_description_content_type="text/markdown",
    author="churunmin",
    author_email="churunmin@outlook.com",
    url="https://github.com/pypa/sampleproject",
    license="MIT",
    py_modules=["pyprodir"],
    install_requires=[
    ],
    python_requires=">=3.6",
)
