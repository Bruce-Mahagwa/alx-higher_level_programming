#!/usr/bin/node
// sorts an object
let obj = require('./101-data.js');
let arr = Array.from(new Set(Object.values(obj.dict)));
let objects = {};
for (let i = 0; i < arr.length; i++) {
    let newArr = [];
    for (let j in obj) {
        if (obj[j] === arr[i]) {
            newArr.push(j);
        }
    }
    objects[arr[i]]  = newArr;
}
console.log(objects)
