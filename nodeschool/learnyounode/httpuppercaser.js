var http = require('http');
var port = process.argv[2];


var server = http.createServer(function(req, res) {
    //req.pipe(res);
    if(req.method == 'POST') {
        var body = '';
        req.on("data", function(data) {
            body += data.toString().toUpperCase(); 
            //console.log(data.toString().toUpperCase());
        });
        req.on("end", function(data) {
            res.end(body);
        });
    }
});
server.listen(port);
