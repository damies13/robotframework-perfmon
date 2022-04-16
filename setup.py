import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="robotframework-perfmon",
	version="0.1",
	author="damies13",
	author_email="damies13+robotframeworkperfmon@gmail.com",
	description="robotframework-perfmon",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/damies13/robotframework-perfmon",
	packages=setuptools.find_packages(exclude=["build/*"]),
	install_requires=['pyperfmon'],
	classifiers=[
		"Development Status :: 4 - Beta",
		"Topic :: System :: Monitoring",
		"Programming Language :: Python :: 3.6",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: Microsoft :: Windows ",
	],
	python_requires='>=3.6',
	project_urls={
		'Getting Help': 'https://github.com/damies13/robotframework-perfmon',
		'Source': 'https://github.com/damies13/robotframework-perfmon',
	},
)
