import re

filepath = 'c:/plagiarism-project/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update API Config HTML
old_api_config = """<div class="space-y-4">
              <div>
                <label class="block text-sm font-bold text-gray-700 dark:text-gray-200 mb-2">SerpApi Key</label>
                <input type="password" id="input-api-key" placeholder="Enter your SerpApi Key" class="w-full p-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary focus:border-transparent outline-none transition-colors">
                <p class="text-xs text-gray-500 mt-2">Your key is securely stored in your browser's LocalStorage and is only sent to the backend during scans.</p>
              </div>
              <button id="btn-save-api" class="px-6 py-3 bg-primary text-white font-bold rounded-lg hover:bg-primaryHover transition-colors">Save API Key</button>
            </div>"""

new_api_config = """<div class="space-y-6">
              <div>
                <label class="block text-sm font-bold text-gray-700 dark:text-gray-200 mb-2">SerpApi Key (Plagiarism Engine)</label>
                <input type="password" id="input-api-key" placeholder="Enter your SerpApi Key" class="w-full p-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary focus:border-transparent outline-none transition-colors">
                <p class="text-xs text-gray-500 mt-2">Required for internet scraping. Stored locally in browser.</p>
              </div>
              <div class="pt-4 border-t border-gray-200 dark:border-gray-700">
                <label class="block text-sm font-bold text-gray-700 dark:text-gray-200 mb-2 flex items-center gap-2">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                  Hugging Face Access Token (AI Detection Engine)
                </label>
                <input type="password" id="input-api-key-ai" placeholder="hf_xxxxxxxxxxxxxxxxxxx" class="w-full p-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-colors">
                <p class="text-xs text-gray-500 mt-2">Required for AI vs Human authorship detection. Get a free token at huggingface.co.</p>
              </div>
              <button id="btn-save-api" class="px-6 py-3 bg-primary text-white font-bold rounded-lg hover:bg-primaryHover transition-colors">Save API Keys</button>
            </div>"""

html = html.replace(old_api_config, new_api_config)

# 2. Add IDs to AI Metrics in HTML
# AI Probability Card
old_ai_prob = """<div class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">AI Probability</div>
            <div class="text-3xl font-black text-blue-500">2%</div>"""
new_ai_prob = """<div class="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">AI Probability</div>
            <div class="text-3xl font-black text-blue-500" id="res-ai-prob">--</div>"""
html = html.replace(old_ai_prob, new_ai_prob)

# AI Authorship detailed metrics
old_ai_metrics = """<div class="grid grid-cols-2 gap-4">
                <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm border border-blue-100 dark:border-blue-800/50">
                  <div class="text-[10px] uppercase font-bold text-gray-500 mb-1">Human Score</div>
                  <div class="text-2xl font-black text-blue-600 dark:text-blue-400">98%</div>
                </div>
                <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm border border-blue-100 dark:border-blue-800/50">
                  <div class="text-[10px] uppercase font-bold text-gray-500 mb-1">Burstiness</div>
                  <div class="text-2xl font-black text-gray-900 dark:text-white">High</div>
                </div>
                <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm border border-blue-100 dark:border-blue-800/50">
                  <div class="text-[10px] uppercase font-bold text-gray-500 mb-1">Perplexity</div>
                  <div class="text-2xl font-black text-gray-900 dark:text-white">142</div>
                </div>
                <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm border border-blue-100 dark:border-blue-800/50">
                  <div class="text-[10px] uppercase font-bold text-gray-500 mb-1">Confidence</div>
                  <div class="text-2xl font-black text-gray-900 dark:text-white">99%</div>
                </div>
              </div>"""
new_ai_metrics = """<div class="grid grid-cols-2 gap-4">
                <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm border border-blue-100 dark:border-blue-800/50">
                  <div class="text-[10px] uppercase font-bold text-gray-500 mb-1">Human Score</div>
                  <div class="text-2xl font-black text-blue-600 dark:text-blue-400" id="ai-human-score">--</div>
                </div>
                <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm border border-blue-100 dark:border-blue-800/50">
                  <div class="text-[10px] uppercase font-bold text-gray-500 mb-1">Burstiness</div>
                  <div class="text-2xl font-black text-gray-900 dark:text-white" id="ai-burstiness">--</div>
                </div>
                <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm border border-blue-100 dark:border-blue-800/50">
                  <div class="text-[10px] uppercase font-bold text-gray-500 mb-1">Perplexity</div>
                  <div class="text-2xl font-black text-gray-900 dark:text-white" id="ai-perplexity">--</div>
                </div>
                <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-sm border border-blue-100 dark:border-blue-800/50">
                  <div class="text-[10px] uppercase font-bold text-gray-500 mb-1">Confidence</div>
                  <div class="text-2xl font-black text-gray-900 dark:text-white" id="ai-confidence">--</div>
                </div>
              </div>
              <div id="ai-error-msg" class="text-xs text-red-500 mt-4 hidden font-medium"></div>"""
