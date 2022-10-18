#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line in the same order of the list “characters” in the /films/ response
 */

const request = require('request');
const id = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + id;

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(char => {
      request(char, function (err, resp, bod) {
        if (err) console.log(err);
        else {
          console.log(JSON.parse(bod).name);
        }
      });
    });
  }
});
