# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Routing for channels
"""

# In routing.py
from channels.routing import route
from document import consumers

channel_routing = [
    # route("http.request", "document.consumers.http_consumer"),
    # route("websocket.receive", consumers.ws_consumer,
    #      path=r'^/doc/update/$'),
    route("websocket.connect", consumers.ws_connect),
    route("websocket.receive", consumers.ws_receive),
]
