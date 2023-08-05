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

from openstack import exceptions
from openstack import resource


# The _check_resource decorator is used on BaseProxy methods to ensure that
# the `actual` argument is in fact the type of the `expected` argument.
# It does so under two cases:
# 1. When strict=False, if and only if `actual` is a Resource instance,
#    it is checked to see that it's an instance of the `expected` class.
#    This allows `actual` to be other types, such as strings, when it makes
#    sense to accept a raw id value.
# 2. When strict=True, `actual` must be an instance of the `expected` class.
def _check_resource(strict=False):
    def wrap(method):
        def check(self, expected, actual=None, *args, **kwargs):
            if (strict and actual is not None and not
               isinstance(actual, resource.Resource)):
                raise ValueError("A %s must be passed" % expected.__name__)
            elif (isinstance(actual, resource.Resource) and not
                  isinstance(actual, expected)):
                raise ValueError("Expected %s but received %s" % (
                                 expected.__name__, actual.__class__.__name__))

            return method(self, expected, actual, *args, **kwargs)
        return check
    return wrap


class BaseProxy(object):

    def __init__(self, session):
        self.session = session

    @_check_resource(strict=False)
    def _delete(self, resource_type, value, ignore_missing=True):
        """Delete a resource

        :param resource_type: The type of resource to delete. This should
                              be a :class:`~openstack.resource.Resource`
                              subclass with a ``from_id`` method.
        :param value: The value to delete. Can be either the ID of a
                      resource or a :class:`~openstack.resource.Resource`
                      subclass.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent server.

        :returns: The result of the ``delete``
        :raises: ``ValueError`` if ``value`` is a
                 :class:`~openstack.resource.Resource` that doesn't match
                 the ``resource_type``.
                 :class:`~openstack.exceptions.ResourceNotFound` when
                 ignore_missing if ``False`` and a nonexistent resource
                 is attempted to be deleted.

        """
        res = resource_type.existing(id=resource.Resource.get_id(value))

        try:
            rv = res.delete(self.session)
        except exceptions.NotFoundException as exc:
            if ignore_missing:
                return None
            else:
                # Reraise with a more specific type and message
                raise exceptions.ResourceNotFound(
                    "No %s found for %s" % (resource_type.__name__, value),
                    details=exc.details, status_code=exc.status_code)

        return rv

    @_check_resource(strict=False)
    def _update(self, resource_type, value, **attrs):
        """Update a resource

        :param resource_type: The type of resource to update.
        :type resource_type: :class:`~openstack.resource.Resource`
        :param value: The resource to update. This must either be a
                      :class:`~openstack.resource.Resource` or an id
                      that corresponds to a resource.
        :param **attrs: Attributes to update on a Resource object.
                        These attributes will be used in conjunction with
                        ``resource_type``.

        :returns: The result of the ``update``
        :rtype: :class:`~openstack.resource.Resource`
        """
        res = resource_type.existing(id=resource.Resource.get_id(value))
        res.update_attrs(attrs)
        return res.update(self.session)

    def _create(self, resource_type, **attrs):
        """Create a resource from attributes

        :param resource_type: The type of resource to create.
        :type resource_type: :class:`~openstack.resource.Resource`
        :param **attrs: Attributes from which to create a Resource object.
                        These attributes will be used in conjunction with
                        ``resource_type``.

        :returns: The result of the ``create``
        :rtype: :class:`~openstack.resource.Resource`
        """
        res = resource_type.new(**attrs)
        return res.create(self.session)

    @_check_resource(strict=False)
    def _get(self, resource_type, value):
        """Get a resource

        :param resource_type: The type of resource to get.
        :type resource_type: :class:`~openstack.resource.Resource`
        :param value: The value to get. Can be either the ID of a
                      resource or a :class:`~openstack.resource.Resource`
                      subclass.

        :returns: The result of the ``get``
        :rtype: :class:`~openstack.resource.Resource`
        """

        res = resource_type.existing(id=resource.Resource.get_id(value))
        try:
            return res.get(self.session)
        except exceptions.NotFoundException as exc:
            raise exceptions.ResourceNotFound(
                "No %s found for %s" % (resource_type.__name__, value),
                details=exc.details, status_code=exc.status_code)

    def _list(self, resource_type, paginated=False, **query):
        """List a resource

        :param resource_type: The type of resource to delete. This should
                              be a :class:`~openstack.resource.Resource`
                              subclass with a ``from_id`` method.
        :param bool paginated: When set to ``False``, expect all of the data
                               to be returned in one response. When set to
                               ``True``, the resource supports data being
                               returned across multiple pages.
        :param kwargs **query: Keyword arguments that are sent to the list
                               method, which are then attached as query
                               parameters on the request URL.

        :returns: A generator of Resource objects.
        :raises: ``ValueError`` if ``value`` is a
                 :class:`~openstack.resource.Resource` that doesn't match
                 the ``resource_type``.
        """
        query = resource_type._convert_ids(query)
        return resource_type.list(self.session, paginated=paginated, **query)

    def _head(self, resource_type, value=None):
        """Retrieve a resource's header

        :param resource_type: The type of resource to retrieve.
        :type resource_type: :class:`~openstack.resource.Resource`
        :param value: The value of a specific resource to retreive headers
                      for. Can be either the ID of a resource,
                      a :class:`~openstack.resource.Resource` subclass,
                      or ``None``.

        :returns: The result of the ``head`` call
        :rtype: :class:`~openstack.resource.Resource`
        """
        if value is not None:
            res = resource_type.existing(id=resource.Resource.get_id(value))
        else:
            res = resource_type()

        return res.head(self.session)
