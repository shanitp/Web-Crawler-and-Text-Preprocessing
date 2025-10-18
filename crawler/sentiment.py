import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure VADER lexicon is downloaded
nltk.download('vader_lexicon')

def analyze_sentiment(input_csv="crawler_output.csv", output_csv="crawler_sentiment.csv"):
    try:
        df = pd.read_csv(input_csv)

        if 'headline' not in df.columns:
            print("❌ 'headline' column not found in CSV.")
            return

        sia = SentimentIntensityAnalyzer()

        # Compute sentiment for each headline
        df['sentiment'] = df['headline'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

        # Categorize sentiment
        df['sentiment_label'] = df['sentiment'].apply(
            lambda score: 'positive' if score > 0.05 else ('negative' if score < -0.05 else 'neutral')
        )

        # Save to new CSV
        df.to_csv(output_csv, index=False, encoding='utf-8')
        print(f"✅ Sentiment analysis complete. Saved to {output_csv}")
        print(df[['headline', 'sentiment_label']].head())

    except Exception as e:
        print(f"⚠️ Error analyzing sentiment: {e}")

if __name__ == "__main__":
    analyze_sentiment()
