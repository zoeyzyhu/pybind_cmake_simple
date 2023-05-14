#!/bin/bash

# ====================================================
# This script assumes that you have Python3 installed 
# ====================================================

# Stop on errors, print commands
set -xEeuo pipefail

# Build the linked package for Python.
rm -rf build
mkdir build
cd build
cmake ..
cd ..

# Install the package for Python.
python setup.py install

# Test the built and installed package.
python test.py