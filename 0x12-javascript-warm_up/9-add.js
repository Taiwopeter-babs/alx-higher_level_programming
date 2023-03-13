#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  console.log(result);
}

const args = process.argv.slice(2);
const arg1 = parseInt(args[0], 10);
const arg2 = parseInt(args[1], 10);
add(arg1, arg2);
