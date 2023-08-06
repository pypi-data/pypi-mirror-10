# -*- coding: utf-8 -*-

# Copyright 2015 Rackspace
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

import mock
from oslo.config import cfg

from arsenal.director import scheduler
from arsenal.strategy import base as sb
from arsenal.tests import base

CONF = cfg.CONF


def strat_directive_mock():
    return [
        sb.CacheNode('node-a', 'image-a', 'checksum-a'),
        sb.CacheNode('node-b', 'image-b', 'checksum-b'),
        sb.CacheNode('node-c', 'image-c', 'checksum-c'),
        sb.CacheNode('node-d', 'image-d', 'checksum-d'),
        sb.CacheNode('node-e', 'image-e', 'checksum-e'),
        sb.EjectNode('node-f'),
        sb.EjectNode('node-g'),
        sb.EjectNode('node-h'),
        sb.EjectNode('node-i'),
        sb.EjectNode('node-J'),
    ]


class TestScheduler(base.TestCase):

    @mock.patch.object(scheduler.DirectorScheduler, 'periodic_tasks')
    @mock.patch('arsenal.director.onmetal_scout.OnMetalScout')
    def setUp(self, onmetal_scout_mock, periodic_task_mock):
        super(TestScheduler, self).setUp()
        CONF.set_override('scout', 'onmetal_scout.OnMetalScout', 'director')
        CONF.set_override('dry_run', False, 'director')
        self.scheduler = scheduler.DirectorScheduler()
        self.scheduler.strat.directives = strat_directive_mock

    def test_rate_limit_on(self):
        issue_action_mock = mock.MagicMock()
        self.scheduler.scout.issue_action = issue_action_mock

        CONF.set_override('cache_directive_rate_limit', 2, 'director')
        self.scheduler.cache_directive_rate_limiter = (
            scheduler.get_configured_rate_limiter())
        self.assertIsNotNone(self.scheduler.cache_directive_rate_limiter)
        self.scheduler.issue_directives(None)
        # 2 cache node directives, plus 5 eject node directives
        self.assertEqual(7, issue_action_mock.call_count)

    def test_rate_limit_off(self):
        issue_action_mock = mock.MagicMock()
        self.scheduler.scout.issue_action = issue_action_mock

        CONF.set_override('cache_directive_rate_limit', 0, 'director')
        self.scheduler.cache_directive_rate_limiter = (
            scheduler.get_configured_rate_limiter())
        self.assertIsNone(self.scheduler.cache_directive_rate_limiter)
        self.scheduler.issue_directives(None)
        # 5 cache node directives, plus 5 eject node directives
        self.assertEqual(10, issue_action_mock.call_count)

    def test_dry_run_on(self):
        issue_action_mock = mock.MagicMock()
        self.scheduler.scout.issue_action = issue_action_mock

        # Dry-run enabled, so issue_action should not be called on the scout.
        CONF.set_override('dry_run', True, 'director')
        self.scheduler.issue_directives(None)
        self.assertFalse(issue_action_mock.called)

    def test_dry_run_off(self):
        issue_action_mock = mock.MagicMock()
        self.scheduler.scout.issue_action = issue_action_mock

        # Dry-run disabled, so issue_action will be called.
        CONF.set_override('dry_run', False, 'director')
        self.scheduler.issue_directives(None)
        self.assertTrue(issue_action_mock.called)
