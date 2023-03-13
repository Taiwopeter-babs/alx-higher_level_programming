#!/usr/bin/node

const argNum = parseInt(process.argv[2], 10);

if (isNaN(argNum)) {
  console.log('Not a number');
} else {
  console.log('My number:', argNum);
}
