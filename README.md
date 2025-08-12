# 📚 Research Agent

A Python-based research assistant that automates:
- Searching the web using **SerpAPI**
- Extracting and cleaning content
- Summarizing results into concise insights

---

## 🚀 Features
- **Automated Search** — Uses SerpAPI to fetch accurate search results.
- **Content Extraction** — Pulls relevant webpage text.
- **Data Cleaning** — Removes HTML tags, ads, and junk content.
- **Summarization** — Generates a short, clear summary of findings.

---

## 📂 Project Structure
research-agent/
│
├── main.py # Entry point (FastAPI app)
├── searcher.py # Handles web search using SerpAPI
├── cleaner.py # Cleans and processes raw text
├── summarizer.py # Generates summaries
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .env.example # Example environment variables


---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/research-agent.git
cd research-agent

2️⃣ Create a virtual environment
python -m venv .venv

3️⃣ Activate the virtual environment
# for Windows (PowerShell)
.venv\Scripts\activate

# for Mac/Linux
source .venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

🔑 Environment Variables
SERPAPI_KEY=your_api_key_here  # Enter your api key

▶️ Running the Project
# Development mode
uvicorn main:app --reload

# After running, you'll see something like:
http://127.0.0.1:8000

## Open your browser and visit:

Home (Root endpoint):
👉 http://127.0.0.1:8000

Interactive API Documentation (Swagger UI):
👉 http://127.0.0.1:8000/docs


## To stop the server
CTRL + C
