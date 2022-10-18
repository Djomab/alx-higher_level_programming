#!/usr/bin/node
/**
 * computes the number of tasks completed by user id.
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 */

const request = require('request');
const id = process.argv[2];
const endpoint = 'https://jsonplaceholder.typicode.com/todos';

request(endpoint, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    console.log(JSON.parse(body).title);
  }
});
