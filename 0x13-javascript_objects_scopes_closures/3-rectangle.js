#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let e = 0; e < this.height; e++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += 'X';
        y++;
      }

      console.log(myVar);
    }
  }
}
module.exports = Rectangle;
