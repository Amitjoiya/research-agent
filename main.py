import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from searcher import search_serpapi, extract_links_from_serp
from summarizer import generate_summary

# Check for API Key
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
if not SERPAPI_KEY:
    raise RuntimeError(
        "❌ SERPAPI_KEY environment variable is missing.\n"
        "Set it using:\n"
        "Windows (Powershell): setx SERPAPI_KEY \"your_api_key\"\n"
        "Mac/Linux: export SERPAPI_KEY=your_api_key"
    )

# FastAPI App
app = FastAPI(
    title="Research Agent API",
    description="Searches info using SerpAPI and summarizes it.",
    version="1.0.0"
)

# Request model
class ResearchRequest(BaseModel):
    query: str

# Routes
@app.get("/")
def home():
    return {"message": "Welcome to Research Agent API"}

@app.post("/research")
def research(req: ResearchRequest):
    try:
        # Step 1: Search on Google via SerpAPI
        serp_results = search_serpapi(req.query, num=5)

        # Step 2: Extract links
        links = extract_links_from_serp(serp_results)

        # Step 3: Summarize content
        summary = generate_summary(links)

        return {
            "query": req.query,
            "links": links,
            "summary": summary
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
