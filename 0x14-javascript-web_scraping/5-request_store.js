#!/usr/bin/node
/**
 * gets the contents of a webpage and stores it in a file.
 * The first argument is the URL to request
 * The second argument the file path to store the body response
 * The file must be UTF-8 encoded
 */

const fs = require('fs');
const request = require('request');
const filePath = process.argv[3];
const endpoint = process.argv[2];

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', function (error) {
      if (error) console.log(error);
    });
  }
});
