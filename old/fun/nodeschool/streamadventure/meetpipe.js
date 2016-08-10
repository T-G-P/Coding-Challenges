var fs = require('fs');
var dataStream = fs.createReadStream(process.argv[2]).pipe(process.stdout);

