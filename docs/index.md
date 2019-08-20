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

Clone the source repository and install with PIP:
```
git clone https://github.com/hadfieldnz/hsmfile.github
pip install .
```

## User customisation

The hsmfile module exposes a dictionary named volume, with each entry defining an hsmfile
volume as described below. During initialisation, the dictionary is created with one
entry, pointing to the user's home directory. However at the end of the initialisation
process, the module attempts to read and execute Python code from a configuration
file, ~/.hsmfile.py. This provides an opportunity for defining further volumes

