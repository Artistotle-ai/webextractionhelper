from setuptools import setup, find_packages

with open("README.MD", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="webextractionhelper",
    version="0.1.0",
    author="Jens Verneuer",
    author_email="Jens@Aristotle.ventures",
    description="A comprehensive web scraping helper package with XPath selectors, regex patterns, and CSS selectors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Artistotle-ai/webextractionhelper",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Creative Commons License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    python_requires=">=3.7",
    install_requires=[
        "lxml>=4.6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    keywords="web scraping, xpath, css selectors, regex, google search, serp",
    project_urls={
        "Bug Reports": "https://github.com/Artistotle-ai/webextractionhelper/issues",
        "Source": "https://github.com/Artistotle-ai/webextractionhelper",
        "Documentation": "https://github.com/Artistotle-ai/webextractionhelper#readme",
    },
)
