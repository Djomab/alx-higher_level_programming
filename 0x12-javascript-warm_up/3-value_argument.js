#!/usr/bin/node

/**
 * prints the first argument passed to it:
 * If no arguments are passed to the script, print “No argument”
 */

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
