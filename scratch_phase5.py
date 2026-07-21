import re

filepath = 'c:/plagiarism-project/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Export Button to a dropdown-like group
export_target = """              <button id="btn-export" class="flex-1 px-4 py-3 rounded-lg font-bold bg-primary text-white hover:bg-primaryHover shadow-sm transition-colors flex justify-center items-center gap-2">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                Export PDF
              </button>"""

export_new = """              <div class="flex-1 relative group">
                <button id="btn-export" class="w-full px-4 py-3 rounded-lg font-bold bg-primary text-white hover:bg-primaryHover shadow-sm transition-colors flex justify-center items-center gap-2">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                  Export Report
                </button>
                <div class="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all z-10">
                  <div class="py-1 flex flex-col">
                    <button class="px-4 py-2 text-left text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700" onclick="window.print()">Export PDF / Print</button>
                    <button class="px-4 py-2 text-left text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700" onclick="alert('Export DOCX placeholder')">Export DOCX</button>
                    <button class="px-4 py-2 text-left text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700" onclick="alert('Export HTML placeholder')">Export HTML</button>
                    <button class="px-4 py-2 text-left text-sm text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700" onclick="alert('Export JSON placeholder')">Export JSON</button>
                  </div>
                </div>
              </div>"""
html = html.replace(export_target, export_new)

# 2. Add Filters UI to Right Panel
filters_target = """              <div class="p-5 border-b border-gray-200 dark:border-gray-700 flex justify-between items-center">
                <h3 class="font-bold text-gray-900 dark:text-white">Matched Sources</h3>
                <span class="bg-gray-100 dark:bg-gray-700 text-xs font-bold px-2 py-1 rounded text-gray-600 dark:text-gray-300" id="source-count-badge">0</span>
              </div>
              <div class="overflow-y-auto p-5 flex-1 space-y-4" id="sources-list">"""

filters_new = """              <div class="p-5 border-b border-gray-200 dark:border-gray-700 flex flex-col gap-3">
                <div class="flex justify-between items-center">
                  <h3 class="font-bold text-gray-900 dark:text-white">Matched Sources</h3>
                  <span class="bg-gray-100 dark:bg-gray-700 text-xs font-bold px-2 py-1 rounded text-gray-600 dark:text-gray-300" id="source-count-badge">0</span>
                </div>
                <div class="flex gap-2 overflow-x-auto pb-1 scrollbar-hide">
                  <button class="px-3 py-1 bg-primary text-white rounded-full text-xs font-bold whitespace-nowrap shadow-sm">All</button>
                  <button class="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">Exact</button>
                  <button class="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">Semantic</button>
                  <button class="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">High Similarity</button>
                  <button class="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">Academic</button>
                </div>
              </div>
              <div class="overflow-y-auto p-5 flex-1 space-y-4" id="sources-list">"""
html = html.replace(filters_target, filters_new)

# 3. Add Citation button to Source Cards inside renderResults
citation_target = """<button class="mt-3 w-full py-1.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors">Expand Details</button>"""
citation_new = """<div class="mt-3 flex gap-2">
                    <button class="flex-1 py-1.5 text-xs font-semibold rounded bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors">Expand Details</button>
                    <button class="flex-1 py-1.5 text-xs font-semibold rounded border border-gray-200 dark:border-gray-600 text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors" onclick="alert('Citation generator placeholder for: APA, MLA, Harvard, Chicago, IEEE')">Cite Source</button>
                </div>"""
html = html.replace(citation_target, citation_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Phase 5 update complete")
