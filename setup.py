from setuptools import setup, find_packages

with open('README.txt') as file:
    long_description = file.read()

setup(
    name='warmrunner',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/caktus/warmrunner',
    license='APL2',
    author='Dan Poirier',
    author_email='dpoirier@caktusgroup.com',
    description='A Django test runner that shows which tests are slowest',
    install_requires=[
        'Django>=1.7',
    ],
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ],
)
