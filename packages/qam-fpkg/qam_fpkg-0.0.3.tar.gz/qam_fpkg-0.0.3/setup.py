import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qam_fpkg",
    version="0.0.3",
    long_description=long_description,
    packages=setuptools.find_packages(exclude=["test", "data"]),

)
