#!/usr/bin/node
// a class square
const Square = require('./5-square.js');
module.exports = class Square1 extends Square {
  constructor(size) {
    super(size);
  }
      charPrint(c='X') {
        let str = c.repeat(this.size);
        for (let i = 0; i < this.size; i++) {
	  console.log(str);
	}
      }
  }
