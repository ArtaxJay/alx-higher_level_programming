#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2])) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
