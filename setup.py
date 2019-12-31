"""
Flask-Authlib-Client
-------------
Flask-Authlib-Client is a Flask extension that adds support for separate authorization/resource servers. It extends
authlib's flask integration.
"""
from setuptools import setup

version = "0.0.1"

setup(
    name='Flask-Authlib-Client',
    version=version,
    url='https://github.com/michaelbukachi/flask-authlib-client',
    license='BSD',
    author='Michael Bukachi',
    author_email='michaelbukachi@gmail.com',
    description='An extension to add support for separate resource server authentication to authlib',
    long_description=__doc__,
    packages=['flask_authlib_client'],
    platforms='any',
    install_requires=['Flask', 'Authlib'],
    setup_requires=['pytest-runner', 'wheel', 'twine'],
    tests_require=['pytest', 'pytest-cov'],
    keywords='flask authlib',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
