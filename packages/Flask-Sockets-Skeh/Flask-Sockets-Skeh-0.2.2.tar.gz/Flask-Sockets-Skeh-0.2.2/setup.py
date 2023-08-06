#!/usr/bin/env python

"""
Flask-Sockets
-------------

Elegant WebSockets for your Flask apps.
A (hopefully) maintained fork of https://github.com/heroku-python/flask-sockets by the wonderful Kenneth Reitz
"""
from setuptools import setup


setup(
    name="Flask-Sockets-Skeh",
    version="0.2.2",
    url="https://git.skeh.site/skeh/flask-sockets",
    license="MIT",
    author="Derek Schmidt",
    author_email="skeh@is.nota.live",
    description="Elegant WebSockets for your Flask apps.",
    long_description=__doc__,
    py_modules=["flask_sockets"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["flask>=2", "gevent", "gevent-websocket"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
