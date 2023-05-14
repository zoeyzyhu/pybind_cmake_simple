#!/bin/bash

# ====================================================
# This script assumes that you have Python3 installed 
# ====================================================

# Stop on errors, print commands
set -xEeuo pipefail

# Upgrade pip
pip install --upgrade pip setuptools

# Install requirements
pip install -r requirements.txt

