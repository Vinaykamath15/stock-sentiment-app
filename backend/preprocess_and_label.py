import pandas as pd
from textblob import TextBlob


df = pd.read_csv('../dataset/headlines.csv')  


def get_sentiment(text):
    score = TextBlob(str(text)).sentiment.polarity
    if score > 0.1:
        return "positive"
    elif score < -0.1:
        return "negative"
    else:
        return "neutral"


df['label'] = df['Headlines'].apply(get_sentiment)


df = df[['Headlines', 'label']]
df = df.rename(columns={'Headlines': 'headline'})  


df.to_csv('../dataset/labeled_headlines.csv', index=False)

print("✅ Labeled headlines saved!")
