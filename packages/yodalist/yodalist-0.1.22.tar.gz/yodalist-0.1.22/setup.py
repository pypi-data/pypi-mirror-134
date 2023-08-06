import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yodalist",
    version="0.1.22",
    author="lynn pepin",
    author_email="1914373-lynnpepin@users.noreply.gitlab.com",
    description="For lists, yoda-indexing this package provides.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/lynnpepin/yodalist",
    project_urls={
        "Bug Tracker": "https://gitlab.com/lynnpepin/yodalist/-/issues",
    },
    classifiers=[
        "Intended Audience :: Other Audience",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)