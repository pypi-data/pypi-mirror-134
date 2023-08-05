"""
https://packaging.python.org/en/latest/tutorials/packaging-projects/
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latestnews-kemendikbud",
    version="0.0.1",
    author="Irfan Basyar",
    author_email="irfanbasyar.ib@gmail.com",
    description="this package will get the latest news from Indonesian Ministry of Education and Culture (Kemdikbud)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dikopini/latest-kemendikbud-news",
    project_urls={
        "Website": "https://dicopynee.com",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    #package_dir={"": "src"},
    #packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)