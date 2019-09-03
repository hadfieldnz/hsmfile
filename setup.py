from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
   name='hsmfile',
   version='0.1.2',
   license='MIT',
   description='Expedite access to files on a slow network volume',
   long_description=long_description,
   long_description_content_type="text/markdown",
   author='Mark Hadfield',
   author_email='mark.hadfield@niwa.co.nz',
   url='https://github.com/hadfieldnz/hsmfile',
   packages=find_packages(),
   classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
   ],
   python_requires='>=3.6'
)
