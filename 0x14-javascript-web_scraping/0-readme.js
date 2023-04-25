#!/usr/bin/node
// This script reads the content of a file from the command line
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
