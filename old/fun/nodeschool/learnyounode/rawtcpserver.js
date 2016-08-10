var net = require('net');

var port = process.argv[2];
var date = new Date();
var server = net.createServer(function(socket) {
    //data = date.getFullYear()+"-"+date.getMonth()+"-"+date.getDay()+" "+date.getHours()+":"+date.getMinutes()
    data = "2015-08-20 14:01\n";
    socket.end(data);
});
server.listen(port);
