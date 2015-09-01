var through2 = require('through2');
var split = require('split');

var i = 1;


process.stdin
    .pipe(split())
    .pipe(through2(write, end))
    .pipe(process.stdout);

function write (buffer, encoding, next) {
    if(!(i % 2 == 0)) {
        this.push(buffer.toString().toLowerCase()+'\n');
    }
    else{
        //console.dir(buffer.toString().toUpperCase());
        this.push(buffer.toString().toUpperCase()+'\n');
    }
    i++;
    next();
}

function end (done) {
    done();
}


// var through = require('through2');
// var split = require('split');
// 
// var lineCount = 0;
// var tr = through(function (buf, _, next) {
//     var line = buf.toString();
//     this.push(lineCount % 2 === 0
//         ? line.toLowerCase() + '\n'
//         : line.toUpperCase() + '\n'
//     );
//     lineCount ++;
//     next();
// });
// process.stdin
//     .pipe(split())
//     .pipe(tr)
//     .pipe(process.stdout)
// ;

