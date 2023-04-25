#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  }
  const filmResults = JSON.parse(body).results;

  let count = 0;
  for (let i = 0; i < filmResults.length; i++) {
    for (let j = 0; j < filmResults[i].characters.length; j++) {
      const newArray = filmResults[i].characters[j].split('/');
      const last = newArray[newArray.length - 2];
      if (parseInt(last, 10) === 18) {
        count++;
      }
    }
  }
  console.log(count);
});
