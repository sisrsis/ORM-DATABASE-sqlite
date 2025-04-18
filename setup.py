from setuptools import setup ,find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
   name='orm_database_sqlite',
   version='0.0.2',
   description='This module is written to launch your programs with any database you want in the shortest time ',
   license="MIT",
   author='SISRSIS',
   author_email='virussisrsis@gmail.com',
   url="https://github.com/sisrsis/orm-database",
   packages=find_packages(),  #same as name
   install_requires=[], #external packages as dependencies
   long_description=long_description,
   long_description_content_type='text/markdown'
)
