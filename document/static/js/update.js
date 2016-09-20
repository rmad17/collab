/*
 * update.js
 * Copyright (C) 2016 rmad17 <souravbasu17@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */
window.onload = function() {
};

// Create a new WebSocket
ws = new WebSocket((window.location.protocol == 'http') ? 'ws://' : 'ws://' +  window.location.host + '/doc/update/');
console.log(ws);
// Make it show an alert when a message is received
ws.onmessage = function(message) {
  alert(message.data);
}
// Send a new message when the WebSocket opens
ws.onopen = function() {
  ws.send('Hello, world');
}
