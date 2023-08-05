from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(name='dftintegrate',
      version='0.0.7',
      description='Integrate DFT data',
      long_description=read_md('README.md'),
      author='Matthew M Burbidge',
      author_email='mmburbidge@gmail.com',
      url='https://github.com/mmb90/dftintegrate',
      license='MIT',
      install_requires=[
          "argparse",
          "termcolor",
          "numpy",
          "matplotlib",
          "scipy",
      ],
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Scientific/Engineering :: Information Analysis'],
      entry_points={
          'console_scripts': [
              'dftintegrate = dftintegrate.dftintegrate:main']})

# packages=['fortpy', 'fortpy.parsers', 'fortpy.isense', 'fortpy.testing',
#           'fortpy.templates', 'fortpy.interop',
#           'fortpy.printing' ],
# scripts=['fortpy/scripts/compare.py', 'fortpy/scripts/convert.py', 'fortpy/scripts/runtests.py',
#          'fortpy/scripts/analyze.py', 'fortpy/scripts/parse.py', 'fortpy/scripts/ftypes.py'],
# package_data={'fortpy': ['isense/builtin.xml']},
# include_package_data=True,S
# )
