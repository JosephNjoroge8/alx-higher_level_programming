#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    const printCharacterName = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
            resolve();
          }
        });
      });
    };

    // Sequentially print character names
    (async () => {
      for (const characterUrl of characters) {
        await printCharacterName(characterUrl);
      }
    })();
  }
});
