var http = require('http');

function getResponses(callback) {
    for(var i=2; i<process.argv.length; i++) {
        callback(process.argv[i], i-2);
    }
}

function getResponse(url, index) {
    var body = '';
    http.get(url, function(response) {
        //encodes response object to be a string
        response.setEncoding("utf8");
        //while getting the data, append to the body string
        response.on("data", function(data){
            body += data;
        });
        response.on("end", function() {
            //when the request is over, log the length and the body
            console.log(body);
        });
        response.on("error", function(err){
            console.log(err);
        });
    });
}

getResponses(getResponse)
