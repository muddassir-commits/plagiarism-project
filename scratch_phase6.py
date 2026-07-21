import re

filepath = 'c:/plagiarism-project/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CDN links to <head>
head_pattern = r'</head>'
cdn_links = """  <!-- Libraries for file parsing -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
  <script>pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.worker.min.js';</script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.4.21/mammoth.browser.min.js"></script>
</head>"""
html = html.replace('</head>', cdn_links)

# 2. Add IDs to sidebar links
sidebar_pattern = r'<nav class="space-y-1 mb-8">(.*?)</nav>'
def replace_sidebar(match):
    nav = match.group(1)
    # Add view attributes
    nav = nav.replace('bg-primary/10 text-primary font-bold', 'nav-link active bg-primary/10 text-primary font-bold" data-view="view-new-scan')
    nav = nav.replace('text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors', 'nav-link text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors" data-view="view-placeholder')
    
    # Let's cleanly rebuild the nav to be safe
    new_nav = """
        <a href="#" class="nav-link flex items-center gap-3 px-4 py-3 rounded-lg text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors" data-view="view-dashboard">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
          Dashboard
        </a>
        <a href="#" class="nav-link active flex items-center gap-3 px-4 py-3 rounded-lg bg-primary/10 text-primary font-bold" data-view="view-new-scan">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
          New Scan
        </a>
        <a href="#" class="nav-link flex items-center gap-3 px-4 py-3 rounded-lg text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors" data-view="view-history">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          History
        </a>
        <a href="#" class="nav-link flex items-center gap-3 px-4 py-3 rounded-lg text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors" data-view="view-reports">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          Reports
        </a>
        <a href="#" class="nav-link flex items-center gap-3 px-4 py-3 rounded-lg text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors" data-view="view-team">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
          Team
        </a>
        <a href="#" class="nav-link flex items-center gap-3 px-4 py-3 rounded-lg text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors" data-view="view-api">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          API
        </a>"""
    return f'<nav class="space-y-1 mb-8">{new_nav}</nav>'

html = re.sub(sidebar_pattern, replace_sidebar, html, flags=re.DOTALL)

# Also update the Settings link at the bottom of the sidebar
html = html.replace('text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors flex items-center gap-3 px-4 py-3 rounded-lg"', 
                    'nav-link text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors flex items-center gap-3 px-4 py-3 rounded-lg" data-view="view-settings"')


# 3. Wrap main content in view-new-scan and add other views
main_start = r'<!-- API WARNING -->'
main_end = r'</main>'

main_wrapper_new = """<!-- VIEWS CONTAINER -->
      <div id="views-container">
        
        <!-- NEW SCAN VIEW -->
        <div id="view-new-scan" class="view-page block">
          <!-- API WARNING -->
          <div id="api-warning" class="hidden mb-6 bg-amber-50 dark:bg-amber-900/30 border-l-4 border-amber-500 p-4 rounded-md text-amber-800 dark:text-amber-200 text-sm shadow-sm">
            <strong>Configuration Notice:</strong> You have not configured a SerpApi key. Go to the API tab to configure your key.
          </div>"""

html = html.replace('<!-- API WARNING -->', main_wrapper_new)
html = html.replace('<div id="api-warning" class="hidden mb-6 bg-amber-50 dark:bg-amber-900/30 border-l-4 border-amber-500 p-4 rounded-md text-amber-800 dark:text-amber-200 text-sm shadow-sm">\n        <strong>Configuration Notice:</strong> SERP_API_KEY environment variable is missing. Scanning is disabled; all lines will be marked as original. Please add your key in Vercel settings and redeploy.\n      </div>', '')


