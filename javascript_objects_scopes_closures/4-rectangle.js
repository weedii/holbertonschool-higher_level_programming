#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  // print method
  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  // rotate method
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // double method
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
