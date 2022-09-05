#!/usr/bin/node

/**
 * searches the second biggest integer in the list of arguments.
 * All arguments can be converted to integer
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 */
const args = process.argv;
if (args.length <= 3) {
  console.log('0');
} else {
  const arrayOfInts = args.map(Number); // convert to Int all elt of args
  const sortedArray = arrayOfInts.slice(2).sort((a, b) => a - b); // slicing from index 2 and sorting
  console.log(sortedArray[sortedArray.length - 2]); // print the second biggest
}
