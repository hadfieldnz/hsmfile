from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
   name='hsmfile',
   version='0.1.1',
   license='MIT',
   description='Expedite access to files on a slow network volume',
   long_description=long_description,
   author='Mark Hadfield',
   author_email='mark.hadfield@niwa.co.nz',
   url='https://github.com/hadfieldnz/hsmfile',
   packages=['hsmfile'],
   package_dir={'hsmfile':'.'},
   classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
   ],
   python_requires='>=3.6'
)
