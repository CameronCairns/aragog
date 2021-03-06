import setuptools

VERSION = "20.6.0"
TITLE = "aragog"
DESCRIPTION = "A better python scraper."
URL = "https://www.cameroncairns.com/"
DOC = DESCRIPTION + " <" + URL + ">"
AUTHOR = "Cameron Cairns"
AUTHOR_EMAIL = "cameron@cameroncairns.com"
LICENSE = "Apache License 2.0"
COPYRIGHT = "Copyright (c) 2020 Cameron Cairns"
NAME = "aragog"


INSTALL_REQUIRES = []
PYTHON_REQUIRES = ">=3.6"

KEYWORDS = ["webscrape", "webcrawl", "crawl", "scrape"]
CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]


def get_description():
    with open("README.rst", "r") as readme:
        long_description = readme.read()
    return long_description


if __name__ == "__main__":
    setuptools.setup(
        zip_safe=False,
        long_description=get_description(),
        long_description_content_type="text/x-rst",
        packages=setuptools.find_packages(where="src"),
        package_dir={"": "src"},
        name=NAME,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=AUTHOR,
        maintainer_email=AUTHOR_EMAIL,
        keywords=KEYWORDS,
        python_requires=PYTHON_REQUIRES,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
    )
