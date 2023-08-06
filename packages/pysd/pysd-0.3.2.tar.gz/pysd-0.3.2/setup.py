from distutils.core import setup

exec(open('pysd/_version.py').read())
print __version__

long_description ="""Project Documentation: http://pysd.readthedocs.org/"""


setup(
    name='pysd',
    version=__version__,
    author='James Houghton',
    author_email='james.p.houghton@gmail.com',
    packages=['pysd', 'pysd.translators', 'pysd.functions', 'pysd.builder'],
    url='https://github.com/JamesPHoughton/pysd',
    license='LICENSE.txt',
    description='System Dynamics Modeling in Python',
    long_description=long_description,
    keywords=['System Dynamics', 'XMILE', 'Vensim'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    install_requires=[
        'pandas',
        'numpy',
        'parsimonious',
        'scipy'
    ]
)