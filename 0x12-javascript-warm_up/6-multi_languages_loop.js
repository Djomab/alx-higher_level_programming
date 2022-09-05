#!/usr/bin/node

/**
 * prints 3 lines: (like 1-multi_languages.js)
 * but by using an array of string and a loop
 * The first line: “C is fun”
 * The second line: “Python is cool”
 * The third line: “JavaScript is amazing”
 * else print “Not a number”
 */
const stringArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

stringArray.forEach(element => {
  console.log(element);
});
