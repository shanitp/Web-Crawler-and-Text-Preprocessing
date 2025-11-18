## 🧠 Web Crawler Sentiment Analysis

**Web Crawler Sentiment Analysis** is a Python-based project that automatically fetches the latest **Yahoo Finance news articles** for a given stock (like Apple, Tesla, or Nvidia), stores them in a CSV file, and performs **sentiment analysis** using the **VADER NLP model**.
The goal is to identify whether the market sentiment toward a stock is **positive, neutral, or negative** based on real-time financial news headlines.

---

### 📁 Project Structure

```
Web-Crawler-Sentiment-Analysis/
│
├── crawler/
│   ├── main.py              # Entry point – runs full pipeline
│   ├── news_scraper.py      # Fetches Yahoo Finance news
│   ├── sentiment.py         # Runs VADER sentiment analysis
│
├── crawler_output.csv       # Raw scraped data (generated)
├── crawler_sentiment.csv    # Final results with sentiment (generated)
├── requirements.txt         # Dependencies list
└── venv/                    # (Optional) Virtual environment
```

---

### ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/shanitp/Web-Crawler-and-Text-Preprocessing.git
   cd Web-Crawler-Sentiment-Analysis/crawler
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # For Mac/Linux
   venv\Scripts\activate         # For Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r ../requirements.txt
   ```

---

### 📰 How It Works

#### 1. **News Scraping**

The project uses the `yfinance` library to fetch the most recent **Yahoo Finance** news articles related to a specific stock symbol (e.g., AAPL).

**File:** `news_scraper.py`

```python
from news_scraper import fetch_yahoo_news
fetch_yahoo_news("AAPL", "crawler_output.csv")
```

Output example (`crawler_output.csv`):

| headline                         | link                                                        | provider      | publish_date |
| -------------------------------- | ----------------------------------------------------------- | ------------- | ------------ |
| Apple shares soar after earnings | [https://finance.yahoo.com/](https://finance.yahoo.com/)... | Yahoo Finance | 2025-10-17   |

---

#### 2. **Sentiment Analysis**

After scraping, the project uses **VADER (Valence Aware Dictionary for Sentiment Reasoning)** from NLTK to determine the sentiment of each headline.

**File:** `sentiment.py`

```python
from sentiment import analyze_sentiment
analyze_sentiment("crawler_output.csv", "crawler_sentiment.csv")
```

Output example (`crawler_sentiment.csv`):

| headline                            | compound | sentiment |
| ----------------------------------- | -------- | --------- |
| Apple shares soar after earnings    | 0.89     | Positive  |
| Investors remain cautious on growth | -0.45    | Negative  |

---

### ▶️ Run the Full Pipeline

```bash
python main.py
```

Output:

```
🚀 Starting Yahoo Finance News Scraper + Sentiment Pipeline
📡 Fetching latest news from Yahoo Finance...
🧠 Running sentiment analysis on scraped headlines...
✅ All tasks complete! Check 'crawler_sentiment.csv' for final results.
```

---

### 📊 Example Output Visualization

| Headline                            | Sentiment |
| ----------------------------------- | --------- |
| Apple iPhone sales boost Q4 results | Positive  |
| Analysts warn of slowing demand     | Negative  |
| Market remains steady               | Neutral   |

---

### 🧩 Tech Stack

* **Language:** Python 3.10+
* **Libraries:**

  * `yfinance` – Fetches financial data and news
  * `pandas` – Data handling
  * `nltk` (VADER) – Sentiment analysis
  * `requests` – API requests (optional extension)

---

### 🚀 Future Enhancements

* [ ] Support multiple tickers (e.g., AAPL, TSLA, NVDA)
* [ ] Store results in a SQL database
* [ ] Add Flask dashboard for visualization
* [ ] Integrate with real-time news APIs (e.g., NewsAPI, Finnhub)

---

### 👨‍💻 Author

**Shani Thalappully Preman**
💼 [LinkedIn Profile](https://www.linkedin.com/in/shani-tp/)
🌐 [GitHub Profile](https://github.com/shanitp)

---


