# hsmfile: a Python module to expedite access to files on a slow network volume

## Synopsis

This module addresses the common case where there are large data files on a supercomputer and these are to be processed, maybe on the
supercomputer or maybe on local machines that can mount the supercomputer file system. The hsmfile module provides functions to

  * Specify the file locations and operate on files in a platform-independent way, given some
    platform-specific configuration data;
  * Copy files automatically from the supercomputer to the local machines.

It is based on a set of IDL functions with a similar purpose with the prefix
[mgh_san](https://github.com/hadfieldnz/idl-roms/tree/master/san).

## Installation
Install from [Conda-Forge](https://conda-forge.org/) with the conda package manager
```
conda install -c conda-forge hsmfile
```

Install from [PyPI](https://pypi.org/) with PIP:
```
pip install hsmfile
```

Clone the [GitHub](https://github.com/) repository and install with PIP in developer mode:
```
git clone https://github.com/hadfieldnz/hsmfile.github
pip install -e hsmfile
```
Or better still, fork your own copy on GitHub and clone that. This way, you can maintain your own improvements and bug fixes and optionally contribute them to the main repository.

## User customisation
The hsmfile module exposes a dictionary named volume, with each entry defining an hsmfile
volume as described below. During initialisation, the dictionary is created with one
entry, pointing to the user's home directory. However at the end of the initialisation
process, the module attempts to read and execute Python code from a configuration
file, ~/.hsmfilerc.py. This provides an opportunity for defining further volumes.

## TODO

The present user customization mechanism is insecure, as it involves executing arbitrary Python code. It will shortly be changed to one that reads volume definitions from a
configuration file using the configparser module.


