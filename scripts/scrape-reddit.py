"""
scrape-reddit.py
Simulated Reddit scraper for testing
"""

import json
from datetime import datetime

def scrape_reddit(subreddits=None, keywords=None, limit=50):
    if subreddits is None:
        subreddits = ["mexico", "Entrepreneur", "startups"]
    
    if keywords is None:
        keywords = ["problema", "automatizar", "SAT", "RFC", "contador"]
    
    # Simulated Reddit data
    reddit_data = {
        "timestamp": datetime.now().isoformat(),
        "source": "reddit",
        "subreddits_searched": subreddits,
        "keywords": keywords,
        "posts_found": [
            {
                "subreddit": "r/mexico",
                "title": "¿Alguien sabe cómo validar RFC automáticamente?",
                "upvotes": 45,
                "comments": 12,
                "pain_point": "manual RFC validation"
            },
            {
                "subreddit": "r/Entrepreneur",
                "title": "El problema más grande: gastar 5 horas semanales en facturación",
                "upvotes": 127,
                "comments": 34,
                "pain_point": "CFDI processing time"
            },
            {
                "subreddit": "r/startups",
                "title": "¿Cómo automatizan contabilidad sin contador full-time?",
                "upvotes": 89,
                "comments": 28,
                "pain_point": "accounting automation"
            }
        ],
        "status": "success"
    }
    
    print(f"✅ Reddit data generated from {len(subreddits)} subreddits")
    return reddit_data

def save_reddit_data(data, output_path='outputs/reddit-data.json'):
    import os
    os.makedirs('outputs', exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    print(f"💾 Data saved to {output_path}")

if __name__ == "__main__":
    reddit_data = scrape_reddit()
    save_reddit_data(reddit_data)