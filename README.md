# Python bindings for C++: pybind11 + cmake + setup.py

This is a toy example showing how to create Python bindings to interface with a C++ library (with only a simple function) using CMake. Everything spreads out in the current directory for simplicity. For a more structured approach, please see [`pybind_cmake_list`](https://github.com/zoeyzyhu/pybind_cmake_example). 

## Environment
It runs on Linux and MacOS.

## Create python virtual environment and install requirements

```
./1.setup.sh
source env/bin/activate
./2.install.sh
```

## Build the linked package for Python
```
./3.build.sh
```
