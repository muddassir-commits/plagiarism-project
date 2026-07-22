module.exports = async function handler(req, res) {
  // 1. CORS Headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle OPTIONS request for CORS
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { line, apiKey: customApiKey } = req.body || {};
  if (!line || typeof line !== 'string') {
    return res.status(400).json({ error: 'No line provided' });
  }

  // No API key required for internal scraper

  // 2. Pre-check: Skip lines shorter than 6 words
  const words = line.trim().split(/\s+/).filter(w => w.length > 0);
  if (words.length < 6) {
    return res.status(200).json({
      type: 'original',
      score: 0,
      url: '',
      title: '',
      matched: '',
      no_key: false
    });
  }

  // 3. Search via Custom Scraper (DuckDuckGo HTML)
  const query = line;
  const searchUrl = `https://html.duckduckgo.com/html/?q=${encodeURIComponent(query)}`;

  let html = '';
  try {
  for (let attempt = 1; attempt <= 3; attempt++) {
    const searchRes = await fetch(searchUrl, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
      }
    });
    
    if (searchRes.status === 429) {
      if (attempt === 3) throw new Error(`Scraper error: 429 (Rate Limited)`);
      // Wait before retrying (1.5s, then 3s)
      await new Promise(r => setTimeout(r, 1500 * attempt));
      continue;
    }
    
    if (!searchRes.ok) {
      throw new Error(`Scraper error: ${searchRes.status}`);
    }
    
    html = await searchRes.text();
    break;
  }
    const results = [];
    
    // Extract each result block safely to avoid misalignment
    const blockRegex = /<div class="result [^"]*">([\s\S]*?)<\/div>\s*<\/div>\s*<\/div>/g;
    let blockMatch;
    
    while ((blockMatch = blockRegex.exec(html)) !== null) {
      const block = blockMatch[1];
      
      const titleMatch = /<h2 class="result__title">\s*<a[^>]*href="([^"]+)"[^>]*>([\s\S]*?)<\/a>\s*<\/h2>/.exec(block);
      const snippetMatch = /<a class="result__snippet[^>]*>([\s\S]*?)<\/a>/.exec(block);
      
      if (titleMatch && snippetMatch) {
        let rawLink = titleMatch[1];
        if (rawLink.includes('uddg=')) {
          rawLink = decodeURIComponent(rawLink.split('uddg=')[1].split('&')[0]);
        }
        
        const titleText = titleMatch[2].replace(/<[^>]+>/g, '').trim();
        const snippetText = snippetMatch[1].replace(/<[^>]+>/g, '').trim();
        
        // Filter ads
        if (rawLink.includes('y.js?ad_domain') || rawLink.includes('duckduckgo.com/y.js')) continue;
        
        results.push({ link: rawLink, title: titleText, snippet: snippetText });
      }
    }

    let bestResult = {
      type: 'original',
      score: 0,
      url: '',
      title: '',
      matched: '',
      no_key: false
    };

    const typeRank = { 'exact copy': 4, 'close copy': 3, 'paraphrase': 2, 'original': 1 };

    // 4. Process up to 4 results
    for (const r of results.slice(0, 4)) {
      const { link, title, snippet } = r;
      if (!link) continue;

      let pageText = '';
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 8000);
        const pageRes = await fetch(link, {
          headers: {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
          },
          signal: controller.signal
        });
        clearTimeout(timeoutId);

        if (pageRes.ok) {
          const html = await pageRes.text();
          pageText = extractText(html);
        }
      } catch (err) {
        // Silently ignore fetch/timeout errors for individual pages
      }

      // Combine snippet and page text
      const blob = (snippet || '') + ' ' + pageText;

      let currentType = 'original';
      let currentScore = 0;
      let matchedChunk = '';

      if (blob.includes(line)) {
        currentType = 'exact copy';
        currentScore = 1.0;
        matchedChunk = line;
      } else {
        const windowMatch = bestWindow(line, blob);
        const fuzzyScore = windowMatch.score;
        const overlap = overlapRatio(line, blob);

        if (fuzzyScore >= 0.75) {
          currentType = 'close copy';
          currentScore = fuzzyScore;
          matchedChunk = windowMatch.chunk;
        } else if (overlap >= 0.70 && fuzzyScore >= 0.40) {
          currentType = 'paraphrase';
          currentScore = (overlap * 0.6) + (fuzzyScore * 0.4);
          matchedChunk = windowMatch.chunk;
        }
      }

      // Update best result if this is better
      if (
        typeRank[currentType] > typeRank[bestResult.type] ||
        (typeRank[currentType] === typeRank[bestResult.type] && currentScore > bestResult.score)
      ) {
        bestResult = {
          type: currentType,
          score: currentScore,
          url: link,
          title: title || '',
          matched: matchedChunk.substring(0, 220),
          no_key: false
        };
      }
    }

    if (bestResult.type === 'original') {
      bestResult.url = '';
      bestResult.title = '';
      bestResult.matched = '';
    }

    return res.status(200).json(bestResult);

  } catch (error) {
    console.error('Scan Error:', error);
    // If it completely fails, return as original but log error
    return res.status(200).json({
      type: 'original',
      score: 0,
      url: '',
      title: '',
      matched: '',
      no_key: false,
      error: error.message || 'Failed to process'
    });
  }
}

