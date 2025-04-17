from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
import requests

app = Flask(__name__)
CORS(app)

NEWS_API_KEY = "a48603a018ec491499eff322042863a0" 

@app.route('/stock-news/<stock_name>', methods=['GET'])
def get_stock_news(stock_name):
    url = f'https://newsapi.org/v2/everything?q={stock_name}&language=en&pageSize=5&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    articles = response.json().get('articles', [])

    headlines = [article['title'] for article in articles]

    
    results = []
    for h in headlines:
        if h:
            vec = vectorizer.transform([h])
            sentiment = model.predict(vec)[0]
            results.append({'headline': h, 'sentiment': sentiment})
    
    return jsonify({'stock': stock_name, 'results': results})



model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))


df = pd.read_csv('../dataset/labeled_headlines.csv')
print(df['label'].value_counts())
df = df.dropna(subset=['headline'])
df = df[df['headline'].str.strip() != '']
X = vectorizer.transform(df['headline'])
y = df['label']
preds = model.predict(X)
accuracy = accuracy_score(y, preds)
f1 = f1_score(y, preds, average='weighted')

@app.route('/analyze', methods=['POST'])
def analyze_headline():
    data = request.get_json()
    headline = data.get('headline')
    if not headline:
        return jsonify({'error': 'No headline provided'}), 400

    vec = vectorizer.transform([headline])
    prediction = model.predict(vec)[0]
    confidence = model.predict_proba(vec).max()

    return jsonify({
        'headline': headline,
        'sentiment': prediction,
        'confidence': float(confidence)
    })

@app.route('/metrics', methods=['GET'])
def get_metrics():
    return jsonify({'accuracy': accuracy, 'f1_score': f1})

if __name__ == '__main__':
    app.run(debug=True)
