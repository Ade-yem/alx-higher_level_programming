#!/usr/bin/node
const lists = require('./100-data').list;
const lis = lists.map((item, index) => item * index);
console.log(lists);
console.log(lis);
