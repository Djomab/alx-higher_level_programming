#!/usr/bin/node

/**
 * prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 */
const firstInt = parseInt(process.argv[2], 10);
const secondInt = parseInt(process.argv[3], 10);

function add (a, b) {
  return a + b;
}

console.log(add(firstInt, secondInt));
