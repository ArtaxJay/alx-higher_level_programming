#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (err, res, msg) => {
  if (err) {
    console.error(err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Failed to fetch movie data: Status ${res.statusCode}`);
    return;
  }
  const movieCollection = JSON.parse(msg);
  console.log(movieCollection.title);
});
