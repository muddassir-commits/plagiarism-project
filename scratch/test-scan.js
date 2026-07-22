const http = require('http');


// Since api/scan.js is a serverless function, let's mock the req/res object
const handler = require('../api/scan.js').default || require('../api/scan.js');

async function test() {
  const req = {
    method: 'POST',
    body: {
      line: 'James Webb Space Telescope is very large.',
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
