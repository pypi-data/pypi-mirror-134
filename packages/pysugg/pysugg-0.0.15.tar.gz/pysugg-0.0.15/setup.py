import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysugg",
    version="0.0.15",
    author="bitekong",
    author_email="btk@qq.com",
    description="A package that can give you some code suggestions when exceptions occurred.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bitekong/pysugg",
    project_urls={
        "Bug Tracker": "https://github.com/bitekong/pysugg/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)