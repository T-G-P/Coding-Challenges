var concat = require('concat-stream');

process.stdin.pipe(concat(function(buff) {
    process.stdout.write(buff.toString().split('').reverse().join(''));
}));

