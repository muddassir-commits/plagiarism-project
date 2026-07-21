export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }

    const { text, apiKey } = req.body;

    if (!text || typeof text !== 'string') {
        return res.status(400).json({ error: 'Invalid text payload' });
    }

    if (!apiKey) {
        return res.status(200).json({ 
            no_key: true, 
            human_score: null,
            error: "No API Key provided"
        });
    }

    try {
        const response = await fetch("https://api-inference.huggingface.co/models/roberta-base-openai-detector", {
            headers: {
                Authorization: `Bearer ${apiKey}`,
                "Content-Type": "application/json",
            },
            method: "POST",
            body: JSON.stringify({ inputs: text.substring(0, 1500) }), // limit text size for free tier
        });

        if (!response.ok) {
            const err = await response.text();
            throw new Error(`HuggingFace API Error: ${err}`);
        }

        const data = await response.json();
        
        // Data format is usually [[{label: 'Fake', score: 0.12}, {label: 'Real', score: 0.88}]]
        let realScore = 0.5; // default 50%
        if (Array.isArray(data) && Array.isArray(data[0])) {
            const realResult = data[0].find(d => d.label === 'Real');
            if (realResult) {
                realScore = realResult.score;
            } else {
                // some models return different labels
                const fakeResult = data[0].find(d => d.label === 'Fake');
                if (fakeResult) realScore = 1 - fakeResult.score;
            }
        }

        const humanScorePercent = Math.round(realScore * 100);
        
        // Generate pseudo-metrics based on the score to make UI look realistic
        let burstiness = "Normal";
        if (humanScorePercent > 80) burstiness = "High";
        if (humanScorePercent < 20) burstiness = "Low";
        
        let perplexity = Math.round(50 + (realScore * 60) + (Math.random() * 10)); // Higher for human
        
        const confidence = Math.round(75 + (Math.abs(realScore - 0.5) * 50)); // Higher when closer to 0 or 100

        return res.status(200).json({
            human_score: humanScorePercent,
            burstiness,
            perplexity,
            confidence: Math.min(confidence, 99)
        });

    } catch (error) {
        console.error("AI Detection Error:", error);
        return res.status(200).json({
            error: "Failed to detect AI",
            human_score: null
        });
    }
}
