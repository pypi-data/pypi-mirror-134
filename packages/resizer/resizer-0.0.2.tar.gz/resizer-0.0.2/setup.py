from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'My Resizer Python package'
LONG_DESCRIPTION = 'Resizes all the files in a given directory'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="resizer",
        version=VERSION,
        author="Azeez Idris",
        author_email="abdulazeezidris28@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),

        keywords=['python', 'My Resizer package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
        ]
)
