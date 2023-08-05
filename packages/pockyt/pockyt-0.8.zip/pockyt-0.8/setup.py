from __future__ import absolute_import, print_function

import sys
from setuptools import setup


if sys.version_info[0:2] not in [(2, 7), (3, 4)]:
    print('This version of Python is unsupported !\n'
          'Please use Python 2.7.x or 3.4.x !')
    sys.exit(1)


name = 'pockyt'
version = '0.8'

try:
    desc_file = open('README.rst')
except:
    desc = ''
else:
    desc = desc_file.read()
    desc_file.close()


setup(
    name=name,
    packages=[name],
    version=version,
    description='automate and manage your pocket collection',
    long_description=desc,
    author='Arvind Chembarpu',
    author_email='achembarpu@gmail.com',
    url='https://github.com/arvindch/{0}'.format(name),
    license='GPLv3+',
    install_requires=[
        'requests>=2.6',
        'parse>=1.6',
    ],
    download_url='https://github.com/arvindch/{0}/tarball/{1}'.format(name, version),
    keywords=['pocket', 'commandline', 'automation'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'pockyt=pockyt.pockyt:main',
        ],
    },
)
