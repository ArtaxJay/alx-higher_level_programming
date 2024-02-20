#!/usr/bin/node

const req = require('request');
const fs = require('fs');

const webUrl = process.argv[2];
const filePath = process.argv[3];

req(webUrl, (err, res, msg) => {
  if (err) {
    console.error(err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Failed to fetch webpage: Status ${res.statusCode}`);
    return;
  }
  fs.writeFile(filePath, msg, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
