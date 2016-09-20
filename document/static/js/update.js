/*
 * update.js
 * Copyright (C) 2016 rmad17 <souravbasu17@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */
window.onload = function() {
    // Create a new WebSocket
    ws = new WebSocket((window.location.protocol == 'http') ? 'ws://' : 'wss://' +  window.location.host + '/')
    // Make it show an alert when a message is received
    ws.onmessage = function(message) {
      alert(message.data);
    }
    // Send a new message when the WebSocket opens
    ws.onopen = function() {
      ws.send('Hello, world');
    }
    for (var i = 0; i < 3; ++i) {
        var ws = new WebSocket((window.location.protocol == 'http') ? 'ws://' : 'wss://' +  window.location.host + '/')
        ws.id = i;
        ws.onmessage = function(message) {
            console.log('W' + this.id + ': ' + message.data);
        }
        ws.onopen = function() {
            this.send('Hello, world');
        }
    }
};
