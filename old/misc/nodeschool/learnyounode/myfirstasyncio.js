var fs = require('fs');

fs.readFile(process.argv[2], callback);

function callback(err, data) {
    if (err) {
        return console.error(err);
    }
    var lineCount = data
        .toString()
        .split('\n')
        .length-1;
    console.log(lineCount)
}
