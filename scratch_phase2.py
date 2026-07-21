import re

filepath = 'c:/plagiarism-project/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the #input-card section
start_input = html.find('      <!-- INPUT VIEW -->')
end_input = html.find('      <!-- RESULTS UI -->')

new_input_html = """      <!-- INPUT VIEW -->
      <div id="input-card" class="max-w-4xl mx-auto space-y-6">
        
        <div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6 md:p-8 transition-colors">
          <h1 class="text-2xl font-bold mb-2 text-gray-900 dark:text-white">New Scan</h1>
          <p class="text-gray-500 dark:text-gray-400 mb-6 text-sm">Upload or paste your document to check for plagiarism and AI-generated content.</p>
          
          <!-- TABS -->
          <div class="flex flex-wrap border-b border-gray-200 dark:border-gray-700 mb-6 gap-6">
            <button class="pb-3 border-b-2 border-primary text-primary font-semibold flex items-center gap-2">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
              Paste Text
            </button>
            <button class="pb-3 border-b-2 border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 font-medium flex items-center gap-2 cursor-pointer transition-colors">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
              Upload File
            </button>
            <button class="pb-3 border-b-2 border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 font-medium flex items-center gap-2 cursor-pointer transition-colors">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
              Scan URL
            </button>
            <button class="pb-3 border-b-2 border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 font-medium flex items-center gap-2 cursor-pointer transition-colors">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              Google Docs
            </button>
          </div>
          
          <textarea id="text-input" placeholder="Paste your text here..." class="w-full h-64 p-4 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary focus:border-transparent outline-none resize-y transition-colors"></textarea>
          
          <div class="flex flex-wrap items-center justify-between mt-4 gap-4">
            <div class="text-sm font-medium text-gray-500 dark:text-gray-400 flex flex-wrap gap-4" id="editor-stats">
              <span id="word-count">0 words</span>
              <span id="char-count">0 characters</span>
              <span id="read-time">0 min read</span>
              <span id="scan-time">~0s scan time</span>
            </div>
            <div class="flex gap-3">
              <button id="btn-sample" class="px-5 py-2.5 rounded-lg font-medium bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors border border-transparent dark:border-gray-600 shadow-sm">Load sample</button>
              <button id="btn-scan" disabled class="px-5 py-2.5 rounded-lg font-medium bg-primary text-white hover:bg-primaryHover disabled:opacity-50 disabled:cursor-not-allowed transition-colors shadow-sm flex items-center gap-2">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                Scan Now
              </button>
            </div>
          </div>
          
          <div id="progress-ui" class="hidden mt-6">
            <div class="flex justify-between text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              <span id="progress-text">Initializing scan...</span>
              <span id="progress-percent">0%</span>
            </div>
            <div class="w-full h-2.5 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden mb-2">
              <div id="progress-fill" class="h-full bg-primary transition-all duration-300 relative" style="width: 0%">
                <div class="absolute inset-0 bg-white/20" style="background-image: linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent); background-size: 1rem 1rem; animation: progress-stripes 1s linear infinite;"></div>
              </div>
            </div>
            <style>
              @keyframes progress-stripes { from { background-position: 1rem 0; } to { background-position: 0 0; } }
            </style>
          </div>
        </div>

        <!-- ADVANCED OPTIONS -->
        <div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6 md:p-8 transition-colors">
          <h2 class="text-lg font-bold text-gray-900 dark:text-white mb-4">Advanced Scan Options</h2>
          
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Sources -->
            <div>
              <h3 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-3">Sources</h3>
              <div class="space-y-3">
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="checkbox" checked class="w-4 h-4 text-primary rounded border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Internet Web Pages</span>
                </label>
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="checkbox" class="w-4 h-4 text-primary rounded border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Academic & Research</span>
                </label>
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="checkbox" class="w-4 h-4 text-primary rounded border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Books & Publications</span>
                </label>
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="checkbox" class="w-4 h-4 text-primary rounded border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">News Articles</span>
                </label>
              </div>
            </div>
            
            <!-- Matching Logic -->
            <div>
              <h3 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-3">Matching Logic</h3>
              <div class="space-y-3">
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="radio" name="match_type" class="w-4 h-4 text-primary border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Exact Matching</span>
                </label>
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="radio" name="match_type" class="w-4 h-4 text-primary border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Semantic Matching</span>
                </label>
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="radio" name="match_type" checked class="w-4 h-4 text-primary border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Hybrid (Recommended)</span>
                </label>
              </div>
            </div>

            <!-- Filters -->
            <div>
              <h3 class="text-sm font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider mb-3">Exclusions</h3>
              <div class="space-y-3">
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="checkbox" checked class="w-4 h-4 text-primary rounded border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Ignore Quotes</span>
                </label>
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="checkbox" checked class="w-4 h-4 text-primary rounded border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Ignore References</span>
                </label>
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="checkbox" class="w-4 h-4 text-primary rounded border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Ignore Small Matches</span>
                </label>
                
                <div class="pt-2">
                  <select class="w-full text-sm p-2 border border-gray-300 dark:border-gray-600 rounded-md bg-gray-50 dark:bg-gray-900 text-gray-700 dark:text-gray-300 focus:ring-primary">
                    <option>Standard Scan Speed</option>
                    <option>Fast Scan</option>
                    <option>Deep Scan (Slower)</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
"""

