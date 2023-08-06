from setuptools import setup, find_packages

DESCRIPTION = 'Get squad details of cricketseries'

setup(
        name="Cricket_Squad_Scraper", 
        version='0.1',
        author="Bhaskar Chauhan",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests','bs4'],
      )