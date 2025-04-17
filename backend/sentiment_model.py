import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report
import pickle


df = pd.read_csv('../dataset/labeled_headlines.csv')

# drop empty headline
df.dropna(subset=['headline'], inplace=True)
df = df[df['headline'].str.strip() != '']

print("Original class distribution:")
print(df['label'].value_counts())

min_class_size = min(df['label'].value_counts()['positive'], df['label'].value_counts()['negative'])
df_positive = df[df['label'] == 'positive']
df_negative = df[df['label'] == 'negative']
df_neutral = df[df['label'] == 'neutral'].sample(n=min_class_size, random_state=42)

df_balanced = pd.concat([df_positive, df_negative, df_neutral])


df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)


print("\nBalanced class distribution:")
print(df_balanced['label'].value_counts())


X = df_balanced['headline']
y = df_balanced['label']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Vectorize 
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train 
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train_vec, y_train)


y_pred = model.predict(X_test_vec)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"F1 Score: {f1_score(y_test, y_pred, average='weighted'):.4f}")


pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))


# Test 
test_headlines = [
    "Apple stock hits new high after strong earnings report",
    "Tesla shares plummet after disappointing delivery numbers",
    "Microsoft remains stable amid tech market uncertainty"
]

for h in test_headlines:
    vec = vectorizer.transform([h])
    pred = model.predict(vec)[0]
    print(f"Headline: {h}\n → Sentiment: {pred}\n")
