import setuptools

VERSION_STR = "0.0.3"

with open("README.md", "r") as fh:
    long_description = fh.read()

# with open('requirements.txt') as f:
#     install_requires = f.read().splitlines()

setuptools.setup(
     name='harmonicseries',
     version=VERSION_STR,
     author="Anjana Wijekoon",
     author_email="a.wijekoon1@rgu.ac.uk",
     description="Python Package to calculate harmonic numbers",
     long_description=long_description,
     long_description_content_type="text/markdown",
     # url="https://github.com/RGU-Computing/discern-xai",
     packages=setuptools.find_packages(exclude=("tests",)),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent"
     ],
     keywords='mathematic calculations',
     # install_requires=install_requires,
 )
