#!/usr/bin/node
const msg = process.argv.length;
console.log(msg === 2 ? 'No argument' : msg === 3 ? 'Argument found' : 'Arguments found');
