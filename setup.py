import os
from distutils.core import setup
from setuptools import find_packages
VERSION = __import__("vida").__version__
CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
]
install_requires = [
    'ipython>=3.2.1',
]
# taken from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)
for dirpath, dirnames, filenames in os.walk('vida'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[5:] # Strip "vida/" or "vida\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))
setup(
    name="Python Vida",
    description="Python binding for Vida data visualizations",
    version=VERSION,
    author="Phuoc Do",
    author_email="phuocd@vida.io",
    url="https://github.com/vidalab/pyvida",
    download_url="https://github.com/vidalab/pyvida/archive/0.1.tar.gz",
    package_dir={'vida': 'vida'},
    packages=packages,
    package_data={'vida': data_files},
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)
