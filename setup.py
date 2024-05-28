from distutils.core import setup
setup(
    name='cicdlab-flask-runner',
    packages=['cicdlab-flask-runner'],
    version='0.1',
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='A simple runner for Flask apps',
    author='Marco Scata',
    author_email='mscata@hotmail.com',
    url='http://scmserver:3000/mscata/cicdlab-flask-runner',
    download_url='https://github.com/mscata/cicdlab-flask-runner/archive/v_01.tar.gz',
    keywords=['CI/CD'],
    install_requires=[
        'flask',
    ],
    classifiers=[ # Pick from https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Framework :: Flask',
        'Topic :: Software Development',
        'Topic :: System :: Software Distribution',
    ],
)
