#!/bin/bash

# ====================================================
# This script assumes that you have Python3 installed 
# ====================================================

# Stop on errors, print commands
set -xEeuo pipefail

# Clear pre-existing environment settings
rm -rf env/

# Create the Python virtual environment
python3 -m venv env
