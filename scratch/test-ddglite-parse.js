const fs = require('fs');

const html = fs.readFileSync('scratch/ddglite-out.html', 'utf8');

// DDG Lite results are usually in rows: 
// <tr class='result-snippet'>...</tr>
// Or <a class="result-url" href="...">

const results = [];
const rowRegex = /<a class="result-snippet"[^>]*href="([^"]+)"[^>]*>(.*?)<\/a>/gi;
let match;
while ((match = rowRegex.exec(html)) !== null) {
  results.push({
    link: match[1],
    snippet: match[2].replace(/<[^>]+>/g, '')
  });
}

// Or we can match the snippet div: <td class='result-snippet'>
const snippetRegex = /<td class='result-snippet'>([\s\S]*?)<\/td>/gi;
const snippets = [];
while ((match = snippetRegex.exec(html)) !== null) {
  snippets.push(match[1].trim());
}

console.log("Snippet Matches:", snippets.length);

const linkRegex = /<a class="result-url" href="([^"]+)">/gi;
const links = [];
while ((match = linkRegex.exec(html)) !== null) {
  links.push(match[1].trim());
}

console.log("Link Matches:", links.length);

for (let i = 0; i < Math.min(links.length, snippets.length); i++) {
  console.log("Result", i, links[i], snippets[i].substring(0, 50));
}
