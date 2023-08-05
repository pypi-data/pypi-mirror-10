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

import mock

from openstack.tests.unit import base


class TestProxyBase(base.TestCase):
    def setUp(self):
        super(TestProxyBase, self).setUp()
        self.session = mock.MagicMock()

    def _verify(self, mock_method, test_method,
                method_args=None, method_kwargs=None,
                expected_args=None, expected_kwargs=None,
                expected_result=None):
        with mock.patch(mock_method) as mocked:
            mocked.return_value = expected_result
            if any([method_args, method_kwargs,
                    expected_args, expected_kwargs]):
                method_args = method_args or ()
                method_kwargs = method_kwargs or {}
                expected_args = expected_args or ()
                expected_kwargs = expected_kwargs or {}

                self.assertEqual(expected_result, test_method(*method_args,
                                 **method_kwargs))
                mocked.assert_called_with(self.session,
                                          *expected_args, **expected_kwargs)
            else:
                self.assertEqual(expected_result, test_method())
                mocked.assert_called_with(self.session)

    # NOTE(briancurtin): This is a duplicate version of _verify that is
    # temporarily here while we shift APIs. The difference is that
    # calls from the Proxy classes aren't going to be going directly into
    # the Resource layer anymore, so they don't pass in the session which
    # was tested in assert_called_with.
    # This is being done in lieu of adding logic and complicating
    # the _verify method. It will be removed once there is one API to
    # be verifying.
    def _verify2(self, mock_method, test_method,
                 method_args=None, method_kwargs=None,
                 expected_args=None, expected_kwargs=None,
                 expected_result=None):
        with mock.patch(mock_method) as mocked:
            mocked.return_value = expected_result
            if any([method_args, method_kwargs,
                    expected_args, expected_kwargs]):
                method_args = method_args or ()
                method_kwargs = method_kwargs or {}
                expected_args = expected_args or ()
                expected_kwargs = expected_kwargs or {}

                self.assertEqual(expected_result, test_method(*method_args,
                                 **method_kwargs))
                mocked.assert_called_with(*expected_args, **expected_kwargs)
            else:
                self.assertEqual(expected_result, test_method())
                mocked.assert_called_with(self.session)

    def verify_create(self, mock_method, test_method, **kwargs):
        self._verify(mock_method, test_method, expected_result="result",
                     **kwargs)

    def verify_create2(self, mock_method, test_method, **kwargs):
        self._verify2(mock_method, test_method, expected_result="result",
                      **kwargs)

    def verify_delete(self, mock_method, test_method, **kwargs):
        self._verify(mock_method, test_method, **kwargs)

    def verify_delete2(self, resource, method, ignore):
        self._verify2('openstack.proxy.BaseProxy._delete',
                      method,
                      method_args=["resource_or_id"],
                      method_kwargs={"ignore_missing": ignore},
                      expected_args=[resource, "resource_or_id", ignore])

    def verify_get(self, mock_method, test_method, **kwargs):
        self._verify(mock_method, test_method, expected_result="result",
                     **kwargs)

    def verify_get2(self, mock_method, test_method, **kwargs):
        self._verify2(mock_method, test_method, expected_result="result",
                      **kwargs)

    def verify_head(self, resource, method, value=None):
        the_value = [value] if value is not None else []
        self._verify2("openstack.proxy.BaseProxy._head",
                      method,
                      method_args=the_value,
                      expected_args=[resource] + the_value)

    def verify_find(self, mock_method, test_method, **kwargs):
        self._verify(mock_method, test_method, method_args=["name_or_id"],
                     expected_args=["name_or_id"], expected_result="result",
                     **kwargs)

    def verify_list(self, mock_method, test_method, **kwargs):
        self._verify(mock_method, test_method, expected_result=["result"],
                     **kwargs)

    def verify_list2(self, method, **kwargs):
        self._verify2("openstack.proxy.BaseProxy._list",
                      method, expected_result=["result"],
                      **kwargs)

    def verify_update(self, mock_method, test_method, **kwargs):
        self._verify(mock_method, test_method, expected_result="result",
                     **kwargs)

    def verify_update2(self, mock_method, test_method, **kwargs):
        self._verify2(mock_method, test_method, expected_result="result",
                      **kwargs)

    def verify_wait_for_status(self, mock_method, test_method, **kwargs):
        self._verify(mock_method, test_method, **kwargs)
