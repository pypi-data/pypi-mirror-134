# CERES
**C**elestial **E**stimation for **R**esearch, **E**xploration, and **S**cience

![Tests](https://github.com/ceres-navigation/ceres/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/ceres-navigation/ceres/branch/main/graph/badge.svg?token=BX07Q0PITB)](https://codecov.io/gh/ceres-navigation/ceres)
[![PyPI version](https://badge.fury.io/py/ceres-nav.svg)](https://badge.fury.io/py/ceres-nav) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[CERES](https://ceresnavigation.org) is an API for aiding in the ismulation of spacecraft dynamics, and the devleopment of new navigation and mapping techniques.

Releases are [registed on PyPI](https://pypi.org/project/ceres-nav/), while development is occuring on the [ceres GitHub page](https://github.com/ceres-navigation/ceres).  Any bugs should be reported to the [Issue Tracker](https://github.com/ceres-navigation/ceres/issues).  Documentation is located at [docs.ceresnavigation.org](https://docs.ceresnavigation.org)

*NOTE: Currently, CERES is only supported on Linux.  Native Windows support is coming soon, though WSL2 (available on both Windows 10 and 11) is already supported.*


## Install
`pip install ceres-nav`

Once installed, ceres can be imported using: `import ceres`

## Call for Contributions
To contribute to this project, it is highly recommended that you create a virtual environment with either mamba or conda.
1. Install mamba or conda:
    - To install mamba (RECOMENDED): [mambaforge](https://github.com/conda-forge/miniforge)
    - To install conda: [anaconda](https://www.anaconda.com/products/individual)
2. Create the virtual environment:
    - source the base environment
    - create `ceres_env` environment with ceres dependencies: `conda create -n ceres_env python=3 numpy`
    - Install tools required for development: `pip install sphinx pytest pytest-cov sphinx-rtd-theme setuptools wheel twine`
    - Activate the virtual environment with `conda activate ceres_env`
3. Installing CERES into the environment:
   - Clone: `git clone https://github.com/ceres-navigation/ceres`
   - Install: `cd ceres; pip install -e .`
4. Running tests:
   - `pytest --cov=ceres tests/`

If you are new to contributing to open source, [this
guide](https://opensource.guide/how-to-contribute/) helps explain why, what,
and how to successfully get involved.

## Contact
All questions should be directed to Chris Gnam: crgnam@buffalo.edu
