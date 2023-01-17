#!/usr/bin/node
// using star wars api to get movie title
const request = require("request");
const process = require("process");
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`
request(url, (err, res, body) => {
    const data = JSON.parse(body)
   console.log(data.title)
})
