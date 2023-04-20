#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  // class of Square that inherit from Rectangle class

  // constructor
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
