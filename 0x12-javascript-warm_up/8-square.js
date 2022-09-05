#!/usr/bin/node

/**
 * prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 */
const squareSize = parseInt(process.argv[2], 10);

if (isNaN(squareSize)) {
  console.log('Missing size');
}

for (let i = 0; i < squareSize; i++) {
  for (let j = 0; j < squareSize; j++) {
    process.stdout.write('X');
  }
  console.log();
}
