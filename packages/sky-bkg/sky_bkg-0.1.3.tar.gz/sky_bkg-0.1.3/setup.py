from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='sky_bkg',
    version='0.1.3',
    description='sky background',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='linlin',
    author_email='linlin@shao.ac.cn',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"sky_bkg": ["refs/*.dat"]},
    python_requires='>=3',
)
