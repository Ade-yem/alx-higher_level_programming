#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let s;
    for (let i = 0; i < this.height; i++) {
      s = '';
      for (let i = 0; i < this.width; i++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const s = this.width;
    this.width = this.height;
    this.height = s;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
