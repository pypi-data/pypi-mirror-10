"""
    Flask-AppUtils
    ~~~~~~~~~~~~~~

    A collection of useful patterns and helpers for Flask applications

    install
    -------
    ::

        $ pip install flask-apputils


    modules
    -------
    - `decorators`
    - `filters`
    - `helpers`
    - `routing`
    - `middlewares`
    - `mimes`
    - `sessions.itdangerous_session`
    - `sessions.redis_session`
    - `validators`


    See: Readme_

    .. Readme: https://github.com/kofrasa/flask-apputils/blob/master/README.md
"""

from setuptools import setup


setup(
    name='Flask-AppUtils',
    version='0.1.1',
    license='BSD',
    author='Francis Asante',
    author_email='kofrasa@gmail.com',
    url='http://github.com/kofrasa/flask-apputils',
    description='A collection of useful patterns and helpers for Flask applications',
    long_description=__doc__,
    packages=['flask_apputils'],
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=['Flask>=0.8'],
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)