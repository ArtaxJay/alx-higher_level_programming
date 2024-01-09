#!/usr/bin/node

let counterVar = 0;

exports.logMe = function (item) {
  console.log(`${counterVar}: ${item}`);
  counterVar++;
};
