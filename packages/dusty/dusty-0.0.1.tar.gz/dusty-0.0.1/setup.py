import os
import sys
import imp
from setuptools import find_packages, setup

# try:
#     from restricted_pkg import setup
# except:
#     # allow falling back to setuptools only if
#     # we are not trying to upload
#     if 'upload' in sys.argv:
#         raise ImportError('restricted_pkg is required to upload, first do pip install restricted_pkg')
#     from setuptools import setup

setup(
    name='dusty',
    version='0.0.1',
    description='Docker-based development environment manager',
    url='https://github.com/gamechanger/dusty',
    #private_repository='gamechanger',
    author='GameChanger',
    author_email='travis@gamechanger.io',
    packages=find_packages(),
    test_suite="nose.collector",
    zip_safe=False
)
