#!/usr/bin/node
/**
 * class Rectangle that defines a rectangle
 */
module.exports = class Rectangle {
  /**
   * Attributes
   *  width: with of rectangle
   *  height: height of rect
   *  If w or h is equal to 0 or not a positive integer,
   *  create an empty object
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
};
