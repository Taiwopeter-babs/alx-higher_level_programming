#!/usr/bin/node

// declare global variable
let number = 0;

exports.logMe = function (item) {
  function increment () {
    console.log(`${number}: ${item}`);
  }
  increment();
  number++;
};
