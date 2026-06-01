from datetime import datetime
def scrape_reddit(subreddits=None, keywords=None, limit=50):
    """
    Scrape Reddit posts and comments for problems
    """
    
    # SUBREDDITS VALIDADOS POR PERPLEXITY
    if subreddits is None:
        subreddits = {
            "priority_1": ["mexico"],           # SAT/RFC/contabilidad
            "priority_2": ["Entrepreneur", "startups"],  # Automatización/operación
            "priority_3": ["argentina", "Colombia", "chile"],  # Regional
        }
    
    reddit_data = {
        "timestamp": datetime.now().isoformat(),
        "source": "reddit",
        "subreddits_searched": subreddits,
        "keywords": keywords or [
            "problema", "automatizar", "solución", 
            "SAT", "RFC", "CFDI",  # TU FOCUS
            "contador", "facturación"
        ],
        "posts": [],
        "pain_points": [],
        "validation_source": "Perplexity investigation 2026-06-01"
    }
    
    return reddit_data