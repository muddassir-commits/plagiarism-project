import re

filepath = 'c:/plagiarism-project/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Source Filter Buttons
old_filters = """<div class="flex gap-2 overflow-x-auto pb-1 scrollbar-hide">
                  <button class="px-3 py-1 bg-primary text-white rounded-full text-xs font-bold whitespace-nowrap shadow-sm">All</button>
                  <button class="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">Exact</button>
                  <button class="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">Semantic</button>
                  <button class="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">High Similarity</button>
                  <button class="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">Academic</button>
                </div>"""

new_filters = """<div class="flex gap-2 overflow-x-auto pb-1 scrollbar-hide" id="source-filters">
                  <button data-filter="all" class="source-filter-btn px-3 py-1 bg-primary text-white rounded-full text-xs font-bold whitespace-nowrap shadow-sm transition-colors">All</button>
                  <button data-filter="exact copy" class="source-filter-btn px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">Exact</button>
                  <button data-filter="close copy" class="source-filter-btn px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">High Similarity</button>
                  <button data-filter="paraphrase" class="source-filter-btn px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full text-xs font-bold whitespace-nowrap transition-colors">Paraphrased</button>
                </div>"""

html = html.replace(old_filters, new_filters)

# 2. Add `data-type` to Source Cards in JS
# We need to modify the JS where `cardHtml` is created.
old_cardHtml_start = """<div id="source-card-${idx}" class="p-4 border border-gray-200 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 hover:shadow-md transition-shadow">"""
new_cardHtml_start = """<div id="source-card-${idx}" data-source-type="${res.type}" class="source-card p-4 border border-gray-200 dark:border-gray-700 rounded-lg bg-white dark:bg-gray-800 hover:shadow-md transition-shadow">"""

html = html.replace(old_cardHtml_start, new_cardHtml_start)


# 3. Update Navbar Dropdowns
old_nav_right = """<div class="flex items-center gap-4">
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
      </div>"""

new_nav_right = """<div class="flex items-center gap-4">
        <button id="btn-theme" class="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200" title="Toggle Dark Mode">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>
        
        <!-- Notifications Dropdown -->
        <div class="relative">
          <button id="btn-notif" class="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200 relative focus:outline-none">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg>
            <span class="absolute top-0 right-0 block h-2 w-2 rounded-full bg-red-500 ring-2 ring-white dark:ring-gray-800"></span>
          </button>
          <div id="dropdown-notif" class="hidden absolute right-0 mt-3 w-72 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 z-50">
            <div class="p-3 border-b border-gray-200 dark:border-gray-700 font-bold text-gray-900 dark:text-white">Notifications</div>
            <div class="flex flex-col max-h-64 overflow-y-auto">
              <a href="#" class="p-3 border-b border-gray-100 dark:border-gray-700/50 hover:bg-gray-50 dark:hover:bg-gray-700/50 block">
                <div class="text-sm font-semibold text-gray-800 dark:text-gray-200">Scan Complete</div>
                <div class="text-xs text-gray-500 mt-1">Your 500-word document scan is ready.</div>
                <div class="text-[10px] text-gray-400 mt-1">2 mins ago</div>
              </a>
              <a href="#" class="p-3 hover:bg-gray-50 dark:hover:bg-gray-700/50 block">
                <div class="text-sm font-semibold text-gray-800 dark:text-gray-200">Welcome to OriginScan!</div>
                <div class="text-xs text-gray-500 mt-1">Setup your custom API key to get started.</div>
                <div class="text-[10px] text-gray-400 mt-1">1 hr ago</div>
              </a>
            </div>
            <a href="#" class="block p-2 text-center text-xs text-primary font-bold bg-gray-50 dark:bg-gray-900/50 rounded-b-lg border-t border-gray-200 dark:border-gray-700">View All</a>
          </div>
        </div>

        <!-- Profile Dropdown -->
        <div class="relative">
          <div id="btn-profile" class="w-8 h-8 rounded-full bg-gradient-to-tr from-primary to-amber-500 flex items-center justify-center text-white font-bold text-sm cursor-pointer shadow-sm">
            MA
          </div>
          <div id="dropdown-profile" class="hidden absolute right-0 mt-3 w-56 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 z-50">
            <div class="p-3 border-b border-gray-200 dark:border-gray-700">
              <div class="font-bold text-gray-900 dark:text-white">Muddassir Ali</div>
              <div class="text-xs text-gray-500">Pro Plan Member</div>
            </div>
            <div class="flex flex-col py-1">
              <a href="#" class="px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700" onclick="switchView('view-settings')">Account Settings</a>
              <a href="#" class="px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">Billing & Usage</a>
              <div class="my-1 border-t border-gray-200 dark:border-gray-700"></div>
              <a href="#" class="px-4 py-2 text-sm text-red-600 dark:text-red-400 hover:bg-gray-100 dark:hover:bg-gray-700" onclick="localStorage.clear(); window.location.reload();">Sign Out</a>
            </div>
          </div>
        </div>
      </div>"""

