#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const wedgeId = 18; // Wedge Antilles

request(apiUrl, (err, res, msg) => {
  if (err) {
    console.error(err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Failed to fetch movie data: Status ${res.statusCode}`);
    return;
  }
  const starWarsMovies = JSON.parse(msg).results;
  const starringWedge = starWarsMovies.filter(movie => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`));
  console.log(starringWedge.length);
});
