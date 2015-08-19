var http = require('http');
var url = process.argv[2];
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
        console.log(body.length);
        console.log(body);
    });
});
