"""
consolidate.py
Consolidates Google Trends, Reddit, Twitter data into one JSON
"""

import json
import os
from datetime import datetime

def consolidate_all_data():
    """Read all 3 source JSONs and merge into raw-data.json"""
    
    print("📦 Consolidating data from all sources...")
    
    # Load all data files
    trends = load_json('outputs/google-trends.json')
    reddit = load_json('outputs/reddit-data.json')
    twitter = load_json('outputs/twitter-data.json')
    
    # Consolidate
    consolidated = {
        "timestamp": datetime.now().isoformat(),
        "sources": {
            "google_trends": trends,
            "reddit": reddit,
            "twitter": twitter
        },
        "problems_identified": extract_problems(trends, reddit, twitter),
        "metadata": {
            "total_sources": 3,
            "keywords_analyzed": 20,
            "posts_analyzed": 6,
            "tweets_analyzed": 3
        }
    }
    
    print(f"✅ Consolidated {len(consolidated['problems_identified'])} pain points")
    return consolidated

def load_json(filepath):
    """Load JSON file safely"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def extract_problems(trends, reddit, twitter):
    """Extract all pain points identified"""
    problems = []
    
    # From Reddit
    if 'posts_found' in reddit:
        for post in reddit['posts_found']:
            problems.append({
                "source": "reddit",
                "problem": post.get('pain_point'),
                "engagement": post.get('upvotes', 0)
            })
    
    # From Twitter
    if 'tweets_found' in twitter:
        for tweet in twitter['tweets_found']:
            problems.append({
                "source": "twitter",
                "problem": tweet.get('pain_point'),
                "engagement": tweet.get('likes', 0)
            })
    
    return problems

def save_consolidated_data(data, output_path='outputs/raw-data.json'):
    """Save to raw-data.json"""
    os.makedirs('outputs', exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    print(f"💾 Consolidated data saved to {output_path}")

if __name__ == "__main__":
    print("=" * 60)
    print("DATA CONSOLIDATION")
    print("=" * 60)
    
    consolidated_data = consolidate_all_data()
    save_consolidated_data(consolidated_data)
    
    print("=" * 60)
    print("✅ Pipeline COMPLETE!")
    print("=" * 60)