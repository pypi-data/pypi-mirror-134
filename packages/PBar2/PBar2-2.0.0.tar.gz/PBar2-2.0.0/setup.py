import setuptools
try:
	import src.pbar
except Exception:
	prj_version = "dev"


src.pbar.bar.recover_stdout()


with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="PBar2",
	version=src.pbar.__version__,
	author="David Losantos (DarviL82)",
	author_email="davidlosantos89@gmail.com",
	description="Display customizable progress bars on the terminal easily.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://darvil82.github.io/PBar",
	project_urls={
		"Tracker": "https://github.com/DarviL82/PBar/issues",
		"Documentation": "https://github.com/DarviL82/PBar/wiki"
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	package_dir={"": "src"},
	packages=setuptools.find_packages(where="src"),
	python_requires=">=3.9",
)
