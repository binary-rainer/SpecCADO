#!/usr/bin/env python3
"""
SpecCADO: Prototype for SimCADO spectroscopy
"""

try:
    import setuptools
except ImportError:
    pass

from datetime import datetime


def write_version(version, filename="speccado/version.py"):
    """Write the file speccado/version.py"""

    cnt = """
# THIS FILE WAS GENERATED BY SPECCADO SETUP.PY
version = '{}'
date = '{}'
"""
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %T GMT')
    with open(filename, 'w') as fd:
        fd.write(cnt.format(version, timestamp))


def setup_package(version):
    """Setup the speccado package for installation"""

    # Write version file on installation
    write_version(version)

    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name='speccado',
        version=version,
        author='Oliver Czoske',
        author_email='oliver.czoske@univie.ac.at',
        description='Prototype for SimCADO spectroscopy',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/oczoske/SpecCADO",
        license='GPL',
        packages=['speccado'],
        zip_safe=False)


if __name__ == '__main__':
    # Define version number
    major = 0
    minor = 1
    tiny = 1
    version = "{}.{}.{}".format(major, minor, tiny)
    setup_package(version)
