#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);

const secondArg = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(firstArg, secondArg);
