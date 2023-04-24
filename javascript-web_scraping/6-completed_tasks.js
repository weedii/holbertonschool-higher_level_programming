#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const dict = {};

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    for (const task in content) {
      if (content[task].completed) {
        if (!(content[task].userId in dict)) {
          dict[content[task].userId] = 1;
        } else {
          dict[content[task].userId]++;
        }
      }
    }
    console.log(dict);
  }
});
