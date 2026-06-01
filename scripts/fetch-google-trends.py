"""
fetch-google-trends.py
Testing version with sample data
"""

import json
from datetime import datetime

def fetch_google_trends(keywords=None, timeframe='7d', geo_region='MX'):
    if keywords is None:
        keywords = ["validar RFC", "factura CFDI error", "SAT México"]
    
    trends_data = {
        "timestamp": datetime.now().isoformat(),
        "source": "google_trends",
        "region": geo_region,
        "keywords_searched": keywords,
        "volume_data": {"validar RFC": 450, "factura CFDI error": 320, "SAT México": 280},
        "status": "success"
    }
    
    print(f"✅ Data generated for {len(keywords)} keywords")
    return trends_data

def save_trends_data(data, output_path='outputs/google-trends.json'):
    import os
    os.makedirs('outputs', exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    print(f"💾 Data saved to {output_path}")

if __name__ == "__main__":
    trends_mx = fetch_google_trends(geo_region='MX')
    save_trends_data(trends_mx)