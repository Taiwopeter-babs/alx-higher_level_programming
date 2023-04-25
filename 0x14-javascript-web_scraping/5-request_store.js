#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const [url, filePath] = process.argv.slice(2);
request
  .get(url)
  .on('error', function (error) {
    if (error) {
      console.error(error);
    }
  })
  .pipe(fs.createWriteStream(filePath, 'utf-8'));
