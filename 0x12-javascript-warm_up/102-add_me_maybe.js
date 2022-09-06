#!/usr/bin/node

/**
 * Executes x times a function
 * The function must be visible from outside
 * Prototype: function (x, theFunction)
 */

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
