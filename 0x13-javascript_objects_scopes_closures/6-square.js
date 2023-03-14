#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let s;
      for (let i = 0; i < this.height; i++) {
        s = '';
        for (let i = 0; i < this.width; i++) {
          s += c;
        }
        console.log(s);
      }
    }
  }
};
