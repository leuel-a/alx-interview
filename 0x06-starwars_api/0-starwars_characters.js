#!/home/leuel/.nvm/versions/node/v10.14.2/bin/node
const args = process.argv;
const request = require('request');

function getCharacters (id) {
  return new Promise((resolve, reject) => {
    const options = {
      url: `https://swapi-api.alx-tools.com/api/films/${id}/`,
      method: 'GET'
    };

    request(options, (error, response, body) => {
      if (error) {
        return reject(new Error(`API Request Error: ${error.message}`));
      }

      if (response.statusCode !== 200) {
        return reject(new Error(`API responded with status code: ${response.statusCode}`));
      }

      try {
        const jsonResponse = JSON.parse(body);
        resolve(jsonResponse.characters);
      } catch (err) {
        reject(new Error('Failed to parse JSON response '));
      }
    });
  });
}

function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    const options = {
      url,
      method: 'GET'
    };

    request(options, (error, response, body) => {
      if (error) {
        return reject(new Error(`API Request Error: ${error}`));
      }

      if (response.statusCode !== 200) {
        return request(new Error(`API responded with status code: ${response.statusCode}`));
      }

      try {
        const responseJSON = JSON.parse(body);
        resolve(responseJSON.name);
      } catch (err) {
        reject(new Error('Failed to parse JSON response '));
      }
    });
  });
}

// This is to get the names of the people in an ordered manner
async function getAllCharacter (endpoints) {
  const result = [];
  for (const endpoint of endpoints) {
    const name = await getCharacterName(endpoint);
    result.push(name);
  }
  return result;
}

// This is the main driver code that will get the names of all the characters in a film
async function main () {
  const filmId = args[2];

  const characters = await getCharacters(filmId);
  const names = await getAllCharacter(characters);

  names.forEach(characterName => console.log(characterName));
}

main();
