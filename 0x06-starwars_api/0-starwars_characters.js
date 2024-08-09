#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/films/' + process.argv[2] + '/';

request(url, (err, response, data) => {
    if (err) throw err;

    const films = JSON.parse(data);

    films.characters.forEach((value) => {
        request(value, (err, response, data) => {
            if (err) throw err;

            const character = JSON.parse(data);
            console.log(character.name);
        });
    });
});
