from setuptools import setup, find_packages


setup(
    name='mosaik',
    version='2.1.3',
    author='Stefan Scherfke',
    author_email='stefan.scherfke at offis.de',
    maintainer='Florian Schlögl, Okko Nannen',
    maintainer_email='florian.schloegl at offis.de, okko.nannen at offis.de',
    description=('Mosaik is a flexible Smart-Grid co-simulation framework.'),
    long_description=(open('README.txt').read() + '\n\n' +
                      open('CHANGES.txt').read() + '\n\n' +
                      open('AUTHORS.txt').read()),
    url='https://moaik.offis.de',
    install_requires=[
        'networkx>=1.8.1',
        'mosaik-api>=2.1',
        'simpy>=3.0.7',
        'simpy.io>=0.2',
    ],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    entry_points={
        'console_scripts': [
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
