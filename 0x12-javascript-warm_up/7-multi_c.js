#!/usr/bin/node

const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let e = 0; e < x; e++) {
    console.log('C is fun');
  }
}
