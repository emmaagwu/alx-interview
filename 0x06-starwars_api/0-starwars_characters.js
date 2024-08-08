#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const filmURL = `${API_URL}/films/${process.argv[2]}/`;
  request(filmURL, (err, _, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (pErr, __, charactersBody) => {
          if (pErr) {
            reject(pErr);
            return;
          }
          resolve(JSON.parse(charactersBody).name);
        });
      })
    );

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
