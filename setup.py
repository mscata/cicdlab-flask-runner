from distutils.core import setup
from setuptools import find_packages

with open('version.txt') as version_file:
    version = version_file.read().strip()

setup(
    name='cicdlab-flask-runner',
    packages=find_packages(),
    version=version,
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='A simple runner for Flask apps',
    author='Marco Scata',
    author_email='mscata@hotmail.com',
    url='http://scmserver:3000/mscata/cicdlab-flask-runner',
    download_url='https://github.com/mscata/cicdlab-flask-runner/archive/v_01.tar.gz',
    keywords=['CI/CD'],
    classifiers=[ # Pick from https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Framework :: Flask',
        'Topic :: Software Development',
        'Topic :: System :: Software Distribution',
    ],
    include_package_data=True,
)
