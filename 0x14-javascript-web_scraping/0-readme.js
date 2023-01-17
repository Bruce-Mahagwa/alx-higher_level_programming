#!/usr/bin/node
// a script that reads a file
const fs = require('fs');
const process = require("process");
fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
	  console.log(err);
	  return;
	   } else {
    console.log(data);
  }
});
