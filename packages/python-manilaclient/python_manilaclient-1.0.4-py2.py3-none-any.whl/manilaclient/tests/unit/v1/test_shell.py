# Copyright 2013 OpenStack LLC.
# Copyright 2014 Mirantis, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import ddt
import fixtures
import mock
from oslo_utils import strutils
import six
from six.moves.urllib import parse

from manilaclient import client
from manilaclient.common import constants
from manilaclient import exceptions
from manilaclient.openstack.common.apiclient import utils as apiclient_utils
from manilaclient.openstack.common import cliutils
from manilaclient import shell
from manilaclient.tests.unit import utils as test_utils
from manilaclient.tests.unit.v1 import fakes
from manilaclient.v1 import shell as shell_v1


@ddt.ddt
class ShellTest(test_utils.TestCase):

    FAKE_ENV = {
        'MANILA_USERNAME': 'username',
        'MANILA_PASSWORD': 'password',
        'MANILA_PROJECT_ID': 'project_id',
        'OS_SHARE_API_VERSION': '2',
        'MANILA_URL': 'http://no.where',
    }

    # Patch os.environ to avoid required auth info.
    def setUp(self):
        """Run before each test."""
        super(ShellTest, self).setUp()
        for var in self.FAKE_ENV:
            self.useFixture(fixtures.EnvironmentVariable(var,
                                                         self.FAKE_ENV[var]))

        self.shell = shell.OpenStackManilaShell()

        # HACK(bcwaldon): replace this when we start using stubs
        self.old_get_client_class = client.get_client_class
        client.get_client_class = lambda *_: fakes.FakeClient

        # Following shows available separators for optional params
        # and its values
        self.separators = [' ', '=']
        self.create_share_body = {
            "share": {
                "share_type": None,
                "name": None,
                "snapshot_id": None,
                "description": None,
                "metadata": {},
                "share_proto": "nfs",
                "share_network_id": None,
                "size": 1,
                "is_public": False,
            }
        }

    def tearDown(self):
        # For some method like test_image_meta_bad_action we are
        # testing a SystemExit to be thrown and object self.shell has
        # no time to get instantatiated which is OK in this case, so
        # we make sure the method is there before launching it.
        if hasattr(self.shell, 'cs') and hasattr(self.shell.cs,
                                                 'clear_callstack'):
            self.shell.cs.clear_callstack()

        # HACK(bcwaldon): replace this when we start using stubs
        client.get_client_class = self.old_get_client_class
        super(ShellTest, self).tearDown()

    def run_command(self, cmd):
        self.shell.main(cmd.split())

    def assert_called(self, method, url, body=None, **kwargs):
        return self.shell.cs.assert_called(method, url, body, **kwargs)

    def assert_called_anytime(self, method, url, body=None):
        return self.shell.cs.assert_called_anytime(method, url, body)

    def test_list(self):
        self.run_command('list')
        # NOTE(jdg): we default to detail currently
        self.assert_called('GET', '/shares/detail')

    def test_list_filter_status(self):
        for separator in self.separators:
            self.run_command('list --status' + separator + 'available')
            self.assert_called('GET', '/shares/detail?status=available')

    def test_list_filter_name(self):
        for separator in self.separators:
            self.run_command('list --name' + separator + '1234')
            self.assert_called('GET', '/shares/detail?name=1234')

    def test_list_all_tenants_only_key(self):
        self.run_command('list --all-tenants')
        self.assert_called('GET', '/shares/detail?all_tenants=1')

    def test_list_all_tenants_key_and_value_1(self):
        for separator in self.separators:
            self.run_command('list --all-tenants' + separator + '1')
            self.assert_called('GET', '/shares/detail?all_tenants=1')

    def test_list_all_tenants_key_and_value_0(self):
        for separator in self.separators:
            self.run_command('list --all-tenants' + separator + '0')
            self.assert_called('GET', '/shares/detail')

    def test_list_filter_by_share_server_and_its_aliases(self):
        aliases = [
            '--share-server-id', '--share-server_id',
            '--share_server-id', '--share_server_id',
        ]
        for alias in aliases:
            for separator in self.separators:
                self.run_command('list ' + alias + separator + '1234')
                self.assert_called(
                    'GET', '/shares/detail?share_server_id=1234')

    def test_list_filter_by_metadata(self):
        self.run_command('list --metadata key=value')
        self.assert_called(
            'GET', '/shares/detail?metadata=%7B%27key%27%3A+%27value%27%7D')

    def test_list_filter_by_extra_specs_and_its_aliases(self):
        aliases = ['--extra-specs', '--extra_specs', ]
        for alias in aliases:
            self.run_command('list ' + alias + ' key=value')
            self.assert_called(
                'GET',
                '/shares/detail?extra_specs=%7B%27key%27%3A+%27value%27%7D',
            )

    def test_list_filter_by_share_type_and_its_aliases(self):
        fake_st = type('Empty', (object,), {'id': 'fake_st'})
        aliases = [
            '--share-type', '--share_type', '--share-type-id',
            '--share-type_id', '--share_type-id', '--share_type_id',
        ]
        for alias in aliases:
            for separator in self.separators:
                with mock.patch.object(
                        apiclient_utils,
                        'find_resource',
                        mock.Mock(return_value=fake_st)):
                    self.run_command('list ' + alias + separator + fake_st.id)
                    self.assert_called(
                        'GET', '/shares/detail?share_type_id=' + fake_st.id)

    def test_list_filter_by_share_type_not_found(self):
        for separator in self.separators:
            self.assertRaises(
                exceptions.CommandError,
                self.run_command,
                'list --share-type' + separator + 'not_found_expected',
            )
            self.assert_called('GET', '/types?is_public=all')

    def test_list_with_limit(self):
        for separator in self.separators:
            self.run_command('list --limit' + separator + '50')
            self.assert_called('GET', '/shares/detail?limit=50')

    def test_list_with_offset(self):
        for separator in self.separators:
            self.run_command('list --offset' + separator + '50')
            self.assert_called('GET', '/shares/detail?offset=50')

    def test_list_with_sort_dir_verify_keys(self):
        # Verify allowed aliases and keys
        aliases = ['--sort_dir', '--sort-dir']
        for alias in aliases:
            for key in constants.SORT_DIR_VALUES:
                for separator in self.separators:
                    self.run_command('list ' + alias + separator + key)
                    self.assert_called('GET', '/shares/detail?sort_dir=' + key)

    def test_list_with_fake_sort_dir(self):
        self.assertRaises(
            ValueError,
            self.run_command,
            'list --sort-dir fake_sort_dir',
        )

    def test_list_with_sort_key_verify_keys(self):
        # Verify allowed aliases and keys
        aliases = ['--sort_key', '--sort-key']
        for alias in aliases:
            for key in constants.SHARE_SORT_KEY_VALUES:
                for separator in self.separators:
                    self.run_command('list ' + alias + separator + key)
                    key = 'share_network_id' if key == 'share_network' else key
                    key = 'snapshot_id' if key == 'snapshot' else key
                    key = 'share_type_id' if key == 'share_type' else key
                    self.assert_called('GET', '/shares/detail?sort_key=' + key)

    def test_list_with_fake_sort_key(self):
        self.assertRaises(
            ValueError,
            self.run_command,
            'list --sort-key fake_sort_key',
        )

    def test_list_filter_by_snapshot(self):
        fake_s = type('Empty', (object,), {'id': 'fake_snapshot_id'})
        for separator in self.separators:
            with mock.patch.object(
                    apiclient_utils,
                    'find_resource',
                    mock.Mock(return_value=fake_s)):
                self.run_command('list --snapshot' + separator + fake_s.id)
                self.assert_called(
                    'GET', '/shares/detail?snapshot_id=' + fake_s.id)

    def test_list_filter_by_snapshot_not_found(self):
        self.assertRaises(
            exceptions.CommandError,
            self.run_command,
            'list --snapshot not_found_expected',
        )
        self.assert_called('GET', '/snapshots/detail')

    def test_list_filter_by_host(self):
        for separator in self.separators:
            self.run_command('list --host' + separator + 'fake_host')
            self.assert_called('GET', '/shares/detail?host=fake_host')

    def test_list_filter_by_share_network(self):
        aliases = ['--share-network', '--share_network', ]
        fake_sn = type('Empty', (object,), {'id': 'fake_share_network_id'})
        for alias in aliases:
            for separator in self.separators:
                with mock.patch.object(
                        apiclient_utils,
                        'find_resource',
                        mock.Mock(return_value=fake_sn)):
                    self.run_command('list ' + alias + separator + fake_sn.id)
                    self.assert_called(
                        'GET', '/shares/detail?share_network_id=' + fake_sn.id)

    def test_list_filter_by_share_network_not_found(self):
        self.assertRaises(
            exceptions.CommandError,
            self.run_command,
            'list --share-network not_found_expected',
        )
        self.assert_called('GET', '/share-networks/detail')

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_type_list(self):
        self.run_command('type-list')

        self.assert_called('GET', '/types')
        cliutils.print_list.assert_called_once_with(
            mock.ANY,
            ['ID', 'Name', 'Visibility', 'is_default', 'required_extra_specs'],
            mock.ANY)

    def test_type_list_default_volume_type(self):
        self.run_command('type-list')
        self.assert_called_anytime('GET', '/types/default')

    def test_type_list_all(self):
        self.run_command('type-list --all')
        self.assert_called_anytime('GET', '/types?is_public=all')

    @ddt.data(True, False)
    def test_type_create_with_access(self, public):
        expected = {
            'share_type': {
                'name': 'test-type-3',
                'extra_specs': {'driver_handles_share_servers': False},
                'os-share-type-access:is_public': public
            }
        }
        self.run_command(
            'type-create test-type-3 false --is-public %s' %
            six.text_type(public))
        self.assert_called('POST', '/types', body=expected)

    def test_type_access_list(self):
        self.run_command('type-access-list 3')
        self.assert_called('GET', '/types/3/os-share-type-access')

    def test_type_access_add_project(self):
        expected = {'addProjectAccess': {'project': '101'}}
        self.run_command('type-access-add 3 101')
        self.assert_called('POST', '/types/3/action', body=expected)

    def test_type_access_remove_project(self):
        expected = {'removeProjectAccess': {'project': '101'}}
        self.run_command('type-access-remove 3 101')
        self.assert_called('POST', '/types/3/action', body=expected)

    def test_list_filter_by_project_id(self):
        aliases = ['--project-id', '--project_id']
        for alias in aliases:
            for separator in self.separators:
                self.run_command('list ' + alias + separator + 'fake_id')
                self.assert_called('GET', '/shares/detail?project_id=fake_id')

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_list_with_public_shares(self):
        listed_fields = [
            'ID',
            'Name',
            'Size',
            'Share Proto',
            'Status',
            'Is Public',
            'Share Type',
            'Export location',
            'Host'
        ]
        self.run_command('list --public')
        self.assert_called('GET', '/shares/detail?is_public=True')
        cliutils.print_list.assert_called_with(mock.ANY, listed_fields)

    def test_show(self):
        self.run_command('show 1234')
        self.assert_called('GET', '/shares/1234')

    @ddt.data({'cmd_args': '--driver_options opt1=opt1 opt2=opt2'
                           ' --share_type fake_share_type',
               'valid_params': {
                   'driver_options': {'opt1': 'opt1', 'opt2': 'opt2'},
                   'share_type': 'fake_share_type',
               }},
              {'cmd_args': '--share_type fake_share_type',
               'valid_params': {
                   'driver_options': {},
                   'share_type': 'fake_share_type',
               }},
              {'cmd_args': '',
               'valid_params': {
                   'driver_options': {},
                   'share_type': None,
               }},)
    @ddt.unpack
    def test_manage(self, cmd_args, valid_params):
        self.run_command('manage fake_service fake_protocol fake_export_path '
                         + cmd_args)
        expected = {
            'share': {
                'service_host': 'fake_service',
                'protocol': 'fake_protocol',
                'export_path': 'fake_export_path',
                'name': None,
                'description': None,
            }
        }
        expected['share'].update(valid_params)

        self.assert_called('POST', '/os-share-manage', body=expected)

    def test_unmanage(self):
        self.run_command('unmanage 1234')
        self.assert_called('POST', '/os-share-unmanage/1234/unmanage')

    def test_delete(self):
        self.run_command('delete 1234')
        self.assert_called('DELETE', '/shares/1234')

    def test_delete_not_found(self):
        self.assertRaises(
            exceptions.CommandError,
            self.run_command,
            'delete fake-not-found'
        )

    def test_list_snapshots(self):
        self.run_command('snapshot-list')
        self.assert_called('GET', '/snapshots/detail')

    def test_list_snapshots_all_tenants_only_key(self):
        self.run_command('snapshot-list --all-tenants')
        self.assert_called('GET', '/snapshots/detail?all_tenants=1')

    def test_list_snapshots_all_tenants_key_and_value_1(self):
        for separator in self.separators:
            self.run_command('snapshot-list --all-tenants' + separator + '1')
            self.assert_called(
                'GET', '/snapshots/detail?all_tenants=1')

    def test_list_snapshots_all_tenants_key_and_value_0(self):
        for separator in self.separators:
            self.run_command('snapshot-list --all-tenants' + separator + '0')
            self.assert_called('GET', '/snapshots/detail')

    def test_list_snapshots_filter_by_name(self):
        for separator in self.separators:
            self.run_command('snapshot-list --name' + separator + '1234')
            self.assert_called(
                'GET', '/snapshots/detail?name=1234')

    def test_list_snapshots_filter_by_status(self):
        for separator in self.separators:
            self.run_command('snapshot-list --status' + separator + '1234')
            self.assert_called(
                'GET', '/snapshots/detail?status=1234')

    def test_list_snapshots_filter_by_share_id(self):
        aliases = ['--share_id', '--share-id']
        for alias in aliases:
            for separator in self.separators:
                self.run_command('snapshot-list ' + alias + separator + '1234')
                self.assert_called(
                    'GET', '/snapshots/detail?share_id=1234')

    def test_list_snapshots_only_used(self):
        for separator in self.separators:
            self.run_command('snapshot-list --usage' + separator + 'used')
            self.assert_called('GET', '/snapshots/detail?usage=used')

    def test_list_snapshots_only_unused(self):
        for separator in self.separators:
            self.run_command('snapshot-list --usage' + separator + 'unused')
            self.assert_called('GET', '/snapshots/detail?usage=unused')

    def test_list_snapshots_any(self):
        for separator in self.separators:
            self.run_command('snapshot-list --usage' + separator + 'any')
            self.assert_called('GET', '/snapshots/detail?usage=any')

    def test_list_snapshots_with_limit(self):
        for separator in self.separators:
            self.run_command('snapshot-list --limit' + separator + '50')
            self.assert_called(
                'GET', '/snapshots/detail?limit=50')

    def test_list_snapshots_with_offset(self):
        for separator in self.separators:
            self.run_command('snapshot-list --offset' + separator + '50')
            self.assert_called(
                'GET', '/snapshots/detail?offset=50')

    def test_list_snapshots_with_sort_dir_verify_keys(self):
        aliases = ['--sort_dir', '--sort-dir']
        for alias in aliases:
            for key in constants.SORT_DIR_VALUES:
                for separator in self.separators:
                    self.run_command(
                        'snapshot-list ' + alias + separator + key)
                    self.assert_called(
                        'GET',
                        '/snapshots/detail?sort_dir=' + key)

    def test_list_snapshots_with_fake_sort_dir(self):
        self.assertRaises(
            ValueError,
            self.run_command,
            'snapshot-list --sort-dir fake_sort_dir',
        )

    def test_list_snapshots_with_sort_key_verify_keys(self):
        aliases = ['--sort_key', '--sort-key']
        for alias in aliases:
            for key in constants.SNAPSHOT_SORT_KEY_VALUES:
                for separator in self.separators:
                    self.run_command(
                        'snapshot-list ' + alias + separator + key)
                    self.assert_called(
                        'GET',
                        '/snapshots/detail?sort_key=' + key)

    def test_list_snapshots_with_fake_sort_key(self):
        self.assertRaises(
            ValueError,
            self.run_command,
            'snapshot-list --sort-key fake_sort_key',
        )

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_extra_specs_list(self):
        self.run_command('extra-specs-list')

        self.assert_called('GET', '/types?is_public=all')
        cliutils.print_list.assert_called_once_with(
            mock.ANY, ['ID', 'Name', 'all_extra_specs'], mock.ANY)

    def test_type_create_without_required_extra_spec(self):
        self.assertRaises(
            exceptions.CommandError,
            self.run_command,
            'type-create test',
        )

    @ddt.data('fake', 'FFFalse', 'trueee')
    def test_type_create_invalid_extra_spec(self, extra_spec):
        self.assertRaises(
            exceptions.CommandError,
            self.run_command,
            'type-create test ' + extra_spec,
        )

    @ddt.unpack
    @ddt.data({'expected_bool': True, 'text': 'true'},
              {'expected_bool': True, 'text': '1'},
              {'expected_bool': False, 'text': 'false'},
              {'expected_bool': False, 'text': '0'})
    def test_type_create(self, expected_bool, text):
        expected = {
            "share_type": {
                "name": "test",
                "os-share-type-access:is_public": True,
                "extra_specs": {
                    "driver_handles_share_servers": expected_bool
                }
            }
        }

        self.run_command('type-create test ' + text)

        self.assert_called('POST', '/types', body=expected)

    @ddt.data('--is-public', '--is_public')
    def test_update(self, alias):
        # basic rename with positional agruments
        self.run_command('update 1234 --name new-name')
        expected = {'share': {'display_name': 'new-name'}}
        self.assert_called('PUT', '/shares/1234', body=expected)
        # change description only
        self.run_command('update 1234 --description=new-description')
        expected = {'share': {'display_description': 'new-description'}}
        self.assert_called('PUT', '/shares/1234', body=expected)
        # update is_public attr
        valid_is_public_values = strutils.TRUE_STRINGS + strutils.FALSE_STRINGS
        for is_public in valid_is_public_values:
            self.run_command('update 1234 %(alias)s %(value)s' % {
                'alias': alias,
                'value': is_public})
            expected = {
                'share': {
                    'is_public': strutils.bool_from_string(is_public,
                                                           strict=True),
                },
            }
            self.assert_called('PUT', '/shares/1234', body=expected)
        for invalid_val in ['truebar', 'bartrue']:
            self.assertRaises(ValueError, self.run_command,
                              'update 1234 %(alias)s %(value)s' % {
                                  'alias': alias,
                                  'value': invalid_val})
        # update all attributes
        self.run_command('update 1234 --name new-name '
                         '--description=new-description '
                         '%s True' % alias)
        expected = {'share': {
            'display_name': 'new-name',
            'display_description': 'new-description',
            'is_public': True,
        }}
        self.assert_called('PUT', '/shares/1234', body=expected)
        self.assertRaises(exceptions.CommandError,
                          self.run_command, 'update 1234')

    def test_rename_snapshot(self):
        # basic rename with positional agruments
        self.run_command('snapshot-rename 1234 new-name')
        expected = {'snapshot': {'display_name': 'new-name'}}
        self.assert_called('PUT', '/snapshots/1234', body=expected)
        # change description only
        self.run_command('snapshot-rename 1234 '
                         '--description=new-description')
        expected = {'snapshot': {'display_description': 'new-description'}}

        self.assert_called('PUT', '/snapshots/1234', body=expected)
        # snapshot-rename and change description
        self.run_command('snapshot-rename 1234 new-name '
                         '--description=new-description')
        expected = {'snapshot': {
            'display_name': 'new-name',
            'display_description': 'new-description',
        }}
        self.assert_called('PUT', '/snapshots/1234', body=expected)
        # noop, the only all will be the lookup
        self.assertRaises(exceptions.CommandError,
                          self.run_command, 'snapshot-rename 1234')

    def test_set_metadata_set(self):
        self.run_command('metadata 1234 set key1=val1 key2=val2')
        self.assert_called('POST', '/shares/1234/metadata',
                           {'metadata': {'key1': 'val1', 'key2': 'val2'}})

    def test_set_metadata_delete_dict(self):
        self.run_command('metadata 1234 unset key1=val1 key2=val2')
        self.assert_called('DELETE', '/shares/1234/metadata/key1')
        self.assert_called('DELETE', '/shares/1234/metadata/key2', pos=-2)

    def test_set_metadata_delete_keys(self):
        self.run_command('metadata 1234 unset key1 key2')
        self.assert_called('DELETE', '/shares/1234/metadata/key1')
        self.assert_called('DELETE', '/shares/1234/metadata/key2', pos=-2)

    def test_share_metadata_update_all(self):
        self.run_command('metadata-update-all 1234 key1=val1 key2=val2')
        self.assert_called('PUT', '/shares/1234/metadata',
                           {'metadata': {'key1': 'val1', 'key2': 'val2'}})

    def test_extract_metadata(self):
        # mimic the result of argparse's parse_args() method
        class Arguments:
            def __init__(self, metadata=[]):
                self.metadata = metadata

        inputs = [
            ([], {}),
            (["key=value"], {"key": "value"}),
            (["key"], {"key": None}),
            (["k1=v1", "k2=v2"], {"k1": "v1", "k2": "v2"}),
            (["k1=v1", "k2"], {"k1": "v1", "k2": None}),
            (["k1", "k2=v2"], {"k1": None, "k2": "v2"})
        ]

        for input in inputs:
            args = Arguments(metadata=input[0])
            self.assertEqual(shell_v1._extract_metadata(args), input[1])

    def test_reset_state(self):
        self.run_command('reset-state 1234')
        expected = {'os-reset_status': {'status': 'available'}}
        self.assert_called('POST', '/shares/1234/action', body=expected)

    def test_reset_state_with_flag(self):
        self.run_command('reset-state --state error 1234')
        expected = {'os-reset_status': {'status': 'error'}}
        self.assert_called('POST', '/shares/1234/action', body=expected)

    def test_snapshot_reset_state(self):
        self.run_command('snapshot-reset-state 1234')
        expected = {'os-reset_status': {'status': 'available'}}
        self.assert_called('POST', '/snapshots/1234/action', body=expected)

    def test_snapshot_reset_state_with_flag(self):
        self.run_command('snapshot-reset-state --state error 1234')
        expected = {'os-reset_status': {'status': 'error'}}
        self.assert_called('POST', '/snapshots/1234/action', body=expected)

    @ddt.data(
        {},
        {'--name': 'fake_name'},
        {'--description': 'fake_description'},
        {'--nova_net_id': 'fake_nova_net_id'},
        {'--neutron_net_id': 'fake_neutron_net_id'},
        {'--neutron_subnet_id': 'fake_neutron_subnet_id'},
        {'--description': 'fake_description',
         '--name': 'fake_name',
         '--neutron_net_id': 'fake_neutron_net_id',
         '--neutron_subnet_id': 'fake_neutron_subnet_id',
         '--nova_net_id': 'fake_nova_net_id'})
    def test_share_network_create(self, data):
        cmd = 'share-network-create'
        for k, v in data.items():
            cmd += ' ' + k + ' ' + v

        self.run_command(cmd)

        self.assert_called('POST', '/share-networks')

    @ddt.data(
        {'--name': 'fake_name'},
        {'--description': 'fake_description'},
        {'--nova_net_id': 'fake_nova_net_id'},
        {'--neutron_net_id': 'fake_neutron_net_id'},
        {'--neutron_subnet_id': 'fake_neutron_subnet_id'},
        {'--description': 'fake_description',
         '--name': 'fake_name',
         '--neutron_net_id': 'fake_neutron_net_id',
         '--neutron_subnet_id': 'fake_neutron_subnet_id',
         '--nova_net_id': 'fake_nova_net_id'})
    def test_share_network_update(self, data):
        cmd = 'share-network-update 1111'
        expected = dict()
        for k, v in data.items():
            cmd += ' ' + k + ' ' + v
            expected[k[2:]] = v
        expected = dict(share_network=expected)

        self.run_command(cmd)

        self.assert_called('PUT', '/share-networks/1111', body=expected)

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list(self):
        self.run_command('share-network-list')
        self.assert_called(
            'GET',
            '/share-networks/detail',
        )
        cliutils.print_list.assert_called_once_with(
            mock.ANY,
            fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_all_tenants(self):
        self.run_command('share-network-list --all-tenants')
        self.assert_called(
            'GET',
            '/share-networks/detail?all_tenants=1',
        )
        cliutils.print_list.assert_called_once_with(
            mock.ANY,
            fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    @mock.patch.object(shell_v1, '_find_security_service', mock.Mock())
    def test_share_network_list_filter_by_security_service(self):
        ss = type('FakeSecurityService', (object,), {'id': 'fake-ss-id'})
        shell_v1._find_security_service.return_value = ss
        for command in ['--security_service', '--security-service']:
            self.run_command('share-network-list %(command)s %(ss_id)s' %
                             {'command': command,
                              'ss_id': ss.id})
            self.assert_called(
                'GET',
                '/share-networks/detail?security_service_id=%s' % ss.id,
            )
            shell_v1._find_security_service.assert_called_with(mock.ANY, ss.id)
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_project_id_aliases(self):
        for command in ['--project-id', '--project_id']:
            self.run_command('share-network-list %s 1234' % command)
            self.assert_called(
                'GET',
                '/share-networks/detail?project_id=1234',
            )
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_created_before_aliases(self):
        for command in ['--created-before', '--created_before']:
            self.run_command('share-network-list %s 2001-01-01' % command)
            self.assert_called(
                'GET',
                '/share-networks/detail?created_before=2001-01-01',
            )
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_created_since_aliases(self):
        for command in ['--created-since', '--created_since']:
            self.run_command('share-network-list %s 2001-01-01' % command)
            self.assert_called(
                'GET',
                '/share-networks/detail?created_since=2001-01-01',
            )
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_nova_net_id_aliases(self):
        for command in ['--nova-net-id', '--nova-net_id',
                        '--nova_net-id', '--nova_net_id']:
            self.run_command('share-network-list %s fake-id' % command)
            self.assert_called(
                'GET',
                '/share-networks/detail?nova_net_id=fake-id',
            )
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_neutron_net_id_aliases(self):
        for command in ['--neutron-net-id', '--neutron-net_id',
                        '--neutron_net-id', '--neutron_net_id']:
            self.run_command('share-network-list %s fake-id' % command)
            self.assert_called(
                'GET',
                '/share-networks/detail?neutron_net_id=fake-id',
            )
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_neutron_subnet_id_aliases(self):
        for command in ['--neutron-subnet-id', '--neutron-subnet_id',
                        '--neutron_subnet-id', '--neutron_subnet_id']:
            self.run_command('share-network-list %s fake-id' % command)
            self.assert_called(
                'GET',
                '/share-networks/detail?neutron_subnet_id=fake-id',
            )
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_network_type_aliases(self):
        for command in ['--network_type', '--network-type']:
            self.run_command('share-network-list %s local' % command)
            self.assert_called(
                'GET',
                '/share-networks/detail?network_type=local',
            )
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_segmentation_id_aliases(self):
        for command in ['--segmentation-id', '--segmentation_id']:
            self.run_command('share-network-list %s 1234' % command)
            self.assert_called(
                'GET',
                '/share-networks/detail?segmentation_id=1234',
            )
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_ip_version_aliases(self):
        for command in ['--ip-version', '--ip_version']:
            self.run_command('share-network-list %s 4' % command)
            self.assert_called(
                'GET',
                '/share-networks/detail?ip_version=4',
            )
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_share_network_list_all_filters(self):
        filters = {
            'name': 'fake-name',
            'project-id': '1234',
            'created-since': '2001-01-01',
            'created-before': '2002-02-02',
            'neutron-net-id': 'fake-net',
            'neutron-subnet-id': 'fake-subnet',
            'network-type': 'local',
            'segmentation-id': '5678',
            'cidr': 'fake-cidr',
            'ip-version': '4',
            'offset': 10,
            'limit': 20,
        }
        command_str = 'share-network-list'
        for key, value in six.iteritems(filters):
            command_str += ' --%(key)s=%(value)s' % {'key': key,
                                                     'value': value}
        self.run_command(command_str)
        query = parse.urlencode(sorted([(k.replace('-', '_'), v) for (k, v)
                                        in list(filters.items())]))
        self.assert_called(
            'GET',
            '/share-networks/detail?%s' % query,
        )
        cliutils.print_list.assert_called_once_with(
            mock.ANY,
            fields=['id', 'name'])

    def test_share_network_security_service_add(self):
        self.run_command('share-network-security-service-add fake_share_nw '
                         'fake_security_service')
        self.assert_called(
            'POST',
            '/share-networks/1234/action',
        )

    def test_share_network_security_service_remove(self):
        self.run_command('share-network-security-service-remove fake_share_nw '
                         'fake_security_service')
        self.assert_called(
            'POST',
            '/share-networks/1234/action',
        )

    def test_share_network_security_service_list_by_name(self):
        self.run_command('share-network-security-service-list fake_share_nw')
        self.assert_called(
            'GET',
            '/security-services/detail?share_network_id=1234',
        )

    def test_share_network_security_service_list_by_name_not_found(self):
        self.assertRaises(
            exceptions.CommandError,
            self.run_command,
            'share-network-security-service-list inexistent_share_nw',
        )

    def test_share_network_security_service_list_by_name_multiple(self):
        self.assertRaises(
            exceptions.CommandError,
            self.run_command,
            'share-network-security-service-list duplicated_name',
        )

    def test_share_network_security_service_list_by_id(self):
        self.run_command('share-network-security-service-list 1111')
        self.assert_called(
            'GET',
            '/security-services/detail?share_network_id=1111',
        )

    def test_share_server_delete(self):
        self.run_command('share-server-delete 1234')
        self.assert_called('DELETE', '/share-servers/1234')

    def test_create_share(self):
        # Use only required fields
        self.run_command("create nfs 1")
        self.assert_called("POST", "/shares", body=self.create_share_body)

    def test_create_public_share(self):
        expected = self.create_share_body.copy()
        expected['share']['is_public'] = True
        self.run_command("create --public nfs 1")
        self.assert_called("POST", "/shares", body=expected)

    def test_create_with_share_network(self):
        # Except required fields added share network
        sn = "fake-share-network"
        with mock.patch.object(shell_v1, "_find_share_network",
                               mock.Mock(return_value=sn)):
            self.run_command("create nfs 1 --share-network %s" % sn)
            expected = self.create_share_body.copy()
            expected['share']['share_network_id'] = sn
            self.assert_called("POST", "/shares", body=expected)
            shell_v1._find_share_network.assert_called_once_with(mock.ANY, sn)

    def test_create_with_metadata(self):
        # Except required fields added metadata
        self.run_command("create nfs 1 --metadata key1=value1 key2=value2")
        expected = self.create_share_body.copy()
        expected['share']['metadata'] = {"key1": "value1", "key2": "value2"}
        self.assert_called("POST", "/shares", body=expected)

    def test_allow_access_cert(self):
        self.run_command("access-allow 1234 cert client.example.com")

        expected = {
            "os-allow_access": {
                "access_type": "cert",
                "access_to": "client.example.com",
            }
        }
        self.assert_called("POST", "/shares/1234/action", body=expected)

    def test_allow_access_cert_error_gt64(self):
        common_name = 'x' * 65
        self.assertRaises(exceptions.CommandError, self.run_command,
                          ("access-allow 1234 cert %s" % common_name))

    def test_allow_access_cert_error_zero(self):
        cmd = mock.Mock()
        cmd.split = mock.Mock(side_effect=lambda: ['access-allow', '1234',
                                                   'cert', ''])

        self.assertRaises(exceptions.CommandError, self.run_command, cmd)

        cmd.split.assert_called_once_with()

    def test_allow_access_cert_error_whitespace(self):
        cmd = mock.Mock()
        cmd.split = mock.Mock(side_effect=lambda: ['access-allow', '1234',
                                                   'cert', ' '])

        self.assertRaises(exceptions.CommandError, self.run_command, cmd)

        cmd.split.assert_called_once_with()

    def test_allow_access_with_access_level(self):
        aliases = ['--access_level', '--access-level']
        expected = {
            "os-allow_access": {
                "access_type": "ip",
                "access_to": "10.0.0.6",
                "access_level": "ro",
            }
        }

        for alias in aliases:
            for s in self.separators:
                self.run_command(
                    "access-allow " + alias + s + "ro 1111 ip 10.0.0.6")
                self.assert_called("POST", "/shares/1111/action",
                                   body=expected)

    def test_allow_access_with_valid_access_levels(self):
        expected = {
            "os-allow_access": {
                "access_type": "ip",
                "access_to": "10.0.0.6",
            }
        }

        for level in ['rw', 'ro']:
            expected["os-allow_access"]['access_level'] = level
            self.run_command(
                "access-allow --access-level " + level + " 1111 ip 10.0.0.6")
            self.assert_called("POST", "/shares/1111/action",
                               body=expected)

    def test_allow_access_with_invalid_access_level(self):
        self.assertRaises(SystemExit, self.run_command,
                          "access-allow --access-level fake 1111 ip 10.0.0.6")

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_access_list(self):
        self.run_command("access-list 1111")
        cliutils.print_list.assert_called_with(
            mock.ANY,
            ['id', 'access type', 'access to', 'access level', 'state'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_security_service_list(self):
        self.run_command('security-service-list')
        self.assert_called(
            'GET',
            '/security-services',
        )
        cliutils.print_list.assert_called_once_with(
            mock.ANY,
            fields=['id', 'name', 'status', 'type'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    @mock.patch.object(shell_v1, '_find_share_network', mock.Mock())
    def test_security_service_list_filter_share_network(self):
        class FakeShareNetwork:
            id = 'fake-sn-id'
        sn = FakeShareNetwork()
        shell_v1._find_share_network.return_value = sn
        for command in ['--share-network', '--share_network']:
            self.run_command('security-service-list %(command)s %(sn_id)s' %
                             {'command': command,
                              'sn_id': sn.id})
            self.assert_called(
                'GET',
                '/security-services?share_network_id=%s' % sn.id,
            )
            shell_v1._find_share_network.assert_called_with(mock.ANY, sn.id)
            cliutils.print_list.assert_called_with(
                mock.ANY,
                fields=['id', 'name', 'status', 'type'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_security_service_list_detailed(self):
        self.run_command('security-service-list --detailed')
        self.assert_called(
            'GET',
            '/security-services/detail',
        )
        cliutils.print_list.assert_called_once_with(
            mock.ANY,
            fields=['id', 'name', 'status', 'type', 'share_networks'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_security_service_list_all_tenants(self):
        self.run_command('security-service-list --all-tenants')
        self.assert_called(
            'GET',
            '/security-services?all_tenants=1',
        )
        cliutils.print_list.assert_called_once_with(
            mock.ANY,
            fields=['id', 'name', 'status', 'type'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_security_service_list_all_filters(self):
        filters = {
            'status': 'new',
            'name': 'fake-name',
            'type': 'ldap',
            'user': 'fake-user',
            'dns-ip': '1.1.1.1',
            'server': 'fake-server',
            'domain': 'fake-domain',
            'offset': 10,
            'limit': 20,
        }
        command_str = 'security-service-list'
        for key, value in six.iteritems(filters):
            command_str += ' --%(key)s=%(value)s' % {'key': key,
                                                     'value': value}
        self.run_command(command_str)
        self.assert_called(
            'GET',
            '/security-services?dns_ip=1.1.1.1&domain=fake-domain&limit=20'
            '&name=fake-name&offset=10&server=fake-server&status=new'
            '&type=ldap&user=fake-user',
        )
        cliutils.print_list.assert_called_once_with(
            mock.ANY,
            fields=['id', 'name', 'status', 'type'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_security_service_list_filter_by_dns_ip_alias(self):
        self.run_command('security-service-list --dns_ip 1.1.1.1')
        self.assert_called(
            'GET',
            '/security-services?dns_ip=1.1.1.1',
        )
        cliutils.print_list.assert_called_once_with(
            mock.ANY,
            fields=['id', 'name', 'status', 'type'])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_pool_list(self):
        self.run_command('pool-list')
        self.assert_called(
            'GET',
            '/scheduler-stats/pools?backend=.%2A&host=.%2A&pool=.%2A',
        )
        cliutils.print_list.assert_called_with(
            mock.ANY,
            fields=["Name", "Host", "Backend", "Pool"])

    @mock.patch.object(cliutils, 'print_list', mock.Mock())
    def test_pool_list_with_filters(self):
        self.run_command(
            'pool-list --host host1 --backend backend1 --pool pool1')
        self.assert_called(
            'GET',
            '/scheduler-stats/pools?backend=backend1&host=host1&pool=pool1',
        )
        cliutils.print_list.assert_called_with(
            mock.ANY,
            fields=["Name", "Host", "Backend", "Pool"])