// === Similarity Helpers ===

function extractText(html) {
  // Strip scripts and styles entirely
  let text = html.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, ' ');
  text = text.replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, ' ');
  // Strip all other HTML tags
  text = text.replace(/<[^>]+>/g, ' ');
  // Collapse whitespace
  text = text.replace(/\s+/g, ' ').trim();
  // Cap at 50k chars
  return text.substring(0, 50000);
}

function contentWords(s) {
  const stopwords = new Set([
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in', 'into', 'is', 'it', 
    'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the', 'their', 'then', 'there', 'these', 
    'they', 'this', 'to', 'was', 'will', 'with', 'which'
  ]);
  const tokens = s.toLowerCase().match(/\b\w+\b/g) || [];
  return tokens.filter(w => w.length > 2 && !stopwords.has(w));
}

function overlapRatio(sentence, page) {
  const sWords = contentWords(sentence);
  if (sWords.length === 0) return 0;
  const pWords = new Set(contentWords(page));
  let count = 0;
  for (const w of sWords) {
    if (pWords.has(w)) count++;
  }
  return count / sWords.length;
}

function dice(a, b) {
  function getBigrams(str) {
    const s = str.toLowerCase();
    const bigrams = new Set();
    for (let i = 0; i < s.length - 1; i++) {
      bigrams.add(s.substring(i, i + 2));
    }
    return bigrams;
  }
  
  const bg1 = getBigrams(a);
  const bg2 = getBigrams(b);
  
  if (bg1.size === 0 || bg2.size === 0) return 0;
  
  let intersection = 0;
  for (const bg of bg1) {
    if (bg2.has(bg)) intersection++;
  }
  
  return (2 * intersection) / (bg1.size + bg2.size);
}

function bestWindow(sentence, page) {
  const sTokens = sentence.trim().split(/\s+/);
  const pTokens = page.trim().split(/\s+/);
  
  if (pTokens.length === 0) return { score: 0, chunk: '' };
  
  const windowSize = sTokens.length + 4;
  const step = Math.max(1, Math.floor(sTokens.length / 2));
  
  let maxScore = 0;
  let bestChunk = '';
  
  for (let i = 0; i < pTokens.length; i += step) {
    const chunkTokens = pTokens.slice(i, i + windowSize);
    const chunkStr = chunkTokens.join(' ');
    const score = dice(sentence, chunkStr);
    
    if (score > maxScore) {
      maxScore = score;
      bestChunk = chunkStr;
    }
    
    if (i + windowSize >= pTokens.length) break;
  }
  
  return { score: maxScore, chunk: bestChunk };
}
