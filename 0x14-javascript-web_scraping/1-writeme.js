#!/usr/bin/node
/**
 * writes a string to a file.
 * first argument is the file path
 * content of the file must be written in utf-8
 */

const fs = require('fs');
const file = process.argv[2];
const phrasal = process.argv[3];
fs.writeFile(file, phrasal, 'utf8', function (err) {
  if (err) throw err;
});
