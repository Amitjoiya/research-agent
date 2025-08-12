import os
import requests
from fastapi import HTTPException

# Get API Key from environment variable
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

if not SERPAPI_KEY:
    raise RuntimeError(
        "❌ SERPAPI_KEY environment variable is missing.\n"
        "Set it using: set SERPAPI_KEY=your_api_key  (Windows)\n"
        "or: export SERPAPI_KEY=your_api_key  (Mac/Linux)"
    )

BASE_URL = "https://serpapi.com/search.json"

def search_serpapi(query: str, num: int = 10):
    """Search Google using SerpAPI and return raw JSON."""
    print(f"🔍 Searching: {query}")  # Debug log

    params = {
        "engine": "google",
        "q": query,
        "num": num,
        "api_key": SERPAPI_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"SerpAPI request failed: {e}")

    data = response.json()
    if "error" in data:
        raise HTTPException(status_code=502, detail=f"SerpAPI error: {data['error']}")

    return data


def extract_links_from_serp(serp_data):
    """Extract links and snippets from SerpAPI results."""
    links = []
    organic_results = serp_data.get("organic_results", [])

    for item in organic_results:
        links.append({
            "title": item.get("title", ""),
            "link": item.get("link", ""),
            "snippet": item.get("snippet", "")
        })

    print(f"✅ Extracted {len(links)} links")  # Debug log
    return links
