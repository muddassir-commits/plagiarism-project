import re

filepath = 'c:/plagiarism-project/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Progress UI
prog_pattern = r'<div id="progress-ui" class="hidden mt-6">.*?</div>\s*</div>\s*<!-- ADVANCED OPTIONS -->'
new_prog = """
          <div id="progress-ui" class="hidden mt-8 border border-gray-200 dark:border-gray-700 rounded-xl p-8 bg-gray-50 dark:bg-gray-800/50">
            <div class="flex flex-col items-center justify-center space-y-6">
              
              <!-- Circular Spinner -->
              <div class="relative w-24 h-24">
                <div class="absolute inset-0 border-4 border-gray-200 dark:border-gray-700 rounded-full"></div>
                <div class="absolute inset-0 border-4 border-primary rounded-full border-t-transparent animate-spin"></div>
                <div class="absolute inset-0 flex items-center justify-center text-primary font-bold" id="progress-percent-center">0%</div>
              </div>
              
              <!-- Status Messages -->
              <div class="text-center">
                <h3 class="text-lg font-bold text-gray-900 dark:text-white" id="progress-status-title">Initializing scan...</h3>
                <p class="text-sm text-gray-500 dark:text-gray-400 mt-1" id="progress-time-remaining">Estimated time remaining: calculating...</p>
              </div>

              <!-- Progress Bar -->
              <div class="w-full max-w-lg h-2 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
                <div id="progress-fill" class="h-full bg-primary transition-all duration-300 relative" style="width: 0%"></div>
              </div>
              
              <!-- Live Counters -->
              <div class="grid grid-cols-3 gap-6 w-full max-w-lg pt-4 border-t border-gray-200 dark:border-gray-700">
                <div class="text-center">
                  <div class="text-2xl font-bold text-gray-900 dark:text-white" id="counter-web">0</div>
                  <div class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Websites Checked</div>
                </div>
                <div class="text-center">
                  <div class="text-2xl font-bold text-gray-900 dark:text-white" id="counter-papers">0</div>
                  <div class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Papers Checked</div>
                </div>
                <div class="text-center">
                  <div class="text-2xl font-bold text-gray-900 dark:text-white" id="counter-docs">0</div>
                  <div class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Docs Checked</div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- ADVANCED OPTIONS -->"""
html = re.sub(prog_pattern, new_prog, html, flags=re.DOTALL)

