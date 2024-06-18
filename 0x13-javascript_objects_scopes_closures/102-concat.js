#!/usr/bin/node
// 102-concat.js
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentA = fs.readFileSync(fileA, 'utf-8');
const contentB = fs.readFileSync(fileB, 'utf-8');

const result = `${contentA}\n${contentB}`;

fs.writeFileSync(fileC, result);
