import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wts-nerdler",
    version="1.1.0",
    author="Nerdler",
    author_email="pip@nerdler.tech",
    description="Windows Task Scheduler Framework by Nerdler.Tech",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nerdlertech/wts-nerdler",
    project_urls={
        "Bug Tracker": "https://github.com/nerdlertech/wts-nerdler/issues",
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