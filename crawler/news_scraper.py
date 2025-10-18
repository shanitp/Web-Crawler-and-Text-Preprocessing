import yfinance as yf
import pandas as pd

def fetch_yahoo_news(ticker_symbol="AAPL", output_csv="crawler_output.csv"):
    try:
        # Create a Ticker object
        stock = yf.Ticker(ticker_symbol)

        # Fetch news (list of dicts)
        news_items = stock.news or []
        if not news_items:
            print(f"No news found for {ticker_symbol}.")
            return

        # Convert to DataFrame
        df = pd.DataFrame(news_items)

        # Flatten nested 'content' field
        if 'content' not in df.columns:
            print("No 'content' field found in Yahoo Finance response.")
            return
        df_content = pd.json_normalize(df['content'])

        # Select useful columns
        desired_columns = [
            'title', 'description', 'summary', 'pubDate',
            'displayTime', 'provider', 'canonicalUrl',
            'clickThroughUrl', 'thumbnail'
        ]
        existing_columns = [col for col in desired_columns if col in df_content.columns]

        # Merge 'id' with available fields
        df_clean = pd.concat([df['id'], df_content[existing_columns]], axis=1)

        # Rename for clarity
        df_clean.rename(columns={
            'title': 'headline',
            'description': 'desc',
            'summary': 'summary_text',
            'pubDate': 'publish_date',
            'displayTime': 'display_time',
            'clickThroughUrl': 'link'
        }, inplace=True)

        # Save to CSV
        df_clean.to_csv(output_csv, index=False, encoding='utf-8')
        print(f"✅ Saved {len(df_clean)} news items to {output_csv}")
        print(df_clean.head())

    except Exception as e:
        print(f"⚠️ Error fetching Yahoo Finance news: {e}")

if __name__ == "__main__":
    fetch_yahoo_news("AAPL")
