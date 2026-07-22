const queryWithQuotes = '"The James Webb Space Telescope (JWST) is a space telescope designed to conduct infrared astronomy."';
const queryWithoutQuotes = 'The James Webb Space Telescope (JWST) is a space telescope designed to conduct infrared astronomy.';

async function search(query) {
  const searchUrl = `https://html.duckduckgo.com/html/?q=${encodeURIComponent(query)}`;
  const searchRes = await fetch(searchUrl, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
      'Accept-Language': 'en-US,en;q=0.9'
    }
  });
  
  const html = await searchRes.text();
  const blockRegex = /<div class="result [^"]*">([\s\S]*?)<\/div>\s*<\/div>\s*<\/div>/g;
  let blockMatch;
  let count = 0;
  while ((blockMatch = blockRegex.exec(html)) !== null) {
    count++;
  }
  console.log(`Results for [${query.substring(0, 20)}...]: ${count}`);
}

async function test() {
  await search(queryWithQuotes);
  await search(queryWithoutQuotes);
}
test();
