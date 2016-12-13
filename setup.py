from setuptools import setup, find_packages

setup(
    name='saem-oaipmh-client',
    version='0.1.0',
    description='OAI-PMH client for SAEM',
    url='https://github.com/logilab/saem-oaipmh-client',
    author='Logilab SA',
    author_email='contact@logilab.fr',
    license='LGPL',
    keywords='oaipmh client saem',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'pyoai',
    ],
    entry_points={
        'console_scripts': [
            'saem-oaipmh=saem_oaipmh_client.__main__',
        ],
    },
)
