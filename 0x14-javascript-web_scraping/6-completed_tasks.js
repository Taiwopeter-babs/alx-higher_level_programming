#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const newArray = {};
let currPos = 0;

request(url, (error, response, body) => {
  if (error) {
    throw error;
  } else {
    const taskList = JSON.parse(body);

    for (let userId = 1; userId <= 10; userId++) {
      let count = 0;
      let done = 0;
      let pos = currPos;
      while (pos < taskList.length) {
        if (count < 20) {
          if (taskList[pos].completed) {
            done++;
          }
        } else {
          break;
        }
        pos++;
        count++;
      }
      currPos = pos;
      newArray[userId] = done;
    }
    console.log(newArray);
  }
});
