# Copyright (C) 2012-2015 by the Free Software Foundation, Inc.
#
# This file is part of GNU Mailman.
#
# GNU Mailman is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# GNU Mailman is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# GNU Mailman.  If not, see <http://www.gnu.org/licenses/>.

"""REST API for held message moderation."""

__all__ = [
    'HeldMessage',
    'HeldMessages',
    ]


from mailman.app.moderator import handle_message
from mailman.interfaces.action import Action
from mailman.interfaces.messages import IMessageStore
from mailman.interfaces.requests import IListRequests, RequestType
from mailman.rest.helpers import (
    CollectionMixin, bad_request, child, etag, no_content, not_found, okay)
from mailman.rest.validator import Validator, enum_validator
from zope.component import getUtility



class _ModerationBase:
    """Common base class."""

    def _make_resource(self, request_id):
        requests = IListRequests(self._mlist)
        results = requests.get_request(request_id)
        if results is None:
            return None
        key, data = results
        resource = dict(key=key, request_id=request_id)
        # Flatten the IRequest payload into the JSON representation.
        resource.update(data)
        # Check for a matching request type, and insert the type name into the
        # resource.
        request_type = RequestType[resource.pop('_request_type')]
        if request_type is not RequestType.held_message:
            return None
        resource['type'] = RequestType.held_message.name
        # This key isn't what you think it is.  Usually, it's the Pendable
        # record's row id, which isn't helpful at all.  If it's not there,
        # that's fine too.
        resource.pop('id', None)
        return resource



class _HeldMessageBase(_ModerationBase):
    """Held messages are a little different."""

    def _make_resource(self, request_id):
        resource = super(_HeldMessageBase, self)._make_resource(request_id)
        if resource is None:
            return None
        # Grab the message and insert its text representation into the
        # resource.  XXX See LP: #967954
        key = resource.pop('key')
        msg = getUtility(IMessageStore).get_message_by_id(key)
        resource['msg'] = msg.as_string()
        # Some of the _mod_* keys we want to rename and place into the JSON
        # resource.  Others we can drop.  Since we're mutating the dictionary,
        # we need to make a copy of the keys.  When you port this to Python 3,
        # you'll need to list()-ify the .keys() dictionary view.
        for key in list(resource):
            if key in ('_mod_subject', '_mod_hold_date', '_mod_reason',
                       '_mod_sender', '_mod_message_id'):
                resource[key[5:]] = resource.pop(key)
            elif key.startswith('_mod_'):
                del resource[key]
        # Also, held message resources will always be this type, so ignore
        # this key value.
        del resource['type']
        return resource


class HeldMessage(_HeldMessageBase):
    """Resource for moderating a held message."""

    def __init__(self, mlist, request_id):
        self._mlist = mlist
        self._request_id = request_id

    def on_get(self, request, response):
        try:
            request_id = int(self._request_id)
        except ValueError:
            bad_request(response)
            return
        resource = self._make_resource(request_id)
        if resource is None:
            not_found(response)
        else:
            okay(response, etag(resource))

    def on_post(self, request, response):
        try:
            validator = Validator(action=enum_validator(Action))
            arguments = validator(request)
        except ValueError as error:
            bad_request(response, str(error))
            return
        requests = IListRequests(self._mlist)
        try:
            request_id = int(self._request_id)
        except ValueError:
            bad_request(response)
            return
        results = requests.get_request(request_id, RequestType.held_message)
        if results is None:
            not_found(response)
        else:
            handle_message(self._mlist, request_id, **arguments)
            no_content(response)



class HeldMessages(_HeldMessageBase, CollectionMixin):
    """Resource for messages held for moderation."""

    def __init__(self, mlist):
        self._mlist = mlist
        self._requests = None

    def _resource_as_dict(self, request):
        """See `CollectionMixin`."""
        return self._make_resource(request.id)

    def _get_collection(self, request):
        requests = IListRequests(self._mlist)
        self._requests = requests
        return list(requests.of_type(RequestType.held_message))

    def on_get(self, request, response):
        """/lists/listname/held"""
        resource = self._make_collection(request)
        okay(response, etag(resource))

    @child(r'^(?P<id>[^/]+)')
    def message(self, request, segments, **kw):
        return HeldMessage(self._mlist, kw['id'])