other_views = """
        </div> <!-- End view-new-scan -->

        <!-- API CONFIGURATION VIEW -->
        <div id="view-api" class="view-page hidden max-w-4xl mx-auto space-y-6">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6 md:p-8">
            <h1 class="text-2xl font-bold mb-2 text-gray-900 dark:text-white">API Configuration</h1>
            <p class="text-gray-500 dark:text-gray-400 mb-6 text-sm">Configure your personal SerpApi key to power the internet scraping engine.</p>
            
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-bold text-gray-700 dark:text-gray-200 mb-2">SerpApi Key</label>
                <input type="password" id="input-api-key" placeholder="Enter your SerpApi Key" class="w-full p-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary focus:border-transparent outline-none transition-colors">
                <p class="text-xs text-gray-500 mt-2">Your key is securely stored in your browser's LocalStorage and is only sent to the backend during scans.</p>
              </div>
              <button id="btn-save-api" class="px-6 py-3 bg-primary text-white font-bold rounded-lg hover:bg-primaryHover transition-colors">Save API Key</button>
            </div>
          </div>
        </div>

        <!-- HISTORY VIEW -->
        <div id="view-history" class="view-page hidden max-w-5xl mx-auto space-y-6">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6 md:p-8">
            <h1 class="text-2xl font-bold mb-2 text-gray-900 dark:text-white">Scan History</h1>
            <p class="text-gray-500 dark:text-gray-400 mb-6 text-sm">Review your past plagiarism checks (stored locally).</p>
            
            <div class="overflow-x-auto">
              <table class="w-full text-left border-collapse">
                <thead>
                  <tr class="border-b border-gray-200 dark:border-gray-700 text-xs font-bold text-gray-500 uppercase">
                    <th class="p-3">Date</th>
                    <th class="p-3">Words</th>
                    <th class="p-3">Similarity</th>
                    <th class="p-3">Status</th>
                  </tr>
                </thead>
                <tbody id="history-table-body" class="text-sm text-gray-800 dark:text-gray-200">
                  <!-- Injected via JS -->
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- DASHBOARD VIEW -->
        <div id="view-dashboard" class="view-page hidden max-w-5xl mx-auto space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6">
              <h3 class="text-sm font-bold text-gray-500 uppercase">Total Scans</h3>
              <div class="text-4xl font-black text-gray-900 dark:text-white mt-2" id="dash-total-scans">0</div>
            </div>
            <div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6">
              <h3 class="text-sm font-bold text-gray-500 uppercase">Total Words Checked</h3>
              <div class="text-4xl font-black text-primary mt-2" id="dash-total-words">0</div>
            </div>
            <div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6">
              <h3 class="text-sm font-bold text-gray-500 uppercase">Avg Similarity</h3>
              <div class="text-4xl font-black text-red-500 mt-2" id="dash-avg-sim">0%</div>
            </div>
          </div>
        </div>

        <!-- PLACEHOLDER VIEWS -->
        <div id="view-reports" class="view-page hidden max-w-4xl mx-auto flex flex-col items-center justify-center h-96 text-center">
          <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-2">Detailed Reports</h2>
          <p class="text-gray-500">This feature requires a premium account (Database integration).</p>
        </div>
        <div id="view-team" class="view-page hidden max-w-4xl mx-auto flex flex-col items-center justify-center h-96 text-center">
          <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-2">Team Management</h2>
          <p class="text-gray-500">Invite members to share your API quota (Coming soon).</p>
        </div>
        <div id="view-settings" class="view-page hidden max-w-4xl mx-auto flex flex-col items-center justify-center h-96 text-center">
          <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-2">Account Settings</h2>
          <p class="text-gray-500">Manage your profile and subscription here.</p>
        </div>

      </div> <!-- End views-container -->
    </main>"""

html = html.replace('    </main>', other_views)


# 4. Modify URL Extract logic
url_extract_target = """                <button class="px-6 py-3 bg-primary text-white font-bold rounded-r-lg hover:bg-primaryHover transition-colors" onclick="alert('URL Scanning API will be connected soon!')">Extract Text</button>"""
url_extract_new = """                <button id="btn-extract-url" class="px-6 py-3 bg-primary text-white font-bold rounded-r-lg hover:bg-primaryHover transition-colors flex items-center gap-2">
                  <span id="url-extract-text">Extract Text</span>
                </button>"""
html = html.replace(url_extract_target, url_extract_new)

# Add URL extract logic inside <script>
url_js = """
    // URL Extraction Logic
    const btnExtractUrl = document.getElementById('btn-extract-url');
    const inputUrl = document.querySelector('input[type="url"]');
    if (btnExtractUrl) {
      btnExtractUrl.addEventListener('click', async () => {
        const url = inputUrl.value;
        if(!url) return;
        
        const txtEl = document.getElementById('url-extract-text');
        txtEl.textContent = "Extracting...";
        btnExtractUrl.disabled = true;

        try {
          const res = await fetch('/api/extract', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
          });
          const data = await res.json();
          if (data.text) {
            elInput.value = data.text;
            elInput.dispatchEvent(new Event('input'));
            document.querySelector('[data-tab="tab-paste"]').click(); // Switch to paste tab to see text
          } else {
            alert(data.error || "Extraction failed");
          }
        } catch(e) {
          alert("Error extracting URL");
        }
        
        txtEl.textContent = "Extract Text";
        btnExtractUrl.disabled = false;
      });
    }
"""

# 5. Modify File Upload logic
file_js = """
    // File Upload Extraction Logic
    const fileInput = document.getElementById('file-upload-input');
    const tabUpload = document.getElementById('tab-upload');
    
    tabUpload.addEventListener('click', () => fileInput.click());
    
    fileInput.addEventListener('change', async (e) => {
      const file = e.target.files[0];
      if(!file) return;

      const txtEl = tabUpload.querySelector('p.font-medium');
      const originalTxt = txtEl.textContent;
      txtEl.textContent = "Extracting text...";

      try {
        if (file.type === "application/pdf" || file.name.endsWith('.pdf')) {
          const arrayBuffer = await file.arrayBuffer();
          const pdf = await pdfjsLib.getDocument({data: arrayBuffer}).promise;
          let text = '';
          for (let i = 1; i <= pdf.numPages; i++) {
            const page = await pdf.getPage(i);
            const content = await page.getTextContent();
            text += content.items.map(item => item.str).join(' ') + '\\n';
          }
          elInput.value = text;
        } else if (file.name.endsWith('.docx')) {
          const arrayBuffer = await file.arrayBuffer();
          const result = await mammoth.extractRawText({arrayBuffer: arrayBuffer});
          elInput.value = result.value;
        } else {
          // Fallback for txt
          const text = await file.text();
          elInput.value = text;
        }
        
        elInput.dispatchEvent(new Event('input'));
        document.querySelector('[data-tab="tab-paste"]').click();
      } catch (err) {
        console.error(err);
        alert("Failed to parse file.");
      }
      
      txtEl.textContent = originalTxt;
      fileInput.value = '';
    });
"""

