#see: https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html
from setuptools import setup, find_packages

setup(name="Maxflow",
      version="0.1",
      description=u"Optimaztion 2022 team 2 Package practica 1, segunda parte ",
      url="https://optimizacion-2-2022-gh-classroom.github.io/practica-1-segunda-parte-LuzVerde23/",
      author="Team-2",
      author_email="",
      license="MIT",
      packages=find_packages(),
      install_requires = [
                          "collections"
                          ],
      )