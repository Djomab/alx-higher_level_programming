#!/usr/bin/node
/**
 * class Rectangle that defines a rectangle
 */
module.exports = class Rectangle {
  /**
   * Attributes
   *  width: wdth of rectangle
   *  height : height of rectangle
   */
  constructor (w, h) {
    if (w > 0 && h > 0){
      this.width = w;
      this.height = h;
    }
  }
}