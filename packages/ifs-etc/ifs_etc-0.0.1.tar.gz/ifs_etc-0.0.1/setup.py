from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='ifs_etc',
    version='0.0.1',
    description='exposure time calculator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='linlin',
    author_email='linlin@shao.ac.cn',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"ifs_etc": ["refdata/sed/*.fits",
                              "refdata/normalization/filters/*.par",
                              "refdata/csst/background/*.dat",
                              "refdata/csst/ifs/*.dat",
                              "refdata/csst/telescope/*",
                              "refdata/source/*"]},
    exclude_package_data={"": ["README.md"]},
    python_requires='>=3',
)

