// var concat = require('concat-stream');
// 
// var concatStream = concat(gotString)
// 
// 
// function gotString(body) {
//   // imageBuffer is all of `cat.png` as a node.js Buffer
//     var res = body.toString().split('').reverse().join('');
//     process.stdout.write(res)
// }
// 
// process.stdin.pipe(concatStream).pipe(process.stdout);

var concat = require('concat-stream'),
        ct = function( data ){
          var text = data.toString(),
            result = '';


      result = text.split('').reverse().join('');
      process.stdout.write(result);                      
      console.log( "Output from inside callback" );      
    };


process.stdin.pipe(concat ( ct ) ).pipe(process.stdout); 
  console.log( "Output after concat" );                  

