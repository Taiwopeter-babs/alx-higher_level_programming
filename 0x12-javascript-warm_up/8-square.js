#!/usr/bin/node

const argNum = parseInt(process.argv[2], 10);

if (isNaN(argNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argNum; i++) {
    console.log('X'.repeat(argNum));
  }
}
