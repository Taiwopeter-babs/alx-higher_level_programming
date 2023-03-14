#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // print method
  print () {
    const width = this.width;
    const height = this.height;

    for (let i = 0; i < height; i++) {
      console.log('X'.repeat(width));
    }
  }
};
