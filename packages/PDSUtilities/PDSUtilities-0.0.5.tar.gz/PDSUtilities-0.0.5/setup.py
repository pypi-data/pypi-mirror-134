from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="PDSUtilities",
	version="0.0.5",
	description="Utilities for data science in python",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/DrJohnWagner/PDSUtilities",
	author="Dr. John Wagner",
	author_email="Dr.John.Wagner@gmail.com",
	license="Apache-2.0",
	packages=[
		"PDSUtilities",
		"PDSUtilities.xgboost",
	],
	install_requires=[
		"numpy",
		"xgboost",
		"plotly",
		"igraph",
	],
	tests_require=[
		"pytest",
	],
	zip_safe=False)

# package_dir={"": "src"},
# packages=setuptools.find_packages(where="src"),