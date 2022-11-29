#!/usr/bin/node
// uses map to compute multiplication of array element to its index
let arr = require('./100-data.js');
let newList = arr.list.map((ele, ind, array) => {
  return ele * ind
});
console.log(arr.list);
console.log(newList);
