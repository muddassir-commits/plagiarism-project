const query = 'The James Webb Space Telescope (JWST) is a space telescope designed to conduct infrared astronomy.';

async function searchYahoo(query) {
  const searchUrl = `https://search.yahoo.com/search?p=${encodeURIComponent(query)}`;
  const searchRes = await fetch(searchUrl, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
      'Accept-Language': 'en-US,en;q=0.9'
    }
  });
  
  if(!searchRes.ok) {
    console.log("Yahoo failed:", searchRes.status);
    return;
  }
  const html = await searchRes.text();
  console.log("Yahoo HTML size:", html.length);
  require('fs').writeFileSync('scratch/yahoo-out.html', html);
}

searchYahoo(query);