if old_nav_right in html:
    html = html.replace(old_nav_right, new_nav_right)
else:
    print("Could not find old nav right!")

# 4. Update Settings Page
old_settings = """<div id="view-settings" class="view-page hidden max-w-4xl mx-auto flex flex-col items-center justify-center h-96 text-center">
          <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-2">Account Settings</h2>
          <p class="text-gray-500">Manage your profile and subscription here.</p>
        </div>"""

new_settings = """<div id="view-settings" class="view-page hidden max-w-4xl mx-auto space-y-6">
          <div class="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6 md:p-8">
            <h1 class="text-2xl font-bold mb-2 text-gray-900 dark:text-white">Account Settings</h1>
            <p class="text-gray-500 dark:text-gray-400 mb-6 text-sm">Manage your profile details and subscription preferences.</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <!-- Profile Details -->
              <div class="space-y-4">
                <h3 class="text-sm font-bold text-gray-900 dark:text-white uppercase tracking-wider border-b border-gray-200 dark:border-gray-700 pb-2">Profile Information</h3>
                <div>
                  <label class="block text-xs font-bold text-gray-500 mb-1">Full Name</label>
                  <input type="text" value="Muddassir Ali" class="w-full p-2.5 text-sm border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary focus:border-transparent outline-none">
                </div>
                <div>
                  <label class="block text-xs font-bold text-gray-500 mb-1">Email Address</label>
                  <input type="email" value="muddassir@example.com" class="w-full p-2.5 text-sm border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-primary focus:border-transparent outline-none">
                </div>
                <button class="px-4 py-2 bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-200 text-sm font-bold rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors">Update Profile</button>
              </div>

              <!-- Subscription Panel -->
              <div class="space-y-4">
                <h3 class="text-sm font-bold text-gray-900 dark:text-white uppercase tracking-wider border-b border-gray-200 dark:border-gray-700 pb-2">Subscription</h3>
                <div class="bg-gradient-to-br from-primary/10 to-amber-500/10 border border-primary/20 rounded-xl p-5">
                  <div class="flex justify-between items-center mb-2">
                    <div class="font-black text-primary text-lg">Pro Plan</div>
                    <span class="px-2 py-1 bg-primary text-white text-[10px] font-bold rounded uppercase">Active</span>
                  </div>
                  <p class="text-xs text-gray-600 dark:text-gray-400 mb-4">You are currently using your own SerpApi Key.</p>
                  
                  <div class="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2 mb-1">
                    <div class="bg-primary h-2 rounded-full" style="width: 45%"></div>
                  </div>
                  <div class="flex justify-between text-xs text-gray-500 font-medium mb-4">
                    <span>450 / 1,000 API calls used</span>
                    <span>Resets in 12 days</span>
                  </div>
                  <button class="w-full py-2 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 text-gray-800 dark:text-gray-200 text-sm font-bold rounded-lg shadow-sm hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors">Manage Billing</button>
                </div>
              </div>
            </div>

            <!-- Preferences -->
            <div class="mt-8 space-y-4">
              <h3 class="text-sm font-bold text-gray-900 dark:text-white uppercase tracking-wider border-b border-gray-200 dark:border-gray-700 pb-2">Preferences</h3>
              <div class="flex flex-col gap-3">
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="checkbox" checked class="w-4 h-4 text-primary rounded border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Receive email notifications for long scans</span>
                </label>
                <label class="flex items-center gap-3 cursor-pointer group">
                  <input type="checkbox" class="w-4 h-4 text-primary rounded border-gray-300 focus:ring-primary">
                  <span class="text-sm text-gray-700 dark:text-gray-300 group-hover:text-primary transition-colors">Share anonymous scan data to improve AI accuracy</span>
                </label>
              </div>
            </div>

          </div>
        </div>"""

