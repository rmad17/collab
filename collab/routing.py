#! /usr/bin/env python
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

channel_routing = [
    # route("http.request", "document.consumers.http_consumer"),
    route("websocket.receive", "document.consumers.ws_consumer"),
]
