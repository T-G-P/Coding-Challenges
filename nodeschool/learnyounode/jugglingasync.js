var http = require('http');
var urls = process.argv[-1, 3];
var body = '';
console.log(urls);

// function getResponses(urls, callback) {
//     for(var url in urls) {
//         callback(url)
//     }
// }
// 
// function getResponse(url) {
//     http.get(url, function(response) {
//         //encodes response object to be a string
//         response.setEncoding("utf8");
//         //while getting the data, append to the body string
//         response.on("data", function(data){
//             body += data;
//         });
//         response.on("end", function() {
//             //when the request is over, log the length and the body
//             console.log(body);
//         });
//         response.on("error", function(err){
//             console.log(err);
//         });
//     });
// }
// 
// getResponses(urls, getResponse)
