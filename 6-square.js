#!/usr/bin/node
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let e = 0; e < this.height; e++) {
      let var = '';
      let b = 0;
      while (b < this.width) {
        var += myChar;
        b++;
      }

      console.log(var);
    }
  }
}

module.exports = Square;
