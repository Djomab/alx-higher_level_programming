#!/usr/bin/node
/**
 * prints the number of movies where the character “Wedge Antilles” is present.
 * The first argument is the API URL
 * Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
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
