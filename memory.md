# OriginScan - Project Memory & Context

## Project Overview
- **Name:** OriginScan
- **Purpose:** A dual-engine modern SaaS application for Plagiarism Checking and AI Authorship Detection.
- **Tech Stack:** Vanilla HTML/JS/Tailwind frontend (`index.html`), Node.js Serverless function backend (`api/scan.js`, `api/detect-ai.js`, `api/extract.js`). Deployed on Vercel.
- **Rules:** No `package.json` for frontend, no Python. Uses native fetch, SerpApi, and Hugging Face API.

## What We Have Built
1. **Premium SaaS UI (Phases 3-7):**
   - Completely overhauled `index.html` from a basic layout to a stunning, modern SaaS dashboard using Tailwind CSS.
   - Built a fully functional Single Page Application (SPA) sidebar routing system (`data-view`).
   - Implemented interactive UI components:
     - Notification Bell dropdown.
     - Profile Avatar dropdown.
     - Source filtering logic (buttons to filter Matched Sources by Exact, High Similarity, Paraphrased).
     - A comprehensive Account Settings dashboard.

2. **Plagiarism Engine (`api/scan.js`):**
   - Connects to SerpApi to scrape the web for matching text.
   - Calculates overlapping similarity score and groups sources uniquely.
   - The user configures their personal SerpApi key directly from the UI (stored securely in `localStorage`).

3. **AI Authorship Engine (`api/detect-ai.js`) (Phase 8):**
   - Created a dedicated backend endpoint for AI vs Human detection.
   - Integrates with Hugging Face Inference API (`roberta-base-openai-detector`).
   - The frontend calls this endpoint in parallel with the plagiarism scan to ensure maximum speed.
   - Dynamically updates the "AI Authorship Analysis (Pro)" UI with real mathematical probabilities (Human Score, Perplexity, Burstiness).
   - Requires a free Hugging Face Access Token to be set in the API Settings panel.

4. **File Extraction Logic:**
   - Integrated client-side parsing using `pdf.js` for PDFs and `mammoth.js` for DOCX.
   - Built `api/extract.js` backend to handle server-side scraping of web URLs.

## Current State
- The frontend is completely functional, styled beautifully, and all placeholder interactions have been wired up.
- The backend successfully runs two distinct machine learning / scraping engines in parallel.
- All code has been pushed and is up-to-date on GitHub (`main` branch) and Vercel.

## Next Steps & Future Roadmap
1. **User Authentication:** Integrate an auth provider (like Firebase or Supabase) to transition from `localStorage` to persistent user accounts.
2. **Payment Gateway:** If the user wants to monetize the SaaS, integrate Stripe billing.
3. **Report Exporting:** Hook up the "Export PDF/DOCX" buttons in the report view to generate downloadable client reports.
