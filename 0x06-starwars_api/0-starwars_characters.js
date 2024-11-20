#!/usr/bin/node
const request = require('request');

let movieIdentification = '';
try {
  movieIdentification = process.argv[2];
  if (movieIdentification === undefined) {
    throw new Error('Exceeded command line argument length');
  }
} catch (error) {
  console.log(`Usage: ${process.argv[1]} movieIdentification`);
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieIdentification}/`;

// Make request
let movie = '';
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(`[${response.statusCode}]: ${response}`);
  } else {
    movie = JSON.parse(body);
    displayCharacters(movie);
  }
});

/**
 * name - displayCharacters
 * @movie: the movie object to log
 */
function displayCharacters (movie) {
  if (movie === undefined) {
    return;
  }
  movie.characters.forEach((url) => {
    request.get((url), (error, response, body) => {
      if (error) {
        console.error('Error', error);
      } else if (response.statusCode !== 200) {
        console.error(`[${response.statusCode}]: ${response}`);
      } else {
        const person = JSON.parse(body);
        console.log(person.name);
      }
    });
  });
}
