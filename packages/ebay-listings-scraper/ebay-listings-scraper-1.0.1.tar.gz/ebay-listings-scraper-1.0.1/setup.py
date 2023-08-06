import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
VERSION = '1.0.1'
PACKAGE_NAME = 'ebay-listings-scraper'
AUTHOR = 'DataKund'
AUTHOR_EMAIL = 'datakund@gmail.com'
KEYWORDS='ebay e-bay python bot_studio automation search scraper scrape listing title rating condition price shipping listing_link'
LICENSE = 'Apache License 2.0'
DESCRIPTION = 'A python library to scrape ebay, listing title, rating, condition, price, shipping, listing link'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'requests','bot-studio'
]
setup(name=PACKAGE_NAME,
      version=VERSION,
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