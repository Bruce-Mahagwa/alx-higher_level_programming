#!/usr/bin/node
// gets the html of a webpage and saves it to a file
const request = require("request");
const process = require("process");
const url = process.argv[2];
const fs = require("fs");
const file = process.argv[3]
request(url, (err, res, body) => {
   if (!err) {
      fs.writeFile(file, body, "utf-8", (err) => {
	      if (err) {
		      console.log(err)}})}}
)
