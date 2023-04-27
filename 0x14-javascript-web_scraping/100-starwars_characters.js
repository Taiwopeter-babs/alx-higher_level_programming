#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const movieObj = JSON.parse(body).characters;

    // console.log(typeof movieObj);
    let idx = 0;

    while (idx < movieObj.length) {
      request(movieObj[idx], (err, response, body) => {
        if (err) {
          throw err;
        } else if (response.statusCode === 200) {
          const actorName = JSON.parse(body).name;
          console.log(actorName);
        }
      });
      idx++;
    }
  }
});
