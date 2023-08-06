# Copyright 2017-2022 Nitor Creations Oy
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
from setuptools import setup
from n_vault import VERSION

with open("README.md") as f:
    long_description = f.read()

setup(name='nitor-vault',
      version=VERSION,
      description='Vault for storing locally encypted data in S3 using KMS keys',
      url='http://github.com/NitorCreations/vault',
      download_url=f'https://github.com/NitorCreations/vault/tarball/${VERSION}',
      author='Pasi Niemi',
      author_email='pasi@nitor.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='Apache 2.0',
      packages=['n_vault'],
      include_package_data=True,
      entry_points={
          'console_scripts': ['vault=n_vault.cli:main']
      },
      install_requires=[
          'threadlocal-aws>=0.10',
          'requests',
          'argcomplete',
          'future',
          'cryptography',
          "win-unicode-console;platform_system=='Windows'",
          "wmi;platform_system=='Windows'",
          "pypiwin32;platform_system=='Windows'"
      ],
      zip_safe=False,
      tests_require=[
        'coverage',
        'coveralls'
      ])
