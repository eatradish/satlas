from setuptools import setup
exec(open('satlas/version.py').read())
setup(
  name='satlas',
  packages=['satlas', 'satlas.lmfit', 'satlas.lmfit.ui', 'satlas.lmfit.uncertainties', 'satlas.emcee', 'satlas.tqdm'],
  version=__release__,
  description='This Python package has been created with the goal of creating an easier interface for the analysis of data gathered from laser spectroscopy experiments. Support for fitting the spectra, using both chi2-fitting and Maximum Likelihood Estimation routines, are present.',
  author='Wouter Gins',
  author_email='woutergins@fys.kuleuven.be',
  url='https://woutergins.github.io/satlas/',
  license='MIT',
  download_url='https://github.com/woutergins/satlas/archive/master.zip',
  keywords=['physics', 'hyperfine structure', 'fitting'],
  install_requires=['numpy>=1.5',
                    'scipy>=0.13',
                    'sympy',
                    'matplotlib',
                    'pandas',
                    'h5py'],
  classifiers=['Development Status :: 4 - Beta',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: MIT License',
               'Operating System :: Microsoft :: Windows',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 3',
               'Topic :: Scientific/Engineering :: Physics'],
)
