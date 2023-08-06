# Author: Tom Richter

from setuptools import find_packages, setup

VERSION = '1.0'
with open('README.rst') as f:
    README = f.read()
if not 'dev' in VERSION:  # get image for correct version from travis-ci
    README = README.replace('branch=master', 'branch=v%s' % VERSION)
DESCRIPTION = 'Separation of intrinsic and scattering Q by envelope inversion'
LONG_DESCRIPTION = '\n'.join(README.split('\n')[7:17])

ENTRY_POINTS = {
    'console_scripts': ['qopen-runtests = qopen.tests:run',
                        'qopen = qopen.core:run_cmdline',
                        'qopen-rt = qopen.rt:main']}

DEPS = 'future obspy>=0.10 numpy scipy>=0.11 statsmodels joblib'.split()

setup(name='qopen',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      url='https://github.com/trichter/qopen',
      author='Tom Eulenfeld',
      author_email='tom.eulenfeld@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=DEPS,
      entry_points=ENTRY_POINTS,
      include_package_data=True,
      zip_safe=False
      )
