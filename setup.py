import setuptools, os
import subprocess

# Detect the Pybind11 include directory
output = subprocess.check_output(["python3", "-m", "pybind11", "--includes"]).decode("utf-8").strip()
include_dirs = output.split(" ")
if len(include_dirs) >= 2:
    pybind11_include = include_dirs[1].strip()[2:]
else:
    pybind11_include_dir = include_dirs[0].strip()[2:]

setuptools.setup(
    name="pymult",
    author="Zoey Hu",
    author_email="zoey.zyhu@gmail.com",
    description="A C++ library for multiplication",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: Linux, MacOS",
    ],
    python_requires='>=3.6',
    install_requires=['pybind11>=2.6'],
    ext_modules=[
        setuptools.Extension(
            name="pymult",
            sources=["mult.cpp"],
			include_dirs=[".", pybind11_include],
            language="c++",
			extra_compile_args=["-std=c++11"]
        ),
    ],
)

