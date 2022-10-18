#!/usr/bin/node
/**
 * reads and prints the content of a file.
 * first argument is the file path
 * content of the file must be read in utf-8
 */

const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', function (err, data) {
  console.log(data);
  if (err) throw err;
});
