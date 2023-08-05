# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import unittest

import os_client_config

from openstack import connection
from openstack import profile
from openstack import utils


class BaseFunctionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        name = os.getenv('OS_CLOUD', 'test_cloud')
        test_cloud = os_client_config.OpenStackConfig().get_one_cloud(name)

        prof = profile.Profile()
        prof.set_region(prof.ALL, test_cloud.region)
        if test_cloud.debug:
            utils.enable_logging(True)

        auth = test_cloud.config['auth']
        if 'insecure' in test_cloud.config:
            auth['verify'] = test_cloud.config['insecure']
        cls.conn = connection.Connection(profile=prof, **auth)

    @classmethod
    def assertIs(cls, expected, actual):
        if expected != actual:
            raise Exception(expected + ' != ' + actual)
