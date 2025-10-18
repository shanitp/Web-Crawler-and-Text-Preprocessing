from news_scraper import fetch_yahoo_news
from sentiment import analyze_sentiment

def main():
    print("🚀 Starting Yahoo Finance News Scraper + Sentiment Pipeline\n")

    # Step 1: Fetch latest news
    print("📡 Fetching latest news from Yahoo Finance...")
    fetch_yahoo_news("AAPL", "crawler_output.csv")

    # Step 2: Perform sentiment analysis
    print("\n🧠 Running sentiment analysis on scraped headlines...")
    analyze_sentiment("crawler_output.csv", "crawler_sentiment.csv")

    print("\n✅ All tasks complete! Check 'crawler_sentiment.csv' for final results.\n")

if __name__ == "__main__":
    main()
