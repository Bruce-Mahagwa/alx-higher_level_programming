#!/usr/bin/node
// prints a string with a datatype converted to an int if possible
let args = process.argv[2];
if (isNaN(args)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args));
}
