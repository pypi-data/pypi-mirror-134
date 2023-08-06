from setuptools import setup, find_packages


setup(name='custom_exceptions', version='1.1', packages=find_packages(where='QueryException'), package_dir={"": "QueryException"})
