# OriginScan - Project Memory & Context

## Project Overview
- **Name:** OriginScan
- **Purpose:** An internet plagiarism & paraphrase checker like Copyscape.
- **Tech Stack:** Vanilla HTML/JS frontend (`index.html`), Node.js Serverless function backend (`api/scan.js`). Deployed on Vercel.
- **Rules:** No `package.json`, no Python, no npm dependencies. Uses native fetch and SerpAPI.

## Current State
- ✅ All project files created (`index.html`, `api/scan.js`, `vercel.json`, `README.md`, `.gitignore`).
- ✅ `.env` created locally with the correct `SERP_API_KEY`.
- ❌ **Issue:** The user manually uploaded the files to GitHub/Vercel (https://plagiarism-project-one.vercel.app/), but reported that "nothing is working."
- ❌ **Blocker:** We couldn't diagnose the error or push code automatically because the user's Windows machine lacked **Git** and **Node.js**.

## Next Steps (When user returns)
When the user returns and says to read this file, execute the following plan:

1. **Verify Installations:**
   - Run `git --version` and `node -v` to ensure the tools are now available in the terminal PATH.
2. **Local Diagnostics:**
   - Run `node test-scan.js` locally (since Node is now installed) to test the `api/scan.js` logic and see if SerpAPI is returning errors or if the text scraping is failing.
3. **Fix the Bugs:**
   - Based on the local test, fix whatever is causing the app to fail. (Check CORS, Vercel function routing, and SerpAPI limits).
4. **Git & GitHub Integration:**
   - Initialize the git repository: `git init`
   - Link to remote: `git remote add origin https://github.com/muddassir-commits/plagiarism-project.git`
   - Commit and push the code directly to trigger a fresh, working Vercel deployment.
5. **Vercel CLI (Optional but helpful):**
   - If we need live logs, we can install Vercel globally (`npm i -g vercel`) and run `vercel dev` or `vercel --prod` to see exactly what Vercel sees.

---
**Note to AI:** Read this file immediately when the new session starts, then proceed with Step 1.
