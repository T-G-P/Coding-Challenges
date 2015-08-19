var filteredLs = require('./modfilteredls.js');

function callback(err, data) {
    if(err) {
        return console.log(err);
    }
    data.forEach(function(element, index, array) {
        console.log(element);
    });

}

filteredLs(process.argv[2], process.argv[3], callback);
