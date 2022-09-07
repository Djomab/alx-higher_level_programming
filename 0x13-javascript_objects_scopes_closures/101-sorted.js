#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
const entries = Object.entries(dict);

for (const [key, val] of entries) {
  if (val in newDict) {
    newDict[val].push(key);
  } else {
    newDict[val] = [key];
  }
}
console.log(newDict);