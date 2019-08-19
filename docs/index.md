# hsmfile: a Python module to expedite access to files on a remote data store

## Synopsis

This module addresses the common case where there are large data files on a supercomputer and these are to be processed, maybe on the
supercomputer or maybe on local machines that can mount the supercomputer file system. The hsmfile module provides functions to

  * Specify the file locations in a platform-independent way, given some platform-specific configuration data; and
  * Optionally copy files automatically as necessary from the supercomputer to the local machines.

It is based on a set of IDL functions with a similar purpose with the prefix
[mgh_san](https://github.com/hadfieldnz/idl-roms/tree/master/san).



