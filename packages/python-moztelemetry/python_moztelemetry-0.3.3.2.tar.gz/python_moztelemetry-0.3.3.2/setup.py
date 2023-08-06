#!/usr/bin/env python
# encoding: utf-8

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from distutils.core import setup

import urllib
import setuptools.command.install


class FetchExternal(setuptools.command.install.install):
    def run(self):
        urllib.urlretrieve("http://hg.mozilla.org/mozilla-central/raw-file/72940b27aeaa/toolkit/components/telemetry/histogram_tools.py", "moztelemetry/histogram_tools.py")
        setuptools.command.install.install.run(self)

setup(cmdclass={'install': FetchExternal},
      name='python_moztelemetry',
      version='0.3.3.2',
      author='Roberto Agostino Vitillo',
      author_email='rvitillo@mozilla.com',
      description='Spark bindings for Mozilla Telemetry',
      url='https://github.com/vitillo/python_moztelemetry',
      packages=['moztelemetry'],
      package_dir={'moztelemetry': 'moztelemetry'},
      install_requires=['boto', 'ujson', 'requests', 'protobuf', 'functools32', 'py4j', 'pandas>=0.15.2', 'numpy>=1.9.2', 'telemetry-tools'])
