# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2016) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from future import standard_library

standard_library.install_aliases()

__title__ = 'storage-volume-templates'
__version__ = '0.0.1'
__copyright__ = '(C) Copyright (2012-2016) Hewlett Packard Enterprise ' \
                ' Development LP'
__license__ = 'MIT'
__status__ = 'Development'

from hpOneView.resources.resource import ResourceClient


class StorageVolumeTemplates(object):
    URI = '/rest/storage-volume-templates'

    def __init__(self, con):
        self._connection = con
        self._client = ResourceClient(con, self.URI)

    def get_all(self, start=0, count=-1, filter='', sort=''):
        """
        Gets a list of storage volume templates.

        Args:
            start:
                The first item to return, using 0-based indexing.
                If not specified, the default is 0 - start with the first available item.
            count:
                The number of resources to return. A count of -1 requests all the items.
                The actual number of items in the response may differ from the requested
                count if the sum of start and count exceed the total number of items.
            filter:
                A general filter/query string to narrow the list of items returned. The
                default is no filter - all resources are returned.
            sort:
                The sort order of the returned data set. By default, the sort order is based
                on create time, with the oldest entry first.

        Returns:
            list: A list of storage volume templates.
        """
        return self._client.get_all(start, count, filter=filter, sort=sort)

    def create(self, resource, timeout=-1):
        """
        Creates a new storage volume template.

        Args:
            resource (dict):
                Object to create.
            timeout:
                Timeout in seconds. Wait task completion by default. The timeout does not abort the operation
                in OneView, just stops waiting for its completion.

        Returns:
            dict: Created storage volume template.
        """
        custom_headers = {'Accept-Language': 'en_US'}
        return self._client.create(resource, timeout=timeout, custom_headers=custom_headers)

    def get(self, id_or_uri):
        """
        Gets the specified storage volume template resource by ID or by uri.

        Args:
            id_or_uri: Could be either the storage volume template id or the storage volume template uri.

        Returns:
            dict: The storage volume template
        """
        return self._client.get(id_or_uri)

    def get_connectable_volume_templates(self):
        """
        Gets the storage volume templates that are available on the specified networks based on the storage system
        port's expected network connectivity. If there are no storage volume templates that meets the specified
        connectivity criteria an empty collection will be returned.

        Returns:
            list: Storage volume templates.
        """
        uri = self.URI + "/connectable-volume-templates"
        return self._client.get(uri)

    def delete(self, resource, force=False, timeout=-1):
        """
        Deletes the specified storage volume template.

        Args:
            resource (dict):
                Object to remove.
            force (bool):
                 If set to true the operation completes despite any problems with
                 network connectivity or errors on the resource itself. The default is false.
            timeout:
                Timeout in seconds. Wait task completion by default. The timeout does not abort the operation
                in OneView, just stops waiting for its completion.
        Returns:
            bool: Indicating if the resource was successfully deleted.
        """
        custom_headers = {'Accept-Language': 'en_US'}
        return self._client.delete(resource, force=force, timeout=timeout, custom_headers=custom_headers)

    def update(self, resource, timeout=-1):
        """
        Updates a storage volume template.

        Args:
            resource (dict):
                Object to update
            timeout:
                Timeout in seconds. Wait task completion by default. The timeout does not abort the operation
                in OneView, just stops waiting for its completion.

        Returns:
            dict: Updated storage volume system
        """
        custom_headers = {'Accept-Language': 'en_US'}
        return self._client.update(resource, timeout=timeout, custom_headers=custom_headers)

    def get_by(self, field, value):
        """
        Get all storage volume templates that match the filter.

        The search is case insensitive.

        Args:
            field: Field name to filter.
            value: Value to filter.

        Returns:
            list: A list of storage volume templates that match the filter.
        """
        return self._client.get_by(field, value)
