# Copyright (c) 2015 Uber Technologies, Inc.
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

from __future__ import absolute_import

import pytest
from mock import MagicMock

from tchannel.event import EventEmitter
from tchannel.event import EventRegistrar
from tchannel.event import EventType


@pytest.mark.parametrize('event_name', EventType._fields)
def test_event_hook(event_name):
    event_value = getattr(EventType, event_name)
    mock_hook = MagicMock()

    event_emitter = EventEmitter()
    event_emitter.register_hook(mock_hook)

    event_emitter.fire(event_value, None)
    assert getattr(mock_hook, event_name).called is True


def test_decorator_registration():
    event_emitter = EventEmitter()
    registrar = EventRegistrar(event_emitter)

    called = [False]

    @registrar.before_send_request
    def foo():
        called[0] = True

    event_emitter.fire(EventType.before_send_request)
    assert called[0] is True
