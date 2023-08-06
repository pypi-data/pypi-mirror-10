# Copyright (c) 2014 NetApp, Inc.
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

from django.core.urlresolvers import reverse
import mock
import unittest

from manila_ui.api import manila as api_manila
from manila_ui.dashboards.project.shares import test_data
from manila_ui.test import helpers as test

from openstack_dashboard import api
from openstack_dashboard.usage import quotas

SHARE_INDEX_URL = reverse('horizon:project:shares:index')


class ShareViewTests(test.TestCase):

    @unittest.skip("broken unit test")
    def test_create_share(self):
        usage_limit = {'maxTotalVolumeGigabytes': 250,
                       'gigabytesUsed': 20,
                       'volumesUsed': 0,
                       'maxTotalVolumes': 6}
        share_net = test_data.active_share_network
        share_nets = [share_net]
        formData = {'name': u'new_share',
                    'description': u'This is test share',
                    'method': u'CreateForm',
                    'share_network': share_net.id,
                    'size': 1,
                    'type': 'NFS'
                    }

        api_manila.share_create = mock.Mock()
        api_manila.share_snapshot_list = mock.Mock(return_value=[])
        api_manila.share_network_list = mock.Mock(return_value=share_nets)
        api_manila.share_type_list = mock.Mock(return_value=[])
        api.neutron.is_service_enabled = mock.Mock(return_value=[True])
        quotas.tenant_limit_usages = mock.Mock(return_value=[usage_limit])
        url = reverse('horizon:project:shares:create')
        self.client.post(url, formData)
        api_manila.share_create.assert_called_with(
            mock.ANY, formData['size'], formData['name'],
            formData['description'], formData['type'], snapshot_id=None,
            share_network_id=share_net.id, metadata={})

    @unittest.skip("broken unit test")
    def test_create_share_from_snapshot(self):
        share_net = test_data.active_share_network
        share_nets = [share_net]
        snapshot = test_data.snapshot
        formData = {'name': u'new_share',
                    'description': u'This is test share from snapshot',
                    'method': u'CreateForm',
                    'share_network': share_net.id,
                    'size': snapshot.size,
                    'type': 'NFS',
                    'share_source_type': 'snapshot',
                    'snapshot': snapshot.id
                    }

        api_manila.share_create = mock.Mock()
        api_manila.share_snapshot_list = mock.Mock(
            return_value=[snapshot])
        api_manila.share_snapshot_get = mock.Mock(
            return_value=snapshot)
        api.neutron.is_service_enabled = mock.Mock(return_value=[True])
        api_manila.share_network_list = mock.Mock(return_value=share_nets)
        url = reverse('horizon:project:shares:create')
        res = self.client.post(url, formData)
        api_manila.share_create.assert_called_with(
            mock.ANY, formData['size'], formData['name'],
            formData['description'], formData['type'],
            snapshot_id=snapshot.id,
            share_network_id=share_net.id, metadata={})
        self.assertRedirectsNoFollow(res, SHARE_INDEX_URL)

    @unittest.skip("broken unit test")
    def test_create_share_from_snapshot_url(self):
        share_net = test_data.active_share_network
        share_nets = [share_net]
        snapshot = test_data.snapshot
        formData = {'name': u'new_share',
                    'description': u'This is test share',
                    'method': u'CreateForm',
                    'share_network': share_net.id,
                    'size': 1,
                    'type': 'NFS'
                    }

        api_manila.share_create = mock.Mock()
        api_manila.share_snapshot_list = mock.Mock(return_value=[])
        api_manila.share_snapshot_get = mock.Mock(
            return_value=snapshot)
        api.neutron.is_service_enabled = mock.Mock(return_value=[True])
        api_manila.share_network_list = mock.Mock(return_value=share_nets)
        url = reverse('horizon:project:shares:create')
        url = url + '?snapshot_id=%s' % snapshot.id
        self.client.post(url, formData)
        api_manila.share_create.assert_called_with(
            mock.ANY, formData['size'], formData['name'],
            formData['description'], formData['type'], snapshot_id=None,
            share_network_id=share_net.id, metadata={})

    @unittest.skip("broken unit test")
    def test_delete_share(self):
        share = test_data.share

        formData = {'action':
                    'shares__delete__%s' % share.id}

        api_manila.share_delete = mock.Mock()
        api_manila.share_get = mock.Mock(
            return_value=test_data.share)
        api_manila.share_list = mock.Mock(
            return_value=[test_data.share])
        url = reverse('horizon:project:shares:index')
        res = self.client.post(url, formData)
        api_manila.share_delete.assert_called_with(
            mock.ANY, test_data.share.id)

        self.assertRedirectsNoFollow(res, SHARE_INDEX_URL)

    def test_detail_view(self):
        share_net = test_data.active_share_network
        share = test_data.share
        rules = [test_data.ip_rule, test_data.user_rule]
        api_manila.share_get = mock.Mock(return_value=share)
        api_manila.share_network_get = mock.Mock(return_value=share_net)
        api_manila.share_rules_list = mock.Mock(return_value=rules)

        url = reverse('horizon:project:shares:detail',
                      args=[share.id])
        res = self.client.get(url)
        self.assertContains(res, "<h1>Share Details: %s</h1>"
                                 % share.name,
                            1, 200)

        self.assertContains(res, "<dd>%s</dd>" % share.name, 1, 200)
        self.assertContains(res, "<dd>%s</dd>" % share.id, 1, 200)
        self.assertContains(res, "<dd>%s GB</dd>" % share.size, 1, 200)
        self.assertContains(res, "<dd>%s</dd>" % share.share_proto, 1, 200)
        for rule in rules:
            self.assertContains(res, "<dt>%s</dt>" % rule.access_type,
                                1, 200)
            self.assertContains(res, "<dd>%s</dd>" % rule.access_to,
                                1, 200)
        self.assertNoMessages()

    def test_update_share(self):
        share = test_data.share

        api_manila.share_get = mock.Mock(return_value=share)
        api_manila.share_update = mock.Mock()

        formData = {'method': 'UpdateForm',
                    'name': share.name,
                    'description': share.description}

        url = reverse('horizon:project:shares:update', args=[share.id])
        res = self.client.post(url, formData)
        self.assertRedirectsNoFollow(res, SHARE_INDEX_URL)

    def test_list_rules(self):
        share = test_data.share
        rules = [test_data.ip_rule, test_data.user_rule]
        api_manila.share_rules_list = mock.Mock(return_value=rules)

        url = reverse('horizon:project:shares:manage_rules', args=[share.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'project/shares/shares/manage_rules.html')

    @unittest.skip("broken unit test")
    def test_create_rule(self):
        share = test_data.share
        url = reverse('horizon:project:shares:rule_add', args=[share.id])
        api_manila.share_get = mock.Mock(return_value=share)
        api_manila.share_allow = mock.Mock()
        api.neutron.is_service_enabled = mock.Mock(return_value=[True])
        formData = {'type': 'user',
                    'method': u'CreateForm',
                    'access_to': 'someuser'}
        res = self.client.post(url, formData)
        api_manila.share_allow.assert_called_once_with(
            mock.ANY, share.id, access_type=formData['type'],
            access=formData['access_to'])
        self.assertRedirectsNoFollow(
            res,
            reverse('horizon:project:shares:manage_rules', args=[share.id]))

    def test_delete_rule(self):
        rule = test_data.ip_rule
        share = test_data.share
        formData = {'action':
                    'rules__delete__%s' % rule.id}

        api_manila.share_deny = mock.Mock()
        api_manila.share_get = mock.Mock(
            return_value=test_data.share)
        api_manila.share_rules_list = mock.Mock(
            return_value=[rule])
        url = reverse('horizon:project:shares:manage_rules', args=[share.id])
        self.client.post(url, formData)
        api_manila.share_deny.assert_called_with(
            mock.ANY, test_data.share.id, rule.id)
