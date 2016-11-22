
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    # Name & Version
    name='bossconf',
    version='0.1a10',

    # Description
    description='Config parser with token interpreter',
    long_description=long_description,

    # Source
    url='https://github.com/mihailv/bossconf',

    # Author details
    author='Mihail Vasile',
    author_email='mihail.catalin.vasile@gmail.com',

    # Licence
    license='MIT',

    # Classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Development status
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Audience
        'Intended Audience :: Developers',

        # Licence classification
        'License :: OSI Approved :: MIT License',

        # Python versions supported here.
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    # Project keywords
    keywords='config library development boss',

    # Packages import
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Run-time dependencies ( installed by pip when project is installed )
    # 
    # "install_requires" vs pip's requirements files see:
    #    https://packaging.python.org/en/latest/requirements.html
    install_requires=['pyaml'],

    # Additional groups of dependencies ( environment [dev, test] dependent )
    # You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # Data files included in the packages 
    # For:
    #   Python 2.6 or less, then these have to be included in MANIFEST.in as well.
    package_data={
        'bossconf': ['package_data.dat'],
    },

    # Data files outside of your packages.
    # See:
    #   http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # Will be installed into '<sys.prefix>/my_data'
    # ex:
    #    data_files=[('my_data', ['data/data_file'])],

    # Executable scripts
    entry_points={
        'console_scripts': [
            'bossconf=bossconf:main_cli',
        ],
    },
)
