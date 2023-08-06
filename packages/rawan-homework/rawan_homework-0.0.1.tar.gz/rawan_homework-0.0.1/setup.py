from setuptools import setup, find_packages
import os


VERSION = '0.0.1'
DESCRIPTION = 'Homework class Rawan'

# Setting up
setup(
    name="rawan_homework",
    version=VERSION,
    author="Rawan Al-Ghamdi",
    author_email="<rawan111188@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 'list', 'numbers', 'math'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)