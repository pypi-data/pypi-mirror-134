from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyCal2PDF",
    version="0.0.3.7",
    author="Oberron",
    author_email="one.annum@gmail.com",
    description="PDF calendar generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/1-annum/pyCal2PDF",
    project_urls={
        "Bug Tracker": "https://github.com/1-annum/pyCal2PDF/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["reportlab","lunardate","svglib","pyICSParser"]
    )