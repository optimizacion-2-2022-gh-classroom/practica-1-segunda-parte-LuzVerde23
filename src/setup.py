#see: https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html
from setuptools import setup, find_packages

setup(name="MaxFlowAeiu",
      version="0.1.1",
      description=u"Execution of the Fork Fulkerson method to find the maximum flow of a network",
      long_description=open("README.md", "r", encoding="utf-8").read(),
      url="https://optimizacion-2-2022-gh-classroom.github.io/practica-1-segunda-parte-LuzVerde23/index.html",
      author="Team-2",
      author_email="",
      classifiers = ['License :: OSI Approved :: MIT License',
                     'Programming Language :: Python :: 3',
                     'Intended Audience :: Education'
                     ],
      license="MIT",
      keywords='max flow',
      packages=find_packages(),
      #install_requires = ["collections-extended"]
      )
