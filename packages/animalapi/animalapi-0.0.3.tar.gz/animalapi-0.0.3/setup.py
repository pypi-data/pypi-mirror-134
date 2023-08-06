from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.3"
DESCRIPTION = "This is the package for api scapper that provides animal images and their facts."
LONG_DESCRIPTION = ""

setup(
    name="animalapi",
    version=VERSION,
    author="DARKPOISON",
    author_email="dashutosh06122004@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages= ["animalapi"],
    install_requires=["requests"],
    keywords=[],
    download_url = "https://github.com/DARKPOISON-yt/animalapi/archive/refs/tags/0.0.3.tar.gz",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
