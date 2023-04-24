#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/:id';

request(url, (err, response, body) => {
    if (err) {
        console.log(err);
    }
    const movie = JSON.parse(body);
    if (movie.episode_id === parseInt(id)) {
        console.log(movie.title);
    }
});