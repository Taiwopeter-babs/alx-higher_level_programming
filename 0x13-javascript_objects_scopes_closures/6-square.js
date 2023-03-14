#!/usr/bin/node
const SquareOne = require('./5-square.js');

module.exports = class Square extends SquareOne {
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
