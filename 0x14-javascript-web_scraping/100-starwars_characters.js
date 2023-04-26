#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api//films/';
request.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    req.get(i, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