# 6. API Key and Routing Logic
api_js = """
    // API Key Management
    const inputApiKey = document.getElementById('input-api-key');
    const btnSaveApi = document.getElementById('btn-save-api');
    
    // Load existing
    const savedKey = localStorage.getItem('plagiarism_api_key') || '';
    if (savedKey) inputApiKey.value = savedKey;

    btnSaveApi.addEventListener('click', () => {
      localStorage.setItem('plagiarism_api_key', inputApiKey.value.trim());
      alert("API Key saved securely to your browser!");
    });

    // SPA Routing
    const navLinks = document.querySelectorAll('.nav-link');
    const viewPages = document.querySelectorAll('.view-page');

    function switchView(viewId) {
      viewPages.forEach(p => {
        p.classList.remove('block');
        p.classList.add('hidden');
      });
      navLinks.forEach(l => {
        l.classList.remove('active', 'bg-primary/10', 'text-primary', 'font-bold');
        l.classList.add('text-gray-700', 'dark:text-gray-200');
      });

      const targetView = document.getElementById(viewId);
      if(targetView) {
        targetView.classList.remove('hidden');
        targetView.classList.add('block');
      }

      const activeLink = document.querySelector(`.nav-link[data-view="${viewId}"]`);
      if(activeLink) {
        activeLink.classList.remove('text-gray-700', 'dark:text-gray-200');
        activeLink.classList.add('active', 'bg-primary/10', 'text-primary', 'font-bold');
      }
      
      if (viewId === 'view-history' || viewId === 'view-dashboard') {
        renderHistory();
      }
    }

    navLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const viewId = link.getAttribute('data-view');
        switchView(viewId);
      });
    });

    // History Logic
    function saveHistory(wordCount, simScore) {
      const history = JSON.parse(localStorage.getItem('plagiarism_history') || '[]');
      history.unshift({
        date: new Date().toLocaleString(),
        words: wordCount,
        sim: simScore,
        status: 'Complete'
      });
      localStorage.setItem('plagiarism_history', JSON.stringify(history.slice(0, 50))); // Keep last 50
    }

    function renderHistory() {
      const history = JSON.parse(localStorage.getItem('plagiarism_history') || '[]');
      const tbody = document.getElementById('history-table-body');
      
      // Update Table
      if(tbody) {
        tbody.innerHTML = history.map(h => `
          <tr class="border-b border-gray-100 dark:border-gray-800">
            <td class="p-3">${h.date}</td>
            <td class="p-3 font-medium">${h.words}</td>
            <td class="p-3"><span class="${h.sim > 20 ? 'text-red-500 font-bold' : 'text-green-500 font-bold'}">${h.sim}%</span></td>
            <td class="p-3"><span class="px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full font-bold">Complete</span></td>
          </tr>
        `).join('');
      }

      // Update Dashboard
      if(document.getElementById('dash-total-scans')) {
        document.getElementById('dash-total-scans').textContent = history.length;
        const totalWords = history.reduce((acc, h) => acc + h.words, 0);
        document.getElementById('dash-total-words').textContent = totalWords;
        const avgSim = history.length > 0 ? Math.round(history.reduce((acc, h) => acc + h.sim, 0) / history.length) : 0;
        document.getElementById('dash-avg-sim').textContent = `${avgSim}%`;
      }
    }
"""

html = html.replace("const elInput = document.getElementById('text-input');", 
                    api_js + url_js + file_js + "\n    const elInput = document.getElementById('text-input');")

# 7. Modify scan request to send API Key
scan_req_target = """        const res = await fetch('/api/scan', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ line: sentences[i] })
        });"""

scan_req_new = """        const apiKey = localStorage.getItem('plagiarism_api_key') || '';
        const res = await fetch('/api/scan', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ line: sentences[i], apiKey: apiKey })
        });"""

html = html.replace(scan_req_target, scan_req_new)

# 8. Save history on completion
render_results_target = """      document.getElementById('res-risk').textContent = exactCount;
      
      if (startTime) {"""

render_results_new = """      document.getElementById('res-risk').textContent = exactCount;
      
      // Save to local history
      saveHistory(totalWords, simScore);

      if (startTime) {"""

html = html.replace(render_results_target, render_results_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Phase 6 implementation complete")
