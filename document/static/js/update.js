/*
 * update.js
 * Copyright (C) 2016 rmad17 <souravbasu17@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */
// Create a new WebSocket
// Send a new message when the WebSocket opens
//ws.onopen = function() {
//  ws.send('Hello, world');
//}
window.onload = function() {
};

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var ws_path = ws_scheme + '://' + window.location.host + '/doc/update/';
    console.log("Connecting to " + ws_path)
    var ws = new ReconnectingWebSocket(ws_path);
    console.log(ws);
    // Make it show an alert when a message is received
    ws.onmessage = function(message) {
      console.log(message.data);
      console.log(message);
    }
    $('#name').change(function(e){
        var data = {
            'text':'sending_data'
        };
        console.log('text:', data);
        ws.send(JSON.stringify(data));
    });
