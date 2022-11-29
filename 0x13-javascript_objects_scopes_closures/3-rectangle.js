#!/usr/bin/node
// Defines a class Rectangl
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const x = 'x'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(x);
    }
  }
};
