#!/usr/bin/node

const argNum = parseInt(process.argv[2], 10);

if (isNaN(argNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argNum; i++) {
    console.log('C is fun');
  }
}
