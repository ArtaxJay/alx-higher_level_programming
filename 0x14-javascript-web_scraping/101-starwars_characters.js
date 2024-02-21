#!/usr/bin/node

const req = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

req(apiUrl, (err, res, msg) => {
  if (err) {
    console.error(err);
    return;
  }
  const movie = JSON.parse(msg);
  const charsUrls = movie.characters;

  // Function to print character name and move to the next character
  const printChar = (i) => {
    if (i >= charsUrls.length) {
      return;
    }
    const charUrl = charsUrls[i];
    req(charUrl, (err, res, msg) => {
      if (err) {
        console.error(err);
        return;
      }
      const chars = JSON.parse(msg);
      console.log(chars.name);

      // Print the next character recursively
      printChar(i + 1);
    });
  };

  // Start printing characters from the first character
  printChar(0);
});
