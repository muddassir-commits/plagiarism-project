# OriginScan

An internet originality scanner that checks text against the live internet. 
Built with vanilla HTML/CSS/JS and a Node.js serverless function.

## Deployment to Vercel

1. Push this repository to GitHub.
2. Import the repository into Vercel and click **Deploy**. Vercel will automatically detect the Node.js serverless function (`api/scan.js`) and the static frontend (`index.html`). No build settings or package installations are required.
3. In your Vercel project dashboard, go to **Settings > Environment Variables** and add:
   - `SERP_API_KEY`: Your key from [SerpApi](https://serpapi.com/) (the free tier provides 100 searches/month).
4. After adding the key, go to **Deployments** and trigger a **Redeploy** to ensure the new environment variable is loaded.
5. Go to **Settings > Domains** in Vercel. Add your custom domain (e.g., `plagiarism.muddassirali.com`) and configure the provided CNAME in your DNS settings.

*Note: Scanning the whole internet requires a search API key. Without `SERP_API_KEY`, the app will load but will mark all lines as original, displaying a configuration warning.*
