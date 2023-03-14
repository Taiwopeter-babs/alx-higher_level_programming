#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // method to print with different character
  charPrint (c) {
    if (c) {
      const size = this.width;

      for (let i = 0; i < size; i++) {
        console.log('C'.repeat(size));
      }
    } else {
      super.print();
    }
  }
};
