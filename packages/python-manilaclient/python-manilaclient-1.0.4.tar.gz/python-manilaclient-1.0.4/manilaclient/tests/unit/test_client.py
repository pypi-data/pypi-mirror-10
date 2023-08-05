# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import manilaclient.client
from manilaclient.tests.unit import utils
import manilaclient.v1.client


class ClientTest(utils.TestCase):

    def test_get_client_class_v1(self):
        output = manilaclient.client.get_client_class('1')
        self.assertEqual(output, manilaclient.v1.client.Client)

    def test_get_client_class_unknown(self):
        self.assertRaises(manilaclient.exceptions.UnsupportedVersion,
                          manilaclient.client.get_client_class, '0')
