#!/usr/bin/node
const request = require('request');
let num = 0;
request(process.argv[2], function (error, response, body) {
  if (error === null) {
    const json = JSON.parse(body);
    const result = json.results;
    for (let i = 0; i < result.length; i++) {
      for (let k = 0; k < result[i].characters.length; k++) {
        if (result[i].characters[k].includes('18')) {
          num++;
        }
      }
    }
  }
  console.log(num);
});
