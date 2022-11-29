#!/usr/bin/node
// a class Square
const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor(size) {
    super(size, size);
      this.size = size;
  }
}
