#!/usr/bin/node
/**
 * display the status code of a GET request.
 * status code must be printed like this: code: <status code>
 */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response) {
  if (!error) {
    console.log('code: ' + response.statusCode);
  }
});
