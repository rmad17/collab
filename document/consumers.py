#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Consumer file for channels
"""
import json
import logging
from django.http import HttpResponse
from channels import Channel
from channels.handler import AsgiHandler
from channels.sessions import channel_session

log = logging.getLogger(__name__)


def ws_consumer(message):
    """
    # From Channels Docs
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Hello world! You asked for %s" %
                            message.content.get('path'))
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
    """
    message.reply_channel.send({
        'text': message.content.get('text'),
    })


@channel_session
def ws_connect(message):
    message.reply_channel.send({
        "text": json.dumps({
            "action": "reply_channel",
            "reply_channel": message.reply_channel.name,
        })
    })


@channel_session
def ws_receive(message):
    try:
        data = json.loads(message.get('text'))
        print('d:', data)
    except ValueError:
        log.debug("ws message isn't json text=%s", message.get('text'))
        return
    if data:
        reply_channel = message.reply_channel.name
    print('reply_channel:', reply_channel)
    # Tell client task has been started
    Channel(reply_channel).send({
        "text": json.dumps({
            "action": "saved",
            "text": "text0",
        })
    })
