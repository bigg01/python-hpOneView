# -*- coding: utf-8 -*-

"""
search.py
~~~~~~~~~~~~

This module implements search HPE OneView REST API
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from future import standard_library

standard_library.install_aliases()

__title__ = 'search'
__version__ = '0.0.1'
__copyright__ = '(C) Copyright (2012-2015) Hewlett Packard Enterprise ' \
                ' Development LP'
__license__ = 'MIT'
__status__ = 'Development'

###
# (C) Copyright (2012-2015) Hewlett Packard Enterprise Development LP
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

from hpOneView.common import get_members, uri


class search(object):
    def __init__(self, con):
        self._con = con

    ###########################################################################
    # Get Resources
    ###########################################################################
    def get_resources(self, query=''):
        if type(query) is dict:
            sQuery = ''
            for key in query:
                sQuery = sQuery + key + '=' + query[key] + '&'
        else:
            sQuery = query
        body = self._con.get(uri['resource'] + '?' + sQuery)
        return get_members(body)

    def get_associations(self, query=''):
        if type(query) is dict:
            sQuery = ''
            for key in query:
                sQuery = sQuery + key + '=' + query[key] + '&'
        else:
            sQuery = query
        body = self._con.get(uri['association'] + '?' + sQuery)
        return get_members(body)

    def get_trees(self, query=''):
        if type(query) is dict:
            sQuery = ''
            for key in query:
                sQuery = sQuery + key + '=' + query[key] + '&'
        else:
            sQuery = query
        body = self._con.get(uri['tree'] + '?' + sQuery)
        return get_members(body)

    def get_search_suggestions(self, query):
        if type(query) is dict:
            sQuery = ''
            for key in query:
                sQuery = sQuery + key + '=' + query[key] + '&'
        else:
            sQuery = query
        body = self._con.get(uri['search-suggestion'] + '?userQuery=' + sQuery)
        return body

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
