#!/usr/bin/node

const cliValue = parseInt(process.argv[2]);
const resultant = 1;

function factorial (n) {
  if (n < 1) {
    return resultant;
  }
  // factorial(n);
  return n * factorial(n - 1);
}

if (cliValue === 0 || isNaN(cliValue) === true) {
  console.log(1);
} else {
  console.log(factorial(cliValue));
}
