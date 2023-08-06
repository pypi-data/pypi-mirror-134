# SPDX-FileCopyrightText: 2019-2021 Freemelt AB <opensource@freemelt.com>
#
# SPDX-License-Identifier: LGPL-3.0-only

import sys
import setuptools

sys.path.append("servicelib")
from _version import __version__

sys.path.remove("servicelib")

with open("README.md") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="servicelib",
    version=__version__,
    author="Freemelt AB",
    author_email="opensource@freemelt.com",
    description="Helpers used by the service-layer",
    long_description=long_description,
    url="https://gitlab.com/freemelt/machine-software/servicelib",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=[
        "pyyaml",
        "grpcio",
        "protobuf",
        "paho-mqtt",
        "systemd-python>=234",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Environment :: Console",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
)
