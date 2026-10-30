"""
Practical 9: Basic Natural Language Processing

Aim:
    To preprocess raw text corpus data using tokenization, stop-word removal
    and stemming, then train a sentiment classifier using TF-IDF features.

How to run:
    python practicals/practical_09_basic_nlp.py
"""

import re
import pandas as pd

# ---------------------------------------------------------------
# STEP 1: Labelled review dataset (positive / negative)
# ---------------------------------------------------------------
reviews = pd.DataFrame({
    "Review": [
        "The product quality is excellent and delivery was fast",
        "Terrible experience, the item arrived broken",
        "Really happy with this purchase, highly recommend",
        "Worst customer service ever, very disappointed",
        "Great value for money and works perfectly",
        "The packaging was damaged and support was unhelpful",
        "Excellent build quality, exceeded expectations",
        "Late delivery and poor quality, not satisfied"
    ],
    "Sentiment": ["positive", "negative", "positive", "negative",
                  "positive", "negative", "positive", "negative"]
})


# ---------------------------------------------------------------
# STEP 2: Tokenization (split text into lower-case words)
# ---------------------------------------------------------------
def tokenize(text):
    text = text.lower()
    return re.findall(r"\b[a-z]+\b", text)


reviews["Tokens"] = reviews["Review"].apply(tokenize)
print("Tokenized Reviews (First 3 samples):")
for idx, r in reviews.head(3).iterrows():
    print(f"[{r['Sentiment']}] {r['Tokens']}")

# ---------------------------------------------------------------
# STEP 3: Stop-word removal and simple stemming
# Stop words are common words (like "the", "is") that add little meaning.
# Stemming cuts word endings, e.g. "arrived" -> "arriv".
# ---------------------------------------------------------------
stop_words = {'the', 'is', 'and', 'was', 'this', 'with', 'for', 'very', 'not'}


# A very simple suffix stripper (a basic version of a Porter Stemmer)
def simple_stem(word):
    for suffix in ['ing', 'ly', 'ed', 'es', 's']:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word[:-len(suffix)]
    return word


def clean_tokens(tokens):
    filtered = [t for t in tokens if t not in stop_words]   # remove stop words
    stemmed = [simple_stem(t) for t in filtered]            # stem each word
    return stemmed


reviews["CleanTokens"] = reviews["Tokens"].apply(clean_tokens)
print("\nCleaned & Stemmed Tokens (First 3 rows):")
for idx, r in reviews.head(3).iterrows():
    print(f"Original: {r['Review'][:35]}...")
    print(f"Cleaned : {r['CleanTokens']}\n")

# ---------------------------------------------------------------
# STEP 4: TF-IDF features
# TF-IDF turns text into numbers; rare, meaningful words get higher scores.
# ---------------------------------------------------------------
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Join the cleaned tokens back into text for the vectorizer
reviews["CleanText"] = reviews["CleanTokens"].apply(lambda toks: " ".join(toks))

tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(reviews["CleanText"])
y = reviews["Sentiment"]

print("TF-IDF Vocabulary Size:", len(tfidf.get_feature_names_out()))
print("TF-IDF Matrix Shape:", X_tfidf.shape)

# ---------------------------------------------------------------
# STEP 5: Train and evaluate the sentiment classifier
# ---------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.25, random_state=42, stratify=y)

clf = MultinomialNB()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(f"Sentiment Classifier Accuracy: {accuracy_score(y_test, y_pred) * 100:.1f}%")

# ---------------------------------------------------------------
# STEP 6: Predict the sentiment of unseen customer reviews
# ---------------------------------------------------------------
test_cases = [
    "The delivery was quick and the product works great",
    "Terrible customer service and broken item arrived"
]

# New reviews must go through the SAME cleaning steps before prediction
test_vec = tfidf.transform([" ".join(clean_tokens(tokenize(t))) for t in test_cases])
preds = clf.predict(test_vec)
for rev, p in zip(test_cases, preds):
    print(f"Review: '{rev}' -> Predicted Sentiment: {p.upper()}")
