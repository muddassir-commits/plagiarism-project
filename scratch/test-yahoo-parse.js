const fs = require('fs');

const html = fs.readFileSync('scratch/yahoo-out.html', 'utf8');

// Yahoo search results are usually in <div class="compTitle"> and <div class="compText">
// Let's use a simpler regex or cheerio. Cheerio is better if available, but we can't install it easily.
// Let's just look at the HTML structure.

const titleRegex = /<h3 class="title"><a[^>]*href="([^"]+)"[^>]*>(.*?)<\/a><\/h3>/gi;
let match;
const results = [];

while ((match = titleRegex.exec(html)) !== null) {
  let link = match[1];
  // Sometimes Yahoo wraps links in their own redirect: https://r.search.yahoo.com/...
  // We can decode them if necessary.
  
  // Clean up title
  let title = match[2].replace(/<[^>]+>/g, '');
  results.push({ link, title });
}

console.log(results);
