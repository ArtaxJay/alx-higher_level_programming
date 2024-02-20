#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const toWrite = process.argv[3];

fs.writeFile(filePath, toWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});
