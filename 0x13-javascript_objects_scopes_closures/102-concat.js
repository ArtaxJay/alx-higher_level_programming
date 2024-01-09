#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const filePath = process.argv[4];

const readFile1 = fs.readFileSync(file1, 'utf-8');
const readFile2 = fs.readFileSync(file2, 'utf-8');

const concatFile = readFile1 + readFile2;

fs.writeFileSync(filePath, concatFile);
