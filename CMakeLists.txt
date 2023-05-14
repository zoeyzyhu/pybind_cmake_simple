cmake_minimum_required(VERSION 3.4)
project(pymult)

# Add Pybind11 directory
add_subdirectory(pybind11)

# Create Python module
pybind11_add_module(pymult mult.cpp)
