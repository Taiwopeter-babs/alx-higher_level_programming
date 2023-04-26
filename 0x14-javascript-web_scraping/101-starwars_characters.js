#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const movieObj = JSON.parse(body).characters;

    async function getNames () {
      for (let i = 0; i < movieObj.length; i++) {
        const newRequest = new Request(movieObj[i]);
        const newResponse = await fetch(newRequest);
        const res = await newResponse.json();
        console.log(res.name);
      }
    }
    getNames();
  }
});
