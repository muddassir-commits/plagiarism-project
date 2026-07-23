const http = require('http');


// Since api/scan.js is a serverless function, let's mock the req/res object
const handler = require('../api/scan.js').default || require('../api/scan.js');

async function test() {
  const req = {
    method: 'POST',
    body: {
      line: 'The James Webb Space Telescope (JWST) is a space telescope designed to conduct infrared astronomy.',
    }
  };
  
  const res = {
    setHeader: () => {},
    status: (code) => ({
      json: (data) => {
        console.log(`Status: ${code}`);
        console.log(JSON.stringify(data, null, 2));
        return data;
      }
    })
  };
  
  await handler(req, res);
}
test();
