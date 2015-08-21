var http = require('http');
var url = require('url');
var port = process.argv[2];


var server = http.createServer(function(req, res) {
    //req.pipe(res);
    if(req.method == 'GET') {
        var urlPath = url.parse(req.url).pathname;
        var queryVars = url.parse(req.url, true).query;

        if(queryVars.iso && urlPath === '/api/parsetime') {
            var date = new Date(queryVars.iso);
            var dateObj = {
                "hour": date.getHours(),
                "minute":date.getMinutes(),
                "second": date.getSeconds()
            };
            res.writeHead(200, {'Content-Type': 'application/json'});
            res.end(JSON.stringify(dateObj));
        }
        else if(queryVars.iso && urlPath === '/api/unixtime') {
            var unixTime = Date.parse(queryVars.iso);
            var dateObj = {
                "unixtime": unixTime
            };
            res.writeHead(200, {'Content-Type': 'application/json'});
            res.end(JSON.stringify(dateObj));
        }
    }
    else{
        var error = {"error": "Bad Request"};
        res.end(JSON.stringify(error));
    }
});

server.listen(port);
