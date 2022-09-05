#!/usr/bin/node

/**
 * prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer, print “Missing number of occurrences”
 */
const argToConvert = parseInt(process.argv[2], 10);

if (isNaN(argToConvert)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < argToConvert; i++) {
  console.log('C is fun');
}
