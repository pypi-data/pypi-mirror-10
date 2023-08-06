# Copyright 2015 - Mirantis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from oslo_config import cfg

from mistral.db.v2 import api as db_api
from mistral import exceptions as exc
from mistral.services import actions
from mistral.tests.unit.engine import base
from mistral.workflow import states

# Use the set_default method to set value otherwise in certain test cases
# the change in value is not permanent.
cfg.CONF.set_default('auth_enable', False, group='pecan')


class RunActionEngineTest(base.EngineTestCase):
    @classmethod
    def heavy_init(cls):
        super(RunActionEngineTest, cls).heavy_init()

        action = """---
        version: '2.0'

        concat:
          base: std.echo
          base-input:
            output: <% $.left %><% $.right %>
          input:
            - left
            - right
        """
        actions.create_actions(action)

    def tearDown(self):
        super(RunActionEngineTest, self).tearDown()

    def test_run_action_sync(self):
        # Start action and see the result.
        action_ex = self.engine.start_action('std.echo', {'output': 'Hello!'})

        self.assertEqual('Hello!', action_ex.output['result'])

    def test_run_action_async(self):
        # Start action.
        action_ex = self.engine.start_action(
            'std.echo',
            {'output': 'Hello!'},
            save_result=True
        )

        is_action_ex_success = (
            lambda: db_api.get_action_execution(
                action_ex.id
            ).state == states.SUCCESS
        )

        self._await(is_action_ex_success)

        action_ex = db_api.get_action_execution(action_ex.id)

        self.assertEqual(states.SUCCESS, action_ex.state)
        self.assertEqual({'result': 'Hello!'}, action_ex.output)

    def test_run_action_adhoc(self):
        # Start action and see the result.
        action_ex = self.engine.start_action(
            'concat',
            {'left': 'Hello, ', 'right': 'John Doe!'}
        )

        self.assertEqual('Hello, John Doe!', action_ex.output['result'])

    def test_run_action_wrong_input(self):
        # Start action and see the result.
        exception = self.assertRaises(
            exc.InputException,
            self.engine.start_action,
            'std.http',
            {'url': 'Hello, ', 'metod': 'John Doe!'}
        )

        self.assertIn('std.http', exception.message)

    def test_adhoc_action_wrong_input(self):
        # Start action and see the result.
        exception = self.assertRaises(
            exc.InputException,
            self.engine.start_action,
            'concat',
            {'left': 'Hello, ', 'ri': 'John Doe!'}
        )

        self.assertIn('concat', exception.message)
