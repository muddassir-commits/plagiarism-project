import re

filepath = 'c:/plagiarism-project/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the \\n bug
html = html.replace("elInput.value = elInput.value ? elInput.value + '\\\\n' + text : text;", 
                    "elInput.value = elInput.value ? elInput.value + '\\n' + text : text;")

# 2. Add IDs and structure for Tab contents
tab_buttons_target = """          <!-- TABS -->
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
          
          <div class="flex flex-wrap items-center justify-between mt-4 gap-4">"""

tab_buttons_new = """          <!-- TABS -->
          <div class="flex flex-wrap border-b border-gray-200 dark:border-gray-700 mb-6 gap-6" id="input-tabs">
            <button data-tab="tab-paste" class="tab-btn pb-3 border-b-2 border-primary text-primary font-semibold flex items-center gap-2">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
              Paste Text
            </button>
            <button data-tab="tab-upload" class="tab-btn pb-3 border-b-2 border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 font-medium flex items-center gap-2 cursor-pointer transition-colors">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
              Upload File
            </button>
            <button data-tab="tab-url" class="tab-btn pb-3 border-b-2 border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 font-medium flex items-center gap-2 cursor-pointer transition-colors">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
              Scan URL
            </button>
            <button data-tab="tab-gdocs" class="tab-btn pb-3 border-b-2 border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 font-medium flex items-center gap-2 cursor-pointer transition-colors">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              Google Docs
            </button>
          </div>
          
          <!-- TAB CONTENTS -->
          <div id="tab-paste" class="tab-content block">
            <textarea id="text-input" placeholder="Paste your text here..." class="w-full h-64 p-4 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary focus:border-transparent outline-none resize-y transition-colors"></textarea>
          </div>
          
          <div id="tab-upload" class="tab-content hidden h-64 border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 flex flex-col items-center justify-center text-gray-500 dark:text-gray-400 hover:border-primary transition-colors cursor-pointer">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="mb-4 text-gray-400"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
            <p class="font-medium text-gray-700 dark:text-gray-300">Click to upload a file (PDF, DOCX, TXT)</p>
            <p class="text-xs mt-2">or drag and drop here</p>
            <input type="file" class="hidden" accept=".txt,.pdf,.doc,.docx" id="file-upload-input">
          </div>

          <div id="tab-url" class="tab-content hidden h-64 flex flex-col items-center justify-center p-8 bg-gray-50 dark:bg-gray-900 rounded-lg border border-gray-300 dark:border-gray-600">
             <h3 class="font-bold text-gray-700 dark:text-gray-200 mb-4">Scan a Web Page</h3>
             <div class="flex w-full max-w-lg">
                <input type="url" placeholder="https://example.com/article" class="flex-1 p-3 border border-gray-300 dark:border-gray-600 rounded-l-lg bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 outline-none focus:ring-2 focus:ring-primary focus:border-transparent transition-colors">
                <button class="px-6 py-3 bg-primary text-white font-bold rounded-r-lg hover:bg-primaryHover transition-colors" onclick="alert('URL Scanning API will be connected soon!')">Extract Text</button>
             </div>
          </div>

          <div id="tab-gdocs" class="tab-content hidden h-64 flex flex-col items-center justify-center p-8 bg-gray-50 dark:bg-gray-900 rounded-lg border border-gray-300 dark:border-gray-600">
             <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="mb-4 text-blue-500"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
             <h3 class="font-bold text-gray-700 dark:text-gray-200 mb-4">Import from Google Drive</h3>
             <button class="px-6 py-3 bg-blue-600 text-white font-bold rounded-lg hover:bg-blue-700 transition-colors shadow-sm" onclick="alert('Google Drive integration requires OAuth setup in Phase 6.')">Connect Google Drive</button>
          </div>
          
          <div class="flex flex-wrap items-center justify-between mt-4 gap-4" id="action-footer">"""

html = html.replace(tab_buttons_target, tab_buttons_new)

# 3. Add JS for Tabs
js_tabs = """
    // Tab Switching Logic
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // Reset all tabs
        tabBtns.forEach(b => {
          b.classList.remove('border-primary', 'text-primary', 'font-semibold');
          b.classList.add('border-transparent', 'text-gray-500');
        });
        tabContents.forEach(c => {
          c.classList.remove('block');
          c.classList.add('hidden');
        });
        
        // Activate clicked tab
        btn.classList.remove('border-transparent', 'text-gray-500');
        btn.classList.add('border-primary', 'text-primary', 'font-semibold');
        const targetId = btn.getAttribute('data-tab');
        document.getElementById(targetId).classList.remove('hidden');
        document.getElementById(targetId).classList.add('block');
      });
    });
"""

html = html.replace("const tabPasteText = Array.from(document.querySelectorAll('button')).find(btn => btn.textContent.includes(\"Paste Text\")) || document.querySelectorAll('.border-b-2')[0];", 
                    js_tabs + "\\n    const tabPasteText = Array.from(document.querySelectorAll('button')).find(btn => btn.textContent.includes(\"Paste Text\")) || document.querySelectorAll('.border-b-2')[0];")


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Tabs")
