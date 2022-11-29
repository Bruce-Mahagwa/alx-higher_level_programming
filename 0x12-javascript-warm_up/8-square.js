#!/usr/bin/node
// prints a square
const args = process.argv[2];
if (isNaN(args)) {
  console.log('Missing size');
} else {
  let str = 'X'.repeat(parseInt(args));
  for (let i = 0; i < parseInt(args); i++) {
    console.log(str);
  }
}
