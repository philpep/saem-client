from setuptools import setup, find_packages

setup(
    name='saem-client',
    version='0.1.0',
    description='Command-line client for a SAEM site',
    url='https://framagit.org/saemproject/saem-client',
    author='Logilab SA',
    author_email='contact@logilab.fr',
    license='LGPL',
    keywords='client saem oaipmh eac skos',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'PyYAML',
        'cwclientlib',
        'pyoai',
    ],
    entry_points={
        'console_scripts': [
            'saem-client=saem_client:main',
        ],
    },
)