html = html.replace(old_ai_metrics, new_ai_metrics)

# 3. Update JS API logic
old_js_api = """    // Settings API Save
    const elApiKey = document.getElementById('input-api-key');
    const btnSaveApi = document.getElementById('btn-save-api');
    
    if (localStorage.getItem('serp_api_key')) {
      elApiKey.value = localStorage.getItem('serp_api_key');
    }

    btnSaveApi.addEventListener('click', () => {
      if (elApiKey.value.trim()) {
        localStorage.setItem('serp_api_key', elApiKey.value.trim());
        alert("API Key saved successfully!");
      } else {
        localStorage.removeItem('serp_api_key');
        alert("API Key removed.");
      }
    });"""

new_js_api = """    // Settings API Save
    const elApiKey = document.getElementById('input-api-key');
    const elApiKeyAi = document.getElementById('input-api-key-ai');
    const btnSaveApi = document.getElementById('btn-save-api');
    
    if (localStorage.getItem('serp_api_key')) {
      elApiKey.value = localStorage.getItem('serp_api_key');
    }
    if (localStorage.getItem('hf_api_key')) {
      elApiKeyAi.value = localStorage.getItem('hf_api_key');
    }

    btnSaveApi.addEventListener('click', () => {
      let msg = [];
      if (elApiKey.value.trim()) {
        localStorage.setItem('serp_api_key', elApiKey.value.trim());
        msg.push("SerpApi Key saved.");
      } else {
        localStorage.removeItem('serp_api_key');
      }
      
      if (elApiKeyAi.value.trim()) {
        localStorage.setItem('hf_api_key', elApiKeyAi.value.trim());
        msg.push("Hugging Face Key saved.");
      } else {
        localStorage.removeItem('hf_api_key');
      }
      
      if (msg.length > 0) alert(msg.join("\\n"));
      else alert("API Keys cleared.");
    });"""
html = html.replace(old_js_api, new_js_api)


# 4. Update Main Scan Logic
# Find the exact fetch call inside btnScan
old_fetch = """      try {
        const response = await fetch('/api/scan', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ 
            text: textToScan,
            apiKey: apiKey 
          })
        });

        if (!response.ok) {
          const errData = await response.json();
          throw new Error(errData.error || 'Server error');
        }"""

new_fetch = """      try {
        // Parallel API Calls for Plagiarism and AI Detection
        const hfApiKey = localStorage.getItem('hf_api_key') || "";
        
        const scanPromise = fetch('/api/scan', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text: textToScan, apiKey: apiKey })
        });
        
        const aiPromise = fetch('/api/detect-ai', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text: textToScan, apiKey: hfApiKey })
        });

        const [scanRes, aiRes] = await Promise.all([scanPromise, aiPromise]);

        if (!scanRes.ok) {
          const errData = await scanRes.json();
          throw new Error(errData.error || 'Plagiarism engine error');
        }
        
        // Handle AI Results without breaking the main scan
        try {
            const aiData = await aiRes.json();
            const errEl = document.getElementById('ai-error-msg');
            errEl.classList.add('hidden');
            
            if (aiData.no_key) {
                errEl.textContent = "AI Analysis paused. Add Hugging Face token in API Settings to unlock.";
                errEl.classList.remove('hidden');
                document.getElementById('res-ai-prob').textContent = "--";
                document.getElementById('ai-human-score').textContent = "--";
                document.getElementById('ai-burstiness').textContent = "--";
                document.getElementById('ai-perplexity').textContent = "--";
                document.getElementById('ai-confidence').textContent = "--";
            } else if (aiData.human_score !== null) {
                const aiProb = 100 - aiData.human_score;
                document.getElementById('res-ai-prob').textContent = `${aiProb}%`;
                document.getElementById('ai-human-score').textContent = `${aiData.human_score}%`;
                document.getElementById('ai-burstiness').textContent = aiData.burstiness;
                document.getElementById('ai-perplexity').textContent = aiData.perplexity;
                document.getElementById('ai-confidence').textContent = `${aiData.confidence}%`;
            } else {
                errEl.textContent = "AI Analysis failed: " + aiData.error;
                errEl.classList.remove('hidden');
            }
        } catch(e) {
            console.error("Failed to parse AI response:", e);
        }

        const response = scanRes; // fallback for the rest of the existing code"""

html = html.replace(old_fetch, new_fetch)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Phase 8 successfully applied to index.html!")
