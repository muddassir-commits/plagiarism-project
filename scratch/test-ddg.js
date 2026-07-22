const query = 'James Webb Space Telescope';
const url = `https://html.duckduckgo.com/html/?q=${encodeURIComponent(query)}`;

async function test() {
  console.log('Fetching:', url);
  const res = await fetch(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
  });
  
  if (!res.ok) {
    console.error('Failed', res.status);
    return;
  }
  
  const html = await res.text();
  console.log('Received HTML size:', html.length);
  require('fs').writeFileSync('scratch/ddg-out.html', html);
  
  // Try to parse results with regex
  const resultRegex = /<a class="result__url" href="([^"]+)">([^<]+)<\/a>/g;
  const snippetRegex = /<a class="result__snippet[^>]*>(.*?)<\/a>/gs;
  
  let match;
  let links = [];
  while ((match = resultRegex.exec(html)) !== null) {
    let rawLink = match[1];
    // DDG sometimes wraps links in /l/?uddg=...
    if (rawLink.startsWith('//duckduckgo.com/l/?uddg=')) {
      rawLink = decodeURIComponent(rawLink.split('uddg=')[1].split('&')[0]);
    } else if (rawLink.startsWith('/l/?uddg=')) {
      rawLink = decodeURIComponent(rawLink.split('uddg=')[1].split('&')[0]);
    }
    links.push({ url: rawLink });
  }
  
  let snippets = [];
  while ((match = snippetRegex.exec(html)) !== null) {
    // Strip inner HTML tags from snippet
    snippets.push(match[1].replace(/<[^>]+>/g, '').trim());
  }
  
  for(let i = 0; i < Math.min(links.length, snippets.length); i++) {
    links[i].snippet = snippets[i];
  }
  
  console.log(links.slice(0, 3));
}

test();
