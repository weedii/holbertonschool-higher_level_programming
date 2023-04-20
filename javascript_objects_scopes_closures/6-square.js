#!/usr/bin/node
const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  // class of Square that inherit from the last Square class

  // charPrint method
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c) { process.stdout.write('c'); } else { process.stdout.write('X'); }
      }
      console.log();
    }
  }
}

module.exports = Square;
