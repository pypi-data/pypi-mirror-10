from setuptools import setup, find_packages
from codecs import open
from os import path


# Get the long description from the relevant file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = "pannenkoek",
      long_description=long_description,
    version = "0.1.5-dev0",
    packages = find_packages(),
    scripts = ['scripts/pannenkoek.py'],

    # Project uses reStructuredText, so ensure that the
    # docutils get installed or upgraded on the target
    # machine
    install_requires = ['qiime', 'rpy2', 'numpy', 'matplotlib', 'argparse', 'pandas', 'biopython'],

    package_data = {
        # If any package contains *.txt or *.rst files,
        # include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the
        # 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "Thomas W. Battaglia",
    author_email = "tb1280@nyu.com",
    description = "A wrapper for Qiime and LEfSe analysis. Split an OTU table by time and make certain comparisons with ease.",
    license = "MIT",
    keywords = "Biology Microbiome LEFSE QIIME Formatting Diversity Python Bioinformatics",

    # project home page, if any :
    url = "https://bitbucket.org/twbattaglia/pannenkoek",

    # could also include long_description, download_url,
    # classifiers, etc.
)
