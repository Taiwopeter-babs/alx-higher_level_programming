#!/usr/bin/node

exports.converter = function (base) {
  return (numberToConvert) => numberToConvert.toString(base);
};
