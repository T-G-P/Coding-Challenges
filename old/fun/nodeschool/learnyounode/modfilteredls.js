var fs = require('fs');
var path = require('path');

function filteredLs(dirName, fileExt, callback) {

    fs.readdir(dirName, function(err, list) {
        if (err) {
            return callback(err);
        }

        callback(null, list.filter(function(file) {
            return path.extname(file) === '.'+fileExt
        }));
        
    });
}

module.exports = filteredLs;
