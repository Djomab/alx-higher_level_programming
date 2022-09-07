#!/usr/bin/node

const { list } = require('./100-data');

/**
 * Imports an array and computes a new array.
 * A new list must be created with each value equal to the value of the initial list,
 * multipled by the index in the list
 */
const newList = list.map((item, key) => item * key);
console.log(list);
console.log(newList);
