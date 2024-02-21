#!/usr/bin/node
const req = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

req(apiUrl, (err, res, msg) => {
  if (err) {
    console.error(err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Failed to fetch movie data: Status ${res.statusCode}`);
    return;
  }
  const parsedMovie = JSON.parse(msg);
  const charsUrls = parsedMovie.characters;

  charsUrls.forEach(charUrl => {
    req(charUrl, (err, res, msg) => {
      if (err) {
        console.error(err);
        return;
      }
      if (res.statusCode !== 200) {
        console.error(`Failed to fetch character data: Status ${res.statusCode}`);
        return;
      }
      const movieChar = JSON.parse(msg);
      console.log(movieChar.name);
    });
  });
});
