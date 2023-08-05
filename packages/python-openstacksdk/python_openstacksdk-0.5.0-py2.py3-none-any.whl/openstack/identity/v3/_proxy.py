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

from openstack.identity.v3 import credential
from openstack.identity.v3 import domain
from openstack.identity.v3 import endpoint
from openstack.identity.v3 import group
from openstack.identity.v3 import policy
from openstack.identity.v3 import project
from openstack.identity.v3 import service
from openstack.identity.v3 import trust
from openstack.identity.v3 import user
from openstack import proxy


class Proxy(proxy.BaseProxy):

    def create_credential(self, **attrs):
        """Create a new credential from attributes

        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.compute.v2.credential.Credential`,
            comprised of the properties on the Credential class.

        :returns: The results of credential creation
        :rtype: :class:`~openstack.compute.v2.credential.Credential`
        """
        return self._create(credential.Credential, **attrs)

    def delete_credential(self, value, ignore_missing=True):
        """Delete a credential

        :param value: The value can be either the ID of a credential or a
               :class:`~openstack.identity.v3.credential.Credential` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the credential does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent credential.

        :returns: ``None``
        """
        self._delete(credential.Credential, value, ignore_missing)

    def find_credential(self, name_or_id):
        """Find a single credential

        :param name_or_id: The name or ID of a credential.
        :returns: One :class:`~openstack.compute.v2.credential.Credential`
                  or None
        """
        return credential.Credential.find(self.session, name_or_id)

    def get_credential(self, value):
        """Get a single credential

        :param value: The value can be the ID of a credential or a
                      :class:`~openstack.identity.v3.credential.Credential`
                      instance.

        :returns: One :class:`~openstack.identity.v3.credential.Credential`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(credential.Credential, value)

    def credentials(self):
        """Retrieve a generator of credentials

        :returns: A generator of credentials instances.
        :rtype: :class:`~openstack.identity.v3.credential.Credential`
        """
        return self._list(credential.Credential)

    def update_credential(self, value, **attrs):
        """Update a credential

        :param value: Either the id of a credential or a
                      :class:`~openstack.compute.v2.credential.Credential`
                      instance.
        :attrs kwargs: The attributes to update on the credential represented
                       by ``value``.

        :returns: The updated credential
        :rtype: :class:`~openstack.compute.v2.credential.Credential`
        """
        return self._update(credential.Credential, value, **attrs)

    def create_domain(self, **attrs):
        """Create a new domain from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.compute.v2.domain.Domain`,
                           comprised of the properties on the Domain class.

        :returns: The results of domain creation
        :rtype: :class:`~openstack.compute.v2.domain.Domain`
        """
        return self._create(domain.Domain, **attrs)

    def delete_domain(self, value, ignore_missing=True):
        """Delete a domain

        :param value: The value can be either the ID of a domain or a
                      :class:`~openstack.identity.v3.domain.Domain` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the domain does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent domain.

        :returns: ``None``
        """
        self._delete(domain.Domain, value, ignore_missing)

    def find_domain(self, name_or_id):
        """Find a single domain

        :param name_or_id: The name or ID of a domain.
        :returns: One :class:`~openstack.compute.v2.domain.Domain` or None
        """
        return domain.Domain.find(self.session, name_or_id)

    def get_domain(self, value):
        """Get a single domain

        :param value: The value can be the ID of a domain or a
                      :class:`~openstack.identity.v3.domain.Domain` instance.

        :returns: One :class:`~openstack.identity.v3.domain.Domain`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(domain.Domain, value)

    def domains(self):
        """Retrieve a generator of domains

        :returns: A generator of domain instances.
        :rtype: :class:`~openstack.identity.v3.domain.Domain`
        """
        return self._list(domain.Domain)

    def update_domain(self, value, **attrs):
        """Update a domain

        :param value: Either the id of a domain or a
                      :class:`~openstack.compute.v2.domain.Domain` instance.
        :attrs kwargs: The attributes to update on the domain represented
                       by ``value``.

        :returns: The updated domain
        :rtype: :class:`~openstack.compute.v2.domain.Domain`
        """
        return self._update(domain.Domain, value, **attrs)

    def create_endpoint(self, **attrs):
        """Create a new endpoint from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.compute.v2.endpoint.Endpoint`,
                           comprised of the properties on the Endpoint class.

        :returns: The results of endpoint creation
        :rtype: :class:`~openstack.compute.v2.endpoint.Endpoint`
        """
        return self._create(endpoint.Endpoint, **attrs)

    def delete_endpoint(self, value, ignore_missing=True):
        """Delete an endpoint

        :param value: The value can be either the ID of an endpoint or a
               :class:`~openstack.identity.v3.endpoint.Endpoint` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the endpoint does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent endpoint.

        :returns: ``None``
        """
        self._delete(endpoint.Endpoint, value, ignore_missing)

    def find_endpoint(self, name_or_id):
        """Find a single endpoint

        :param name_or_id: The name or ID of a endpoint.
        :returns: One :class:`~openstack.compute.v2.endpoint.Endpoint` or None
        """
        return endpoint.Endpoint.find(self.session, name_or_id)

    def get_endpoint(self, value):
        """Get a single endpoint

        :param value: The value can be the ID of an endpoint or a
                      :class:`~openstack.identity.v3.endpoint.Endpoint`
                      instance.

        :returns: One :class:`~openstack.identity.v3.endpoint.Endpoint`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(endpoint.Endpoint, value)

    def endpoints(self):
        """Retrieve a generator of endpoints

        :returns: A generator of endpoint instances.
        :rtype: :class:`~openstack.identity.v3.endpoint.Endpoint`
        """
        return self._list(endpoint.Endpoint)

    def update_endpoint(self, value, **attrs):
        """Update a endpoint

        :param value: Either the id of a endpoint or a
                      :class:`~openstack.compute.v2.endpoint.Endpoint`
                      instance.
        :attrs kwargs: The attributes to update on the endpoint represented
                       by ``value``.

        :returns: The updated endpoint
        :rtype: :class:`~openstack.compute.v2.endpoint.Endpoint`
        """
        return self._update(endpoint.Endpoint, value, **attrs)

    def create_group(self, **attrs):
        """Create a new group from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.compute.v2.group.Group`,
                           comprised of the properties on the Group class.

        :returns: The results of group creation
        :rtype: :class:`~openstack.compute.v2.group.Group`
        """
        return self._create(group.Group, **attrs)

    def delete_group(self, value, ignore_missing=True):
        """Delete a group

        :param value: The value can be either the ID of a group or a
                      :class:`~openstack.identity.v3.group.Group` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the group does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent group.

        :returns: ``None``
        """
        self._delete(group.Group, value, ignore_missing)

    def find_group(self, name_or_id):
        """Find a single group

        :param name_or_id: The name or ID of a group.
        :returns: One :class:`~openstack.compute.v2.group.Group` or None
        """
        return group.Group.find(self.session, name_or_id)

    def get_group(self, value):
        """Get a single group

        :param value: The value can be the ID of a group or a
                      :class:`~openstack.identity.v3.group.Group`
                      instance.

        :returns: One :class:`~openstack.identity.v3.group.Group`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(group.Group, value)

    def groups(self):
        """Retrieve a generator of groups

        :returns: A generator of group instances.
        :rtype: :class:`~openstack.identity.v3.group.Group`
        """
        return self._list(group.Group)

    def update_group(self, value, **attrs):
        """Update a group

        :param value: Either the id of a group or a
                      :class:`~openstack.compute.v2.group.Group` instance.
        :attrs kwargs: The attributes to update on the group represented
                       by ``value``.

        :returns: The updated group
        :rtype: :class:`~openstack.compute.v2.group.Group`
        """
        return self._update(group.Group, value, **attrs)

    def create_policy(self, **attrs):
        """Create a new policy from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.compute.v2.policy.Policy`,
                           comprised of the properties on the Policy class.

        :returns: The results of policy creation
        :rtype: :class:`~openstack.compute.v2.policy.Policy`
        """
        return self._create(policy.Policy, **attrs)

    def delete_policy(self, value, ignore_missing=True):
        """Delete a policy

        :param value: The value can be either the ID of a policy or a
                      :class:`~openstack.identity.v3.policy.Policy` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the policy does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent policy.

        :returns: ``None``
        """
        self._delete(policy.Policy, value, ignore_missing)

    def find_policy(self, name_or_id):
        """Find a single policy

        :param name_or_id: The name or ID of a policy.
        :returns: One :class:`~openstack.compute.v2.policy.Policy` or None
        """
        return policy.Policy.find(self.session, name_or_id)

    def get_policy(self, value):
        """Get a single policy

        :param value: The value can be the ID of a policy or a
                      :class:`~openstack.identity.v3.policy.Policy` instance.

        :returns: One :class:`~openstack.identity.v3.policy.Policy`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(policy.Policy, value)

    def policies(self):
        """Retrieve a generator of policies

        :returns: A generator of policy instances.
        :rtype: :class:`~openstack.identity.v3.policy.Policy`
        """
        return self._list(policy.Policy)

    def update_policy(self, value, **attrs):
        """Update a policy

        :param value: Either the id of a policy or a
                      :class:`~openstack.compute.v2.policy.Policy` instance.
        :attrs kwargs: The attributes to update on the policy represented
                       by ``value``.

        :returns: The updated policy
        :rtype: :class:`~openstack.compute.v2.policy.Policy`
        """
        return self._update(policy.Policy, value, **attrs)

    def create_project(self, **attrs):
        """Create a new project from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.compute.v2.project.Project`,
                           comprised of the properties on the Project class.

        :returns: The results of project creation
        :rtype: :class:`~openstack.compute.v2.project.Project`
        """
        return self._create(project.Project, **attrs)

    def delete_project(self, value, ignore_missing=True):
        """Delete a project

        :param value: The value can be either the ID of a project or a
                      :class:`~openstack.identity.v3.project.Project` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the project does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent project.

        :returns: ``None``
        """
        self._delete(project.Project, value, ignore_missing)

    def find_project(self, name_or_id):
        """Find a single project

        :param name_or_id: The name or ID of a project.
        :returns: One :class:`~openstack.compute.v2.project.Project` or None
        """
        return project.Project.find(self.session, name_or_id)

    def get_project(self, value):
        """Get a single project

        :param value: The value can be the ID of a project or a
                      :class:`~openstack.identity.v3.project.Project` instance.

        :returns: One :class:`~openstack.identity.v3.project.Project`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(project.Project, value)

    def projects(self):
        """Retrieve a generator of projects

        :returns: A generator of project instances.
        :rtype: :class:`~openstack.identity.v3.project.Project`
        """
        return self._list(project.Project)

    def update_project(self, value, **attrs):
        """Update a project

        :param value: Either the id of a project or a
                      :class:`~openstack.compute.v2.project.Project` instance.
        :attrs kwargs: The attributes to update on the project represented
                       by ``value``.

        :returns: The updated project
        :rtype: :class:`~openstack.compute.v2.project.Project`
        """
        return self._update(project.Project, value, **attrs)

    def create_service(self, **attrs):
        """Create a new service from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.compute.v2.service.Service`,
                           comprised of the properties on the Service class.

        :returns: The results of service creation
        :rtype: :class:`~openstack.compute.v2.service.Service`
        """
        return self._create(service.Service, **attrs)

    def delete_service(self, value, ignore_missing=True):
        """Delete a service

        :param value: The value can be either the ID of a service or a
                      :class:`~openstack.identity.v3.service.Service` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the service does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent service.

        :returns: ``None``
        """
        self._delete(service.Service, value, ignore_missing)

    def find_service(self, name_or_id):
        """Find a single service

        :param name_or_id: The name or ID of a service.
        :returns: One :class:`~openstack.compute.v2.service.Service` or None
        """
        return service.Service.find(self.session, name_or_id)

    def get_service(self, value):
        """Get a single service

        :param value: The value can be the ID of a service or a
                      :class:`~openstack.identity.v3.service.Service` instance.

        :returns: One :class:`~openstack.identity.v3.service.Service`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(service.Service, value)

    def services(self):
        """Retrieve a generator of services

        :returns: A generator of service instances.
        :rtype: :class:`~openstack.identity.v3.service.Service`
        """
        return self._list(service.Service)

    def update_service(self, value, **attrs):
        """Update a service

        :param value: Either the id of a service or a
                      :class:`~openstack.compute.v2.service.Service` instance.
        :attrs kwargs: The attributes to update on the service represented
                       by ``value``.

        :returns: The updated service
        :rtype: :class:`~openstack.compute.v2.service.Service`
        """
        return self._update(service.Service, value, **attrs)

    def create_user(self, **attrs):
        """Create a new user from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.compute.v2.user.User`,
                           comprised of the properties on the User class.

        :returns: The results of user creation
        :rtype: :class:`~openstack.compute.v2.user.User`
        """
        return self._create(user.User, **attrs)

    def delete_user(self, value, ignore_missing=True):
        """Delete a user

        :param value: The value can be either the ID of a user or a
                      :class:`~openstack.identity.v3.user.User` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the user does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent user.

        :returns: ``None``
        """
        self._delete(user.User, value, ignore_missing)

    def find_user(self, name_or_id):
        """Find a single user

        :param name_or_id: The name or ID of a user.
        :returns: One :class:`~openstack.compute.v2.user.User` or None
        """
        return user.User.find(self.session, name_or_id)

    def get_user(self, value):
        """Get a single user

        :param value: The value can be the ID of a user or a
                      :class:`~openstack.identity.v3.user.User` instance.

        :returns: One :class:`~openstack.identity.v3.user.User`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(user.User, value)

    def users(self):
        """Retrieve a generator of users

        :returns: A generator of user instances.
        :rtype: :class:`~openstack.identity.v3.user.User`
        """
        return self._list(user.User)

    def update_user(self, value, **attrs):
        """Update a user

        :param value: Either the id of a user or a
                      :class:`~openstack.compute.v2.user.User` instance.
        :attrs kwargs: The attributes to update on the user represented
                       by ``value``.

        :returns: The updated user
        :rtype: :class:`~openstack.compute.v2.user.User`
        """
        return self._update(user.User, value, **attrs)

    def create_trust(self, **attrs):
        """Create a new trust from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.compute.v2.trust.Trust`,
                           comprised of the properties on the Trust class.

        :returns: The results of trust creation
        :rtype: :class:`~openstack.compute.v2.trust.Trust`
        """
        return self._create(trust.Trust, **attrs)

    def delete_trust(self, value, ignore_missing=True):
        self._delete(trust.Trust, value, ignore_missing)

    def find_trust(self, name_or_id):
        """Find a single trust

        :param name_or_id: The name or ID of a trust.
        :returns: One :class:`~openstack.compute.v2.trust.Trust` or None
        """
        return trust.Trust.find(self.session, name_or_id)

    def get_trust(self, value):
        """Get a single trust

        :param value: The value can be the ID of a trust or a
                      :class:`~openstack.identity.v3.trust.Trust` instance.

        :returns: One :class:`~openstack.identity.v3.trust.Trust`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(trust.Trust, value)

    def trusts(self):
        """Retrieve a generator of trusts

        :returns: A generator of trust instances.
        :rtype: :class:`~openstack.identity.v3.trust.Trust`
        """
        return self._list(trust.Trust)

    def update_trust(self, value, **attrs):
        """Update a trust

        :param value: Either the id of a trust or a
                      :class:`~openstack.compute.v2.trust.Trust` instance.
        :attrs kwargs: The attributes to update on the trust represented
                       by ``value``.

        :returns: The updated trust
        :rtype: :class:`~openstack.compute.v2.trust.Trust`
        """
        return self._update(trust.Trust, value, **attrs)
