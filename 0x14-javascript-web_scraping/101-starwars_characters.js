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
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(body).name);
        });
      }));
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.log(err));
  }
});
