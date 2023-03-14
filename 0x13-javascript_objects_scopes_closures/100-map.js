#!/usr/bin/node
const lists = require('./100-data').list;
const lis = lists.map(x => x * lists.indexOf(x));
console.log(lists);
console.log(lis);
