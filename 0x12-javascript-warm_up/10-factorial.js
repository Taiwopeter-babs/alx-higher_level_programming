#!/usr/bin/node

function factorial (argNum) {
  if (isNaN(argNum)) {
    return 1;
  }
  if (argNum === 0) {
    return 1;
  }
  return argNum * factorial(argNum - 1);
}

const arg = parseInt(process.argv[2], 10);
const result = factorial(arg);
console.log(result);
