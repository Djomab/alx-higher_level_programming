#!/usr/bin/node
/**
 * Prints the title of a Star Wars movie
 * The first argument is the movie ID
 * status code must be printed like this: code: <status code>
 */

const request = require('request');
const id = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + id;

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
