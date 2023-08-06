# -*- coding: utf-8 -*-


import setuptools
from pathlib import Path
#from setuptools import setup
setuptools.setup(name='gym_contin',
      version='1.5.0',
      description="A OpenAI Gym Env for continuous actions",
      long_description=Path("README.md").read_text(),
      long_description_content_type="text/markdown",
                 author="Claudia Viaro",
                 license="MIT",
      packages=setuptools.find_packages(include="gym_contin*"),
      install_requires=['gym']  # And any other dependencies needed
)
