var fs = require('fs');
var path = require('path');
var dirName = process.argv[2];
var fileExt = process.argv[3];

function filteredLs(dirName, fileExt) {
    fs.readdir(dirName, function(err, list) {
        if (err) {
            throw err
        }

        list.filter(function(file) {
            return path.extname(file) === '.'+fileExt;
        })
            .forEach(function(element, index, array) {
                console.log(element);
            });
    });
}
