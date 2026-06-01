"""
consolidate.py

Consolidates data from Google Trends, Reddit, and Twitter
into a single JSON structure for analysis
"""

import json
import os
from datetime import datetime
from typing import Dict, List

def consolidate_all_data(
    raw_data_path: str = "outputs/raw-data.json"
) -> Dict:
    """
    Read all source JSONs and consolidate into one structure
    
    Args:
        raw_data_path: Path to output raw-data.json
    
    Returns:
        Consolidated data dict
    """
    
    consolidated = {
        "timestamp": datetime.now().isoformat(),
        "sources": {
            "google_trends": None,
            "reddit": None,
            "twitter": None
        },
        "problems_identified": [],
        "metadata": {
            "total_sources": 3,
            "processing_date": datetime.now().isoformat()
        }
    }
    
    return consolidated

def merge_data_sources(trends_data: Dict, reddit_data: Dict, twitter_data: Dict) -> Dict:
    """
    Merge data from all 3 sources into unified structure
    
    Args:
        trends_data: Google Trends output
        reddit_data: Reddit scraper output
        twitter_data: Twitter scraper output
    
    Returns:
        Merged data ready for Claude analysis
    """
    
    merged = {
        "timestamp": datetime.now().isoformat(),
        "all_sources": {
            "trends": trends_data,
            "reddit": reddit_data,
            "twitter": twitter_data
        },
        "unified_problems": []
    }
    
    return merged

def save_consolidated_data(data: Dict, output_path: str = "outputs/raw-data.json"):
    """
    Save consolidated data to JSON file
    
    Args:
        data: Consolidated data dict
        output_path: Where to save
    """
    
    os.makedirs("outputs", exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Consolidated data saved to {output_path}")

if __name__ == "__main__":
    # Test: consolidate empty data
    data = consolidate_all_data()
    save_consolidated_data(data)
    print(json.dumps(data, indent=2, default=str))