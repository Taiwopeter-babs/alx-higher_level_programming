#!/usr/bin/node
// This script writes a string to a file from the command line
const fs = require('fs');

(function () {
  try {
    const [filePath, text] = process.argv.slice(2);
    fs.writeFile(filePath, text, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } catch (err) {

  }
})();
