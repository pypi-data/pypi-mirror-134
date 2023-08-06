from pathlib import Path
from setuptools import find_packages, setup

NAME = 'admission-prediction-model'
DESCRIPTION = "A sample model to predict your chances of admission in graduate universities"
URL = ""
AUTHOR = "Mihir Gupte"
EMAIL = "mihir.a.gupte@gmail.com"
REQUIRES_PYTHON = ">=3.8.0"

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

about = {}
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR
PACKAGE_DIR = ROOT_DIR / 'prediction_model'

with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version

def list_reqs(fname="requirements.txt"):
    with open(REQUIREMENTS_DIR / fname) as fd:
        return fd.read().splitlines()

setup(
    name=NAME,
    version=about["__version__"],
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    email = EMAIL,
    packages=find_packages(exclude=("tests",)),
    package_data={"prediction_model": ["VERSION"]},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license="BSD-3",  
)