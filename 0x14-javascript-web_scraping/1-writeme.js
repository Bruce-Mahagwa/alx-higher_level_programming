#!/usr/bin/node
// a script that writes to a file
const fs = require('fs');
const process = require("process");
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err) {
  if (err) {
	  console.log(err);
  }
});