html = html[:start_input] + new_input_html + html[end_input:]


# 2. Update the JS event listeners for the new counters
js_target = """    elInput.addEventListener('input', () => {
      const text = elInput.value;
      const wordCount = getWordCount(text);
      const charCount = text.length;
      
      elWordCount.textContent = `${wordCount} ${wordCount === 1 ? 'word' : 'words'} | ${charCount} ${charCount === 1 ? 'character' : 'characters'}`;
      
      if (wordCount < 6) {
        btnScan.disabled = true;
        btnScan.textContent = `Scan (need ${6 - wordCount} more ${6 - wordCount === 1 ? 'word' : 'words'})`;
      } else {
        btnScan.disabled = false;
        btnScan.textContent = 'Scan the internet';
      }
    });"""

new_js = """    const elCharCount = document.getElementById('char-count');
    const elReadTime = document.getElementById('read-time');
    const elScanTime = document.getElementById('scan-time');

    elInput.addEventListener('input', () => {
      const text = elInput.value;
      const wordCount = getWordCount(text);
      const charCount = text.length;
      const readTime = Math.max(1, Math.ceil(wordCount / 200)); 
      const scanTime = Math.max(1, Math.ceil(wordCount / 50)); 
      
      elWordCount.textContent = `${wordCount} words`;
      if (elCharCount) elCharCount.textContent = `${charCount} characters`;
      if (elReadTime) elReadTime.textContent = `~${readTime} min read`;
      if (elScanTime) elScanTime.textContent = `~${scanTime}s scan time`;
      
      if (wordCount < 6) {
        btnScan.disabled = true;
        btnScan.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg> Scan Now`;
      } else {
        btnScan.disabled = false;
        btnScan.innerHTML = `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg> Scan Now`;
      }
    });"""

html = html.replace(js_target, new_js)

# 3. Update updateProgress function
prog_target = """      const updateProgress = () => {
        const percent = Math.round((completed / total) * 100);
        progressFill.style.width = `${percent}%`;
        progressText.textContent = `Searching the internet — line ${completed} of ${total}…`;
      };"""

new_prog = """      const updateProgress = () => {
        const percent = Math.round((completed / total) * 100);
        progressFill.style.width = `${percent}%`;
        progressText.textContent = `Searching the internet — line ${completed} of ${total}…`;
        const elPercent = document.getElementById('progress-percent');
        if(elPercent) elPercent.textContent = `${percent}%`;
      };"""

html = html.replace(prog_target, new_prog)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Phase 2 update complete")
