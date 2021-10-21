"""
Pip.Services service-beacons-python
------------------

The service-beacons microservice for working with beacons data.

"""

try:
    readme = open('readme.md').read()
except:
    readme = __doc__

from setuptools import find_packages
from setuptools import setup

setup(
    name='service_beacons',
    version='0.0.1',
    url='https://github.com/pip-services-samples/service-beacons-python.git',
    license='MIT',
    author='Conceptual Vision Consulting LLC',
    author_email='seroukhov@gmail.com',
    description='Microservice for Beacons in Python',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['config', 'data', 'test']),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=[
        'pip_services3_commons',
        'pip_services3_expressions',
        'pip_services3_components',
        'pip_services3_container',
        'pip_services3_data',
        'pip_services3_mongodb',
        'pip_services3_rpc',
        'pip_services3_swagger'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
