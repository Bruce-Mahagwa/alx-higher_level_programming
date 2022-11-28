#!/usr/bin/node
// prints a string x number of times according to the first argument
const args = process.argv[2];
const str = 'C is fun';
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(args); i++) {
    console.log('C is fun');
  }
}
