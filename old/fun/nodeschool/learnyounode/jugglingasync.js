var http = require('http');
var urls = process.argv.slice(2, process.argv.length+1);
var result = [];

function getResponse(url, index, callback) {
    http.get(url, function(response) {
        var body = '';
        //encodes response object to be a string
        response.setEncoding("utf8");
        //while getting the data, append to the body string
        response.on("data", function(data){
            body += data;
        });
        response.on("end", function() {
            //when the request is over, log the length and the body
            //calls the getResult callback
            callback(index, body);
        });
        response.on("error", function(err){
            console.log(err);
        });
    });
}


function getResult(index, body) {
    //sets the result at the index based on when it came in
    result[index] = body;
    //gets the length of the array not counting undefind values
    var size = result.filter(function(item) {
        return item !== undefined
    }).length;

    //if the array has 3 values, we're done and print
    if(size === 3) {
        result.forEach(function(val) {
            console.log(val);
        });
    }
    
}

urls.forEach(function(url, index) {
    getResponse(url, index, getResult);
});
