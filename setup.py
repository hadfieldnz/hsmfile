from setuptools import setup

setup(
   name='hsmfile',
   version='0.1',
   license='MIT',
   description='Expedite access to files on a slow network volume',
   author='Mark Hadfield',
   author_email='mark.hadfield@niwa.co.nz',
   url='https://github.com/hadfieldnz/hsmfile',
   packages=['hsmfile'],
   package_dir={'hsmfile':'.'}
)
