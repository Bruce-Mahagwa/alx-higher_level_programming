#!/usr/bin/node
// counts the number of times a character appears in an api
const request = require("request");
const process = require("process");
const ulr = process.argv[2];
request(ulr, (err, res, body) => {
   const data = JSON.parse(body)
   const arr =data.results.filter((item) => {
      return item.characters.filter((actor) => {
         return actor.includes("18")
      })})
	console.log(arr.length)
})
