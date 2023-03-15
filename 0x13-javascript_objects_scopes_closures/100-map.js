#!/usr/bin/node
const list = require('./100-data.js').list;

(function () {
  const newList = list.map((item, index) => item * index);

  console.log(list);
  console.log(newList);
})();
