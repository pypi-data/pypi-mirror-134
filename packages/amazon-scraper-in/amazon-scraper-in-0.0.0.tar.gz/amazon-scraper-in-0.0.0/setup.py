import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
PACKAGE_NAME = 'amazon-scraper-in'
AUTHOR = 'DataKund'
AUTHOR_EMAIL = 'datakund@gmail.com'
KEYWORDS='amazon title price link product python bot_studio automation search scraper scrape'
LICENSE = 'Apache License 2.0'
DESCRIPTION = 'A python library to scrape data on Amazon.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'requests','bot-studio'
]
setup(name=PACKAGE_NAME,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      keywords = KEYWORDS
      )