#!/usr/bin/node
// adds 2 integers
function add(a, b) { 
  // adds 2 numbers
  let sum = parseInt(a) + parseInt(b);
  console.log(sum);
}
add(process.argv[2], process.argv[3]);
