"""GitHub.com project hadfieldnz/hsmfile: expedite file access on slow network volumes"""

# The hsmfile module is modelled on my IDL mgh_san routines:
#   https://github.com/hadfieldnz/idl-roms/tree/master/san

# For usage examples see:
#   https://git.niwa.local/hadfield/notebooks-mgh/blob/master/examples/HSMfile_examples.ipynb

# MGH 2019-08-05
#   - Written

import shutil
import logging
import pathlib

# The global variable "volume" is a dictionary that will contain entries
# each defining an hsmfile volume. Create the variable and populate it with an
# entry specifying the home directory.

volume = {}
volume['HOME'] = {'master': pathlib.Path.home()}

# The global variable "default" is the name (dictionary key) of the default volume.

default = 'HOME'

# The above variables will normally be modified or overidden in the file ~/.hsmfile.py.

RCFILE = pathlib.Path(pathlib.Path.home(),'.hsmfilerc.py')

def loadconfig(file=RCFILE):
    # The following idiom is adopted from https://tinyurl.com/yyk4yza3. It is
    # thread-safe, unlike the other code in this module!
    try:
        with open(file) as f:
            code = compile(f.read(), RCFILE, 'exec')
            exec(code)
        logging.info(f"Configuration file {file} loaded")
    except FileNotFoundError:
        logging.warning(f"Configuration file {file} was not found")

loadconfig()

def path(name='',sub='',vol=default,mirror=False):
    """Return a path on the remote (master) or local (mirror volume)"""
    if mirror:
        root = volume[vol]['mirror']
        return pathlib.Path(root,sub,name)
    else:
        root = volume[vol]['master']
        return pathlib.Path(root,sub,name)

def search(pattern='*',sub='',vol=default,mirror=False):
    """Search for files on the remote (master) or local (mirror volume)"""
    base = path(sub=sub,vol=vol,mirror=mirror)
    return sorted([f.relative_to(base) for f in base.glob(pattern)])

def file(name='',sub='',vol=default,mirror=None):
    """Return a pathlib.Path object for a file

    The file must exist on the master and is automatically copied to the
    mirror as necessary
    """
    if mirror is None:
        mirror = 'mirror' in volume[vol]
    path_master = path(name,sub,vol,mirror=False)
    if not path_master.is_file():
        raise Exception(f"File does not exist: {path_master}")
    if mirror:
        path_mirror = path(name,sub,vol,mirror=True)
        copy = False
        if not path_mirror.is_file():
            copy = True
        elif path_mirror.stat().st_size == 0:
            copy = True
        elif path_mirror.stat().st_mtime < path_master.stat().st_mtime:
            copy = True
        if copy:
            print(f"Copying {path_master} to {path_mirror}")
            path_mirror.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path_master,path_mirror)
        return path_mirror
    else:
        return path_master