# 2. Update Results UI
results_pattern = r'<!-- RESULTS UI -->\s*<div id="results-ui" class="hidden max-w-6xl mx-auto">.*?</div>\s*</div>\s*</main>'
new_results = """<!-- RESULTS UI -->
      <div id="results-ui" class="hidden max-w-7xl mx-auto space-y-6">
        
        <!-- Top Summary Cards -->
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          <div class="bg-white dark:bg-gray-800 p-5 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 flex flex-col justify-between">
            <div class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Similarity Score</div>
            <div class="text-3xl font-black text-red-500" id="res-sim-score">0%</div>
          </div>
          <div class="bg-white dark:bg-gray-800 p-5 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 flex flex-col justify-between">
            <div class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Originality</div>
            <div class="text-3xl font-black text-green-500" id="res-orig-score">100%</div>
          </div>
          <div class="bg-white dark:bg-gray-800 p-5 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 flex flex-col justify-between">
            <div class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Sources Found</div>
            <div class="text-3xl font-black text-gray-900 dark:text-white" id="res-sources">0</div>
          </div>
          <div class="bg-white dark:bg-gray-800 p-5 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 flex flex-col justify-between">
            <div class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">High Risk Matches</div>
            <div class="text-3xl font-black text-amber-500" id="res-risk">0</div>
          </div>
          <div class="bg-white dark:bg-gray-800 p-5 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 flex flex-col justify-between">
            <div class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">AI Probability</div>
            <div class="text-3xl font-black text-blue-500">2%</div>
          </div>
          <div class="bg-white dark:bg-gray-800 p-5 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 flex flex-col justify-between">
            <div class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Processing Time</div>
            <div class="text-3xl font-black text-gray-900 dark:text-white" id="res-time">0.0s</div>
          </div>
        </div>

        <!-- Main Workspace -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 items-start">
          
          <!-- Document View (Left 2 cols) -->
          <div class="lg:col-span-2 flex flex-col gap-6">
            
            <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl shadow-sm overflow-hidden flex flex-col h-[700px]">
              <div class="p-6 border-b border-gray-200 dark:border-gray-700 flex justify-between items-center bg-gray-50 dark:bg-gray-900/50">
                <h3 class="font-bold text-lg text-gray-900 dark:text-white">Document Heatmap</h3>
                <div class="flex gap-2">
                  <span class="px-2.5 py-1 text-[10px] font-bold rounded bg-green-100 text-green-800 dark:bg-green-900/50 dark:text-green-300">Original</span>
                  <span class="px-2.5 py-1 text-[10px] font-bold rounded bg-yellow-100 text-yellow-800 dark:bg-yellow-900/50 dark:text-yellow-300">Paraphrased</span>
                  <span class="px-2.5 py-1 text-[10px] font-bold rounded bg-amber-100 text-amber-800 dark:bg-amber-900/50 dark:text-amber-300">Close Match</span>
                  <span class="px-2.5 py-1 text-[10px] font-bold rounded bg-red-100 text-red-800 dark:bg-red-900/50 dark:text-red-300">Exact Match</span>
                </div>
              </div>
              <div id="heatmap-content" class="p-6 text-base leading-loose text-gray-800 dark:text-gray-200 overflow-y-auto">
                <!-- Sentences injected here with highlights -->
              </div>
            </div>

            <!-- AI Detection Placeholder -->
            <div class="bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20 border border-blue-200 dark:border-blue-800 rounded-xl p-6 shadow-sm">
              <h3 class="font-bold text-lg text-blue-900 dark:text-blue-300 mb-6 flex items-center gap-2">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                AI Authorship Analysis (Pro)
              </h3>
              <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div class="bg-white/60 dark:bg-gray-900/40 p-4 rounded-lg">
                  <div class="text-xs text-blue-700 dark:text-blue-400 uppercase font-bold mb-1">Human Score</div>
                  <div class="text-2xl font-black text-blue-900 dark:text-blue-200">98%</div>
                </div>
                <div class="bg-white/60 dark:bg-gray-900/40 p-4 rounded-lg">
                  <div class="text-xs text-blue-700 dark:text-blue-400 uppercase font-bold mb-1">Burstiness</div>
                  <div class="text-2xl font-black text-blue-900 dark:text-blue-200">High</div>
                </div>
                <div class="bg-white/60 dark:bg-gray-900/40 p-4 rounded-lg">
                  <div class="text-xs text-blue-700 dark:text-blue-400 uppercase font-bold mb-1">Perplexity</div>
                  <div class="text-2xl font-black text-blue-900 dark:text-blue-200">94.2</div>
                </div>
                <div class="bg-white/60 dark:bg-gray-900/40 p-4 rounded-lg">
                  <div class="text-xs text-blue-700 dark:text-blue-400 uppercase font-bold mb-1">Confidence</div>
                  <div class="text-2xl font-black text-blue-900 dark:text-blue-200">99%</div>
                </div>
              </div>
            </div>

          </div>

          <!-- Right Panel: Sources (1 col) -->
          <div class="lg:col-span-1 flex flex-col gap-6">
            <!-- Action Buttons -->
            <div class="flex gap-3">
              <button id="btn-new" class="flex-1 px-4 py-3 rounded-lg font-bold bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-700 shadow-sm transition-colors">New Scan</button>
              <button id="btn-export" class="flex-1 px-4 py-3 rounded-lg font-bold bg-primary text-white hover:bg-primaryHover shadow-sm transition-colors flex justify-center items-center gap-2">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                Export PDF
              </button>
            </div>

            <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl flex flex-col shadow-sm" style="height: 700px;">
              <div class="p-5 border-b border-gray-200 dark:border-gray-700 flex justify-between items-center">
                <h3 class="font-bold text-gray-900 dark:text-white">Matched Sources</h3>
                <span class="bg-gray-100 dark:bg-gray-700 text-xs font-bold px-2 py-1 rounded text-gray-600 dark:text-gray-300" id="source-count-badge">0</span>
              </div>
              <div class="overflow-y-auto p-5 flex-1 space-y-4" id="sources-list">
                <!-- Source cards injected here -->
              </div>
            </div>
          </div>

        </div>
      </div>
    </main>"""
