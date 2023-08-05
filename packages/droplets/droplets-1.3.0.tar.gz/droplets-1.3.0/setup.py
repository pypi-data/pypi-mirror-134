import os
from setuptools import setup

VERSION = "1.3.0"

requires = [
    "docopt",
    "ndg-httpsclient",
    "pyasn1",
    "pyopenssl",
    "requests",
]

setup_requires = ["pytest-runner"]
tests_require = ["pytest"]

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, "README.md")).read()
except IOError:
    README = CHANGES = ""

setup(
    name="droplets",
    version=VERSION,
    description="Library for building Ansible dynamic inventories for "
    "Digital Ocean.",
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: Repoze Public License",
    ],
    author="Chris Rossi",
    author_email="chris@armchimedeanco.com",
    url="http://github.com/chrisrossi/droplets",
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    py_modules=["droplets"],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
