#!/usr/bin/node
// prints the status code of a GET request
const request = require("request");
const process = require("process");
let url = process.argv[2];
request(url, (err, res, body) => {
      console.log(`code: ${res.statusCode}`)
   }
)
