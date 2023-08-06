"""Installation script."""


#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------

import os
import os.path as op
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


#------------------------------------------------------------------------------
# Setup
#------------------------------------------------------------------------------


def _package_tree(pkgroot):
    path = op.dirname(__file__)
    subdirs = [op.relpath(i[0], path).replace(op.sep, '.')
               for i in os.walk(op.join(path, pkgroot))
               if '__init__.py' in i[2]]
    return subdirs


curdir = op.dirname(op.realpath(__file__))
readme = open(op.join(curdir, 'README.rst')).read()


# Find version number from `__init__.py` without executing it.
filename = op.join(curdir, 'klustakwik2/__init__.py')
with open(filename, 'r') as f:
    version = re.search(r"__version__ = '([^']+)'", f.read()).group(1)


requirements = [
]

test_requirements = [
]

setup(
    name='klustakwik2',
    version=version,
    description='Clustering for high dimensional neural data',
    long_description=readme,
    url='https://github.com/kwikteam/klustakwik2',
    packages=_package_tree('klustakwik2'),
    package_dir={'klustakwik2': 'klustakwik2'},
    package_data={'klustakwik2.numerics.cylib': ['*.pyx', '*.pyxbld']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'kk2_legacy=klustakwik2.scripts.kk2_legacy:main',
        ],
    },
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='klustakwik2,data analysis,electrophysiology,neuroscience,clustering',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    tests_require=test_requirements
)
