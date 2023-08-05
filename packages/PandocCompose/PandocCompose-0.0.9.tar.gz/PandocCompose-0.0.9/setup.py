from setuptools import setup

with open("requirements.txt") as rqrmts:
    requirements = [line for line in rqrmts.readlines() if not line.strip().startswith("#") and len(line.strip()) > 0]

setup(install_requires=requirements)
