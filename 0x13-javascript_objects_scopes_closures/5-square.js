#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * class Square that defines a square and inherits from Rectangle
 */
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
};