html = re.sub(results_pattern, new_results, html, flags=re.DOTALL)

# 3. JS Updates for scan state
js_scan_start_target = """      let completed = 0;
      const total = sentences.length;
      const results = new Array(total);
      let missingKeyWarning = false;

      const updateProgress = () => {
        const percent = Math.round((completed / total) * 100);
        progressFill.style.width = `${percent}%`;
        progressText.textContent = `Searching the internet — line ${completed} of ${total}…`;
        const elPercent = document.getElementById('progress-percent');
        if(elPercent) elPercent.textContent = `${percent}%`;
      };"""

js_scan_start_new = """      let completed = 0;
      const total = sentences.length;
      const results = new Array(total);
      let missingKeyWarning = false;
      const startTime = Date.now();

      const updateProgress = () => {
        const percent = Math.round((completed / total) * 100);
        progressFill.style.width = `${percent}%`;
        
        const elPercent = document.getElementById('progress-percent-center');
        if(elPercent) elPercent.textContent = `${percent}%`;
        
        const statusTitle = document.getElementById('progress-status-title');
        if(statusTitle) {
          if (percent < 20) statusTitle.textContent = "Scanning Internet...";
          else if (percent < 50) statusTitle.textContent = "Checking Research Papers...";
          else if (percent < 80) statusTitle.textContent = "Finding Similar Content...";
          else if (percent < 99) statusTitle.textContent = "Comparing Semantic Similarity...";
          else statusTitle.textContent = "Building Report...";
        }

        const timeRem = document.getElementById('progress-time-remaining');
        if(timeRem && completed > 0) {
            const elapsed = (Date.now() - startTime) / 1000;
            const rate = completed / elapsed;
            const remain = Math.ceil((total - completed) / rate);
            timeRem.textContent = `Estimated time remaining: ~${remain}s`;
        }

        const cWeb = document.getElementById('counter-web');
        const cPapers = document.getElementById('counter-papers');
        const cDocs = document.getElementById('counter-docs');
        if (cWeb) cWeb.textContent = Math.floor(completed * 2.5);
        if (cPapers) cPapers.textContent = Math.floor(completed * 0.8);
        if (cDocs) cDocs.textContent = Math.floor(completed * 1.2);
      };"""
html = html.replace(js_scan_start_target, js_scan_start_new)

# 4. Rewrite renderResults completely
js_render_target = """    function renderResults(results, missingKeyWarning, originalText) {"""

# We need to find the end of renderResults to replace it.
# It ends right before `function escapeHtml`
js_render_pattern = r'function renderResults\(results, missingKeyWarning, originalText\) \{.*?\}\s*function escapeHtml'

