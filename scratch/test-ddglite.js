const query = 'The James Webb Space Telescope (JWST) is a space telescope designed to conduct infrared astronomy.';

async function searchDDGLite(query) {
  const searchUrl = `https://lite.duckduckgo.com/lite/`;
  const searchRes = await fetch(searchUrl, {
    method: 'POST',
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: `q=${encodeURIComponent(query)}`
  });
  
  if(!searchRes.ok) {
    console.log("DDG Lite failed:", searchRes.status);
    return;
  }
  const html = await searchRes.text();
  console.log("DDG Lite HTML size:", html.length);
  require('fs').writeFileSync('scratch/ddglite-out.html', html);
}

searchDDGLite(query);
