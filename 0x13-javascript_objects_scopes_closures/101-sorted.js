#!/usr/bin/node
// 101-sorted.js
const dict = require('./101-data').dict;

const newDict = {};

for (const [id, occurrences] of Object.entries(dict)) {
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(id);
}

for (const [occurrences, ids] of Object.entries(newDict)) {
  newDict[occurrences] = ids.sort();
}

console.log(newDict);
