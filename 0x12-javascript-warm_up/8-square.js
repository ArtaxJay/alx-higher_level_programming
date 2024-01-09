#!/usr/bin/node

// const myArr = []
if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2])) === true) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
