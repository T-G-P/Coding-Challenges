var fs = require('fs');
var path_to_file = process.argv[2];
var buff = fs.readFileSync(path_to_file);
var new_line_count = buff.toString().split('\n').length-1;
console.log(new_line_count);
