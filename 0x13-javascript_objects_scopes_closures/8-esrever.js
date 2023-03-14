#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];
  const lenList = list.length;

  if (!list || list.length === 0) {
    return arr;
  }

  for (let i = lenList - 1; i >= 0; i--) {
    arr.push(list[i]);
  }
  return (arr);
};
