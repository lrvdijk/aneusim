from setuptools import setup, find_packages

setup(
    name='aneuploidgen',
    version='0.2.2',
    packages=find_packages(),

    # Metadata
    description='Helper script to generate synthetic aneuploid genomes.',
    author='Lucas van Dijk',
    author_email='info@lucasvandijk.nl',
    license='MIT',
    url='https://bitbucket.org/tudelft-bioinformatics/aneugen',

    # Dependencies
    install_requires=[
        'scikit-bio>=0.5.0',
        'pybedtools>=0.7'
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest'
    ],

    # Entry points
    entry_points={
        'console_scripts': [
            'aneuploidgen = aneuploidgen:main'
        ]
    }
)