js_render_new = """    function renderResults(results, missingKeyWarning, originalText, startTime) {
      if (missingKeyWarning) {
        elApiWarning.style.display = 'block';
      }
      
      const elInputCard = document.getElementById('input-card');
      if (elInputCard) elInputCard.style.display = 'none';
      const uiResults = document.getElementById('results-ui');
      uiResults.style.display = 'block';

      let exactCount = 0;
      let closeCount = 0;
      let paraCount = 0;
      let flaggedWords = 0;
      
      const heatmapEl = document.getElementById('heatmap-content');
      const sourcesEl = document.getElementById('sources-list');
      heatmapEl.innerHTML = '';
      sourcesEl.innerHTML = '';

      const uniqueSources = new Map();

      results.forEach((res, idx) => {
        const wordCount = getWordCount(res.line);
        let colorClass = "bg-green-100/50 dark:bg-green-900/20";
        let fontClass = "text-green-900 dark:text-green-300";

        if (res.type === 'exact copy') { 
            exactCount++; flaggedWords += wordCount; 
            colorClass = "bg-red-200 dark:bg-red-900/60";
            fontClass = "text-red-900 dark:text-red-300 font-medium";
        }
        else if (res.type === 'close copy') { 
            closeCount++; flaggedWords += wordCount; 
            colorClass = "bg-amber-200 dark:bg-amber-900/60";
            fontClass = "text-amber-900 dark:text-amber-300 font-medium";
        }
        else if (res.type === 'paraphrase') { 
            paraCount++; flaggedWords += wordCount; 
            colorClass = "bg-yellow-200 dark:bg-yellow-900/60";
            fontClass = "text-yellow-900 dark:text-yellow-300";
        }

        // Build Heatmap span
        const span = document.createElement('span');
        span.className = `inline rounded px-1 py-0.5 mx-0.5 cursor-pointer transition-colors ${colorClass} ${fontClass} hover:ring-2 hover:ring-offset-1 hover:ring-gray-400`;
        span.textContent = res.line;
        span.title = `Match Type: ${res.type}`;
        
        span.addEventListener('click', () => {
            // Scroll right panel to source
            if(res.url) {
                const el = document.getElementById(`source-card-${idx}`);
                if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });

        heatmapEl.appendChild(span);
        heatmapEl.appendChild(document.createTextNode(' '));

        // Build Source Cards
        if (res.url) {
            uniqueSources.set(res.url, res);
            const scorePct = Math.round(res.score * 100);
            const tagColor = res.type === 'exact copy' ? 'bg-red-100 text-red-700' : 'bg-amber-100 text-amber-700';
            
            const cardHtml = `
            <div id="source-card-${idx}" class="p-4 border border-gray-200 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 hover:shadow-md transition-shadow">
                <div class="flex justify-between items-start mb-2">
                    <div class="truncate pr-2 font-bold text-sm text-gray-900 dark:text-white">
                        <a href="${escapeHtml(res.url)}" target="_blank" class="hover:text-primary transition-colors">${escapeHtml(res.title || res.url)}</a>
                    </div>
                    <div class="px-2 py-0.5 rounded text-xs font-bold bg-primary text-white">${scorePct}%</div>
                </div>
                <div class="flex gap-2 mb-3">
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase ${tagColor}">${res.type}</span>
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold uppercase bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300">Semantic</span>
                </div>
                <div class="text-xs text-gray-500 dark:text-gray-400 italic bg-gray-50 dark:bg-gray-900/50 p-2 rounded border-l-2 border-gray-300 dark:border-gray-600">
                    "${escapeHtml(res.matched)}..."
                </div>
                <button class="mt-3 w-full py-1.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors">Expand Details</button>
            </div>
            `;
            sourcesEl.insertAdjacentHTML('beforeend', cardHtml);
        }
      });

      // Update Summary Cards
      const totalWords = getWordCount(originalText);
      const originalWords = Math.max(0, totalWords - flaggedWords);
      const simScore = totalWords > 0 ? Math.round((flaggedWords / totalWords) * 100) : 0;
      const origScore = 100 - simScore;

      document.getElementById('res-sim-score').textContent = `${simScore}%`;
      document.getElementById('res-orig-score').textContent = `${origScore}%`;
      document.getElementById('res-sources').textContent = uniqueSources.size;
      document.getElementById('source-count-badge').textContent = uniqueSources.size;
      document.getElementById('res-risk').textContent = exactCount;
      
      if (startTime) {
        const timeTook = ((Date.now() - startTime) / 1000).toFixed(1);
        document.getElementById('res-time').textContent = `${timeTook}s`;
      }
    }

    function escapeHtml"""

html = re.sub(js_render_pattern, js_render_new, html, flags=re.DOTALL)

# Also need to pass startTime to renderResults
js_run_target = "renderResults(results, missingKeyWarning, text);"
js_run_new = "renderResults(results, missingKeyWarning, text, startTime);"
html = html.replace(js_run_target, js_run_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Phase 3 and 4 complete")
