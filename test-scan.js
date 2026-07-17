const handler = require('./api/scan.js');

const req = {
  method: 'POST',
  body: {
    line: "The James Webb Space Telescope is the largest optical telescope in space. It is designed to conduct infrared astronomy."
  }
};

const res = {
  setHeader: () => {},
  status: (code) => {
    return {
      json: (data) => {
        console.log("Status:", code);
        console.log("Response:", JSON.stringify(data, null, 2));
      },
      end: () => {}
    };
  }
};

// require('dotenv').config(); // This will load SERP_API_KEY from .env if dotenv is installed, but since there's no package.json we can just set it manually.
process.env.SERP_API_KEY = "954688dfb6a87aa36c4b7e9f5590f6320618c9768f2189f2c1b076a8c717a24c";

async function run() {
  console.log("Testing exact match...");
  await handler(req, res);

  console.log("\nTesting paraphrase match...");
  req.body.line = "The Webb telescope in outer space is a massive optical instrument created to look at the universe using infrared light.";
  await handler(req, res);

  console.log("\nTesting original text...");
  req.body.line = "I am writing a completely original sentence right now that nobody has ever written before in the exact history of the universe.";
  await handler(req, res);
}

run();
