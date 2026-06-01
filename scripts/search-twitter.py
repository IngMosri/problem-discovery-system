"""
search-twitter.py
Simulated Twitter/X scraper for testing
"""

import json
from datetime import datetime

def search_twitter(keywords=None, limit=100, days_back=7):
    if keywords is None:
        keywords = ["#Mexico", "#SAT", "#RFC", "#startups", "#pymes"]
    
    twitter_data = {
        "timestamp": datetime.now().isoformat(),
        "source": "twitter",
        "keywords": keywords,
        "tweets_found": [
            {
                "author": "@contador_mx",
                "text": "Pasé 3 horas validando RFCs manualmente. Tiene que haber una solución mejor.",
                "likes": 234,
                "replies": 45,
                "pain_point": "RFC validation time waste"
            },
            {
                "author": "@startup_founder",
                "text": "El mayor cuello de botella: procesar CFDI rechazados. No hay forma automática.",
                "likes": 567,
                "replies": 89,
                "pain_point": "CFDI error handling"
            },
            {
                "author": "@pymes_mexico",
                "text": "¿Alguien sabe de herramienta que automatice facturación en México?",
                "likes": 123,
                "replies": 34,
                "pain_point": "invoice automation"
            }
        ],
        "status": "success"
    }
    
    print(f"✅ Twitter data generated for {len(keywords)} keywords")
    return twitter_data

def save_twitter_data(data, output_path='outputs/twitter-data.json'):
    import os
    os.makedirs('outputs', exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    print(f"💾 Data saved to {output_path}")

if __name__ == "__main__":
    twitter_data = search_twitter()
    save_twitter_data(twitter_data)