if old_settings in html:
    html = html.replace(old_settings, new_settings)
else:
    print("Could not find old settings placeholder!")

# 5. Inject JS logic
js_additions = """
    // --- PHASE 7 INTERACTIVE UI LOGIC ---

    // Source Filtering
    const sourceFilters = document.querySelectorAll('.source-filter-btn');
    sourceFilters.forEach(btn => {
      btn.addEventListener('click', () => {
        // Reset styles
        sourceFilters.forEach(b => {
          b.classList.remove('bg-primary', 'text-white');
          b.classList.add('bg-gray-100', 'dark:bg-gray-700', 'text-gray-600', 'dark:text-gray-300');
        });
        // Activate current
        btn.classList.add('bg-primary', 'text-white');
        btn.classList.remove('bg-gray-100', 'dark:bg-gray-700', 'text-gray-600', 'dark:text-gray-300');

        const filterType = btn.getAttribute('data-filter');
        const cards = document.querySelectorAll('.source-card');
        
        cards.forEach(card => {
          if (filterType === 'all') {
            card.style.display = 'block';
          } else {
            const type = card.getAttribute('data-source-type');
            if (type === filterType) {
              card.style.display = 'block';
            } else {
              card.style.display = 'none';
            }
          }
        });
      });
    });

    // Navbar Dropdowns
    const btnNotif = document.getElementById('btn-notif');
    const dropdownNotif = document.getElementById('dropdown-notif');
    const btnProfile = document.getElementById('btn-profile');
    const dropdownProfile = document.getElementById('dropdown-profile');

    function closeAllDropdowns() {
      if(dropdownNotif) dropdownNotif.classList.add('hidden');
      if(dropdownProfile) dropdownProfile.classList.add('hidden');
    }

    if(btnNotif) {
      btnNotif.addEventListener('click', (e) => {
        e.stopPropagation();
        const isHidden = dropdownNotif.classList.contains('hidden');
        closeAllDropdowns();
        if(isHidden) dropdownNotif.classList.remove('hidden');
      });
    }

    if(btnProfile) {
      btnProfile.addEventListener('click', (e) => {
        e.stopPropagation();
        const isHidden = dropdownProfile.classList.contains('hidden');
        closeAllDropdowns();
        if(isHidden) dropdownProfile.classList.remove('hidden');
      });
    }

    // Close dropdowns when clicking outside
    document.addEventListener('click', (e) => {
      closeAllDropdowns();
    });

    // Prevent dropdown clicks from closing themselves
    if(dropdownNotif) dropdownNotif.addEventListener('click', e => e.stopPropagation());
    if(dropdownProfile) dropdownProfile.addEventListener('click', e => e.stopPropagation());

  </script>
</body>"""

html = html.replace("  </script>\n</body>", js_additions)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Phase 7 successfully applied!")
