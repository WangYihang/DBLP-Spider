import setuptools
import dblp_spider

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DBLP-Spider",
    version=dblp_spider.__version__,
    author="Wang Yihang",
    author_email="wangyihanger@gmail.com",
    description="A spider tool for downloading the DBLP search results into local BibTeX files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WangYihang/Platypus-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
    keywords="academic, research, spider, dblp, ccf",
    install_requires=["termcolor", "requests", "bs4"],
    entry_points={
        "console_scripts": [
            "dblp-spider=dblp_spider:main",
        ],
    },
)
