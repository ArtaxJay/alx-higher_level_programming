#!/usr/bin/node

const { dict } = require('./101-data');

const extDict = {};

for (const userId in dict) {
  const occurTimes = dict[userId];

  if (occurTimes in extDict) {
    extDict[occurTimes].push(userId);
  } else {
    extDict[occurTimes] = [userId];
  }
}

console.log(extDict);
