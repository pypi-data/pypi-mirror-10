#!/usr/bin/env python2.7
# Utool is released under the Apache License Version 2.0
# no warenty liability blah blah blah blah legal blah
# just use the software, don't be a jerk, and write kickass code.
from __future__ import absolute_import, division, print_function
from setuptools import setup
import sys


def utool_setup():
    INSTALL_REQUIRES = [
        'six >= 1.8.0',
        'psutil >= 2.1.3',
        'parse >= 1.6.6',
        'lockfile >= 0.10.2',
        'lru-dict >= 1.1.1',  # import as lru
        #'decorator',
    ]

    INSTALL_OPTIONAL = [
        'numpy >= 1.8.0',  # TODO REMOVE DEPENDENCY
        'astor',
        'sphinx',
        'sphinxcontrib-napoleon',
        'pyperclip >= 1.5.7',
        'pyfiglet >= 0.7.2',
    ]

    REQUIRES_LINKS = [
    ]

    OPTIONAL_DEPENDS_LINKS = [
        #'git+https://github.com/amitdev/lru-dict',  # TODO REMOVE DEPENDENCY
        #'git+https://github.com/pwaller/pyfiglet',

    ]

    INSTALL_OPTIONAL_EXTRA = [  # NOQA
        'guppy',
        'objgraph',
    ]

    # TODO: remove optional depends
    INSTALL_REQUIRES += INSTALL_OPTIONAL
    REQUIRES_LINKS += OPTIONAL_DEPENDS_LINKS

    try:
        # HACK: Please remove someday
        from utool import util_setup
        import utool
        from os.path import dirname
        for arg in iter(sys.argv[:]):
            # Clean clutter files
            if arg in ['clean']:
                clutter_dirs = ['cyth']
                CLUTTER_PATTERNS = [
                    '\'',
                    'cyth',
                    '*.dump.txt',
                    '*.sqlite3',
                    '*.prof',
                    '*.prof.txt',
                    '*.lprof',
                    '*.ln.pkg',
                    'failed.txt',
                    'failed_doctests.txt',
                    'failed_shelltests.txt',
                    'test_pyflann_index.flann',
                    'test_pyflann_ptsdata.npz',
                    '_test_times.txt',
                    'test_times.txt',
                    'Tgen.sh',
                ]
                utool.clean(dirname(__file__), CLUTTER_PATTERNS, clutter_dirs)
        ext_modules = util_setup.find_ext_modules()
        cmdclass = util_setup.get_cmdclass()
    except Exception as ex:
        print(ex)
        ext_modules = {}
        cmdclass = {}

    # run setuptools setup function
    setup(
        name='utool',
        packages=[
            'utool',
            'utool._internal',
            'utool.tests',
            'utool.util_scripts',
        ],
        #packages=util_setup.find_packages(),
        version='1.1.0.dev1',
        download_url='https://github.com/erotemic/utool/tarball/1.1.0.dev1',
        description='Univerally useful utility tools for you!',
        url='https://github.com/Erotemic/utool',
        ext_modules=ext_modules,
        cmdclass=cmdclass,
        author='Jon Crall',
        author_email='erotemic@gmail.com',
        keywords='',
        install_requires=INSTALL_REQUIRES,
        dependency_links=REQUIRES_LINKS,
        package_data={},
        scripts=[
            'utool/util_scripts/makesetup.py',
            'utool/util_scripts/makeinit.py',
            'utool/util_scripts/utprof.sh',
            'utool/util_scripts/utprof.py',
            'utool/util_scripts/utprof_cleaner.py',
            'utool/util_scripts/utoolwc.py',
            'utool/util_scripts/grabzippedurl.py',
            'utool/util_scripts/autogen_sphinx_docs.py',
            'utool/util_scripts/permit_gitrepo.py',
            'utool/util_scripts/viewdir.py',
        ],
        classifiers=[],
    )


if __name__ == '__main__':
    utool_setup()
