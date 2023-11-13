#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let e = 0; e < size; e++) {
    let row = '';
    for (let b = 0; b < size; b++) row += 'X';
    console.log(row);
  }
}
