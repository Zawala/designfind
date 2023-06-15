from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in designfind/__init__.py
from designfind import __version__ as version

setup(
	name="designfind",
	version=version,
	description="Created to link designers with customers",
	author="Zawala",
	author_email="kelvinzawala@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
