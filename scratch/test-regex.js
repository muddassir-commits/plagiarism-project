const fs = require('fs');

const html = fs.readFileSync('scratch/ddglite-out.html', 'utf8');

const linkRegex = /<a[^>]*href="([^"]+)"[^>]*class=['"]result-link['"][^>]*>([\s\S]*?)<\/a>|<a[^>]*class=['"]result-link['"][^>]*href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/gi;
const snippetRegex = /<td class='result-snippet'>([\s\S]*?)<\/td>/gi;

const links = [];
const titles = [];
const snippets = [];

let match;
while ((match = linkRegex.exec(html)) !== null) {
  links.push(match[1] || match[3]);
  titles.push((match[2] || match[4]).replace(/<[^>]+>/g, '').trim());
}
while ((match = snippetRegex.exec(html)) !== null) {
  snippets.push(match[1].replace(/<[^>]+>/g, '').trim());
}

console.log("Links:", links.length);
console.log("Snippets:", snippets.length);
