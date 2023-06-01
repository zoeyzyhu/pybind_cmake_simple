import distutils.command.build as _build
import os
import sys
from distutils import spawn
from distutils.sysconfig import get_python_lib
from setuptools import setup


def extend_build():
    class build(_build.build):
        def run(self):
            cwd = os.getcwd()
            if spawn.find_executable('cmake') is None:
                sys.stderr.write("CMake is required to build this package.\n")
                sys.exit(-1)
            _source_dir = os.path.split(__file__)[0]
            _build_dir = os.path.join(_source_dir, 'build_setup_py')
            _prefix = get_python_lib()
            try:
                cmake_configure_command = [
                    'cmake',
                    '-H{0}'.format(_source_dir),
                    '-B{0}'.format(_build_dir),
                    '-DCMAKE_INSTALL_PREFIX={0}'.format(_prefix),
                ]
                _generator = os.getenv('CMAKE_GENERATOR')
                if _generator is not None:
                    cmake_configure_command.append('-G{0}'.format(_generator))
                spawn.spawn(cmake_configure_command)
                spawn.spawn(
                    ['cmake', '--build', _build_dir, '--target', 'install'])
                os.chdir(cwd)
            except spawn.DistutilsExecError:
                sys.stderr.write("Error while building with CMake\n")
                sys.exit(-1)
            _build.build.run(self)

    return build


_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

_this_package = 'pymult'

version = {}
with open(os.path.join(_here, _this_package, 'version.py')) as f:
    exec(f.read(), version)

setup(
    name=_this_package,
    version=version['__version__'],
    description='Description in here.',
    long_description=long_description,
    author='Bruce Wayne',
    author_email='bruce.wayne@example.com',
    url='http://example.com',
    license='MIT',
    packages=[_this_package],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ],
    cmdclass={'build': extend_build()})






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

