import re

filepath = 'c:/plagiarism-project/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract script content
script_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if script_match:
    script_content = script_match.group(1)
else:
    print("Could not find script block")
    exit(1)

new_script_content = script_content + """
    // --- SaaS UI LOGIC ---
    
    // Dark Mode Toggle
    const btnTheme = document.getElementById('btn-theme');
    if (btnTheme) {
      btnTheme.addEventListener('click', () => {
        document.documentElement.classList.toggle('dark');
      });
    }

    // Sidebar Mobile Toggle
    const btnMenu = document.getElementById('btn-menu');
    const sidebar = document.getElementById('sidebar');
    if (btnMenu && sidebar) {
      btnMenu.addEventListener('click', () => {
        sidebar.classList.toggle('-translate-x-full');
      });
    }
"""

new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OriginScan · SaaS Plagiarism Checker</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <!-- Tailwind via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            primary: '#e8542f',
            primaryHover: '#d14624',
          }}
        }}
      }}
    }}
  </script>
  <style type="text/tailwindcss">
    /* Custom Scrollbar */
    ::-webkit-scrollbar {{ width: 8px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 8px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #94a3b8; }}
    .dark ::-webkit-scrollbar-thumb {{ background: #475569; }}
    .dark ::-webkit-scrollbar-thumb:hover {{ background: #64748b; }}

    /* Layout specific */
    html, body {{ height: 100%; }}
    
    /* Ensure chart container text is centered properly */
    .chart-center-text {{
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      pointer-events: none;
    }}

    /* Map JS output classes to Tailwind */
    .line-item {{ @apply p-5 mb-4 rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 shadow-sm transition-colors hover:border-gray-300 dark:hover:border-gray-600; }}
    .line-text {{ @apply text-base mb-3 leading-relaxed text-gray-700 dark:text-gray-300; }}
    .tag {{ @apply inline-block px-2.5 py-1 rounded text-xs font-semibold uppercase tracking-wide; }}
    .tag.original {{ @apply bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300; }}
    .tag.exact {{ @apply bg-red-100 dark:bg-red-900/40 text-red-700 dark:text-red-400; }}
    .tag.close {{ @apply bg-amber-100 dark:bg-amber-900/40 text-amber-700 dark:text-amber-400; }}
    .tag.paraphrase {{ @apply bg-blue-100 dark:bg-blue-900/40 text-blue-700 dark:text-blue-400; }}
    .line-meta {{ @apply mt-4 text-sm text-gray-500 dark:text-gray-400 bg-gray-50 dark:bg-gray-900/50 p-4 rounded-lg border border-gray-200 dark:border-gray-700; }}
    .line-meta a {{ @apply text-primary font-semibold hover:underline; }}
    .matched-chunk {{ @apply mt-3 italic text-gray-500 dark:text-gray-400 border-l-2 border-gray-300 dark:border-gray-600 pl-3; }}
  </style>
</head>
<body class="bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 flex overflow-hidden transition-colors duration-200">

  <!-- LEFT SIDEBAR -->
  <aside id="sidebar" class="bg-white dark:bg-gray-800 w-64 border-r border-gray-200 dark:border-gray-700 flex-shrink-0 flex flex-col absolute inset-y-0 left-0 transform -translate-x-full md:relative md:translate-x-0 transition-transform duration-300 ease-in-out z-20">
    <div class="h-16 flex items-center px-6 border-b border-gray-200 dark:border-gray-700 font-bold text-xl text-primary gap-2">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
      OriginScan
    </div>
    <nav class="flex-1 p-4 space-y-1 overflow-y-auto">
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 font-medium">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9"></rect><rect x="14" y="3" width="7" height="5"></rect><rect x="14" y="12" width="7" height="9"></rect><rect x="3" y="16" width="7" height="5"></rect></svg>
        Dashboard
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg bg-primary/10 text-primary font-medium">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
        New Scan
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 font-medium">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        History
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 font-medium">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
        Reports
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 font-medium">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
        Team
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 font-medium">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
        API
      </a>
    </nav>
    <div class="p-4 border-t border-gray-200 dark:border-gray-700">
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 font-medium">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
        Settings
      </a>
    </div>
  </aside>

  <!-- MAIN WRAPPER -->
  <div class="flex-1 flex flex-col min-w-0">
    <!-- TOP NAVBAR -->
    <header class="bg-white dark:bg-gray-800 h-16 border-b border-gray-200 dark:border-gray-700 flex items-center justify-between px-4 sm:px-6 z-10">
      <div class="flex items-center gap-4">
        <button id="btn-menu" class="md:hidden text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
        <div class="relative hidden sm:block">
          <svg class="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" placeholder="Search..." class="pl-9 pr-4 py-1.5 bg-gray-100 dark:bg-gray-700 border-transparent rounded-md text-sm focus:bg-white dark:focus:bg-gray-600 focus:ring-2 focus:ring-primary focus:border-transparent outline-none w-64 transition-all placeholder-gray-500 dark:placeholder-gray-400">
        </div>
      </div>
      <div class="flex items-center gap-4">
        <button id="btn-theme" class="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200" title="Toggle Dark Mode">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>
        <button class="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 relative">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
          <span class="absolute top-0 right-0 block h-2 w-2 rounded-full bg-red-500 ring-2 ring-white dark:ring-gray-800"></span>
        </button>
        <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-primary to-amber-500 flex items-center justify-center text-white font-bold text-sm cursor-pointer shadow-sm">
          MA
        </div>
      </div>
    </header>

    <!-- PAGE CONTENT -->
    <main class="flex-1 overflow-y-auto p-4 sm:p-6 lg:p-8">
      
      <!-- API WARNING -->
      <div id="api-warning" class="hidden mb-6 bg-amber-50 dark:bg-amber-900/30 border-l-4 border-amber-500 p-4 rounded-md text-amber-800 dark:text-amber-200 text-sm shadow-sm">
        <strong>Configuration Notice:</strong> SERP_API_KEY environment variable is missing. Scanning is disabled; all lines will be marked as original. Please add your key in Vercel settings and redeploy.
      </div>

      <!-- INPUT VIEW -->
      <div id="input-card" class="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6 md:p-8 max-w-4xl mx-auto transition-colors">
        <h1 class="text-2xl font-bold mb-2 text-gray-900 dark:text-white">Check for Plagiarism & Paraphrasing</h1>
        <p class="text-gray-500 dark:text-gray-400 mb-6 text-sm">Paste your article or blog draft below to check every sentence against the live internet.</p>
        
        <textarea id="text-input" placeholder="Paste your text here..." class="w-full h-64 p-4 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary focus:border-transparent outline-none resize-y transition-colors"></textarea>
        
        <div class="flex flex-wrap items-center justify-between mt-4 gap-4">
          <div class="text-sm font-medium text-gray-500 dark:text-gray-400" id="word-count">0 words | 0 characters</div>
          <div class="flex gap-3">
            <button id="btn-sample" class="px-5 py-2 rounded-lg font-medium bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors border border-transparent dark:border-gray-600 shadow-sm">Load sample</button>
            <button id="btn-scan" disabled class="px-5 py-2 rounded-lg font-medium bg-primary text-white hover:bg-primaryHover disabled:opacity-50 disabled:cursor-not-allowed transition-colors shadow-sm">Scan the internet</button>
          </div>
        </div>
        
        <div id="progress-ui" class="hidden mt-6">
          <div class="w-full h-2 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden mb-2">
            <div id="progress-fill" class="h-full bg-primary transition-all duration-300" style="width: 0%"></div>
          </div>
          <div id="progress-text" class="text-sm text-center text-gray-500 dark:text-gray-400 font-medium">Searching the internet...</div>
        </div>
      </div>

      <!-- RESULTS UI -->
      <div id="results-ui" class="hidden max-w-6xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8 items-start">
          
          <!-- Left Panel: Analytics -->
          <div class="lg:col-span-1 flex flex-col gap-6 lg:sticky lg:top-8">
            <div id="verdict-box" class="p-5 rounded-xl bg-green-100 dark:bg-green-900/30 border-l-4 border-green-500 shadow-sm transition-colors">
              <h2 id="verdict-title" class="text-green-800 dark:text-green-400 text-lg font-bold mb-1">Reviewing...</h2>
              <p id="verdict-desc" class="text-green-700 dark:text-green-500 text-sm">Please wait.</p>
            </div>

            <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-5 shadow-sm relative flex items-center justify-center h-56 transition-colors">
              <canvas id="score-chart"></canvas>
              <div class="chart-center-text">
                <div id="score-percent" class="text-4xl font-extrabold text-gray-900 dark:text-white tracking-tight">0%</div>
                <div class="text-xs font-bold text-gray-500 dark:text-gray-400 uppercase tracking-widest mt-1">Original</div>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-4 text-center shadow-sm transition-colors">
                <div id="stat-exact" class="text-2xl font-bold text-red-500 mb-1">0</div>
                <div class="text-[10px] font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Exact Copies</div>
              </div>
              <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-4 text-center shadow-sm transition-colors">
                <div id="stat-close" class="text-2xl font-bold text-amber-500 mb-1">0</div>
                <div class="text-[10px] font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Close Matches</div>
              </div>
              <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-4 text-center shadow-sm transition-colors">
                <div id="stat-para" class="text-2xl font-bold text-blue-500 mb-1">0</div>
                <div class="text-[10px] font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Paraphrased</div>
              </div>
              <div class="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-4 text-center shadow-sm transition-colors">
                <div id="stat-lines" class="text-2xl font-bold text-gray-900 dark:text-white mb-1">0</div>
                <div class="text-[10px] font-bold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Total Lines</div>
              </div>
            </div>
            
            <div class="flex flex-col sm:flex-row gap-3 pt-4 border-t border-gray-200 dark:border-gray-700">
              <button id="btn-new" class="flex-1 px-4 py-2 rounded-lg font-medium bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors shadow-sm">New Scan</button>
              <button id="btn-export" class="flex-1 px-4 py-2 rounded-lg font-medium bg-primary text-white hover:bg-primaryHover transition-colors shadow-sm">Export PDF</button>
            </div>
          </div>

          <!-- Right Panel: Line by Line -->
          <div class="lg:col-span-2 bg-gray-50 dark:bg-gray-900/50 border border-gray-200 dark:border-gray-700 rounded-xl h-[800px] overflow-y-auto p-4 sm:p-6 shadow-inner transition-colors">
            <div id="line-list" class="flex flex-col gap-4">
              <!-- populated by JS -->
            </div>
          </div>

        </div>
      </div>
      
    </main>
  </div>

  <script>
{new_script_content}
  </script>
</body>
</html>"""

with open('c:/plagiarism-project/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Phase 1 Layout rewrite complete")
