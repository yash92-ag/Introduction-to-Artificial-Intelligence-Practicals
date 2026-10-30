"""
Practical 6: Bayes Rule and Naive Bayes Classifier

Aim:
    To apply Bayes' theorem mathematically, then train and evaluate a Naive
    Bayes text classification model using scikit-learn.

How to run:
    python practicals/practical_06_naive_bayes.py
"""

# ---------------------------------------------------------------
# PART 1: Bayes' Theorem by hand
# P(Spam | free) = [P(free | Spam) x P(Spam)] / P(free)
# ---------------------------------------------------------------
# Given prior probabilities
p_spam = 0.4
p_ham = 0.6

# Likelihoods derived from training vocabulary
p_free_given_spam = 0.6
p_free_given_ham = 0.1

# Law of Total Probability:
# P(free) = P(free|Spam)*P(Spam) + P(free|Ham)*P(Ham)
p_free = (p_free_given_spam * p_spam) + (p_free_given_ham * p_ham)

# Bayes' Theorem
p_spam_given_free = (p_free_given_spam * p_spam) / p_free

print(f"Total probability of word 'free' P(Free): {p_free:.3f}")
print(f"P(Spam | word='free') = {p_spam_given_free:.2f} ({p_spam_given_free * 100:.1f}%)")

# ---------------------------------------------------------------
# PART 2: Create a labelled email dataset
# ---------------------------------------------------------------
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

data = {
    "Text": [
        "win a free prize now",
        "claim your free lottery winnings",
        "meeting scheduled for tomorrow at 10am",
        "please review the attached report",
        "you have won a cash reward click here",
        "lunch with the team on friday",
        "urgent verify your account to claim prize",
        "project deadline extended to next week",
        "exclusive free offer just for you",
        "can you send me the sales figures"
    ],
    "Label": ["spam", "spam", "ham", "ham", "spam",
              "ham", "spam", "ham", "spam", "ham"]
}
df = pd.DataFrame(data)
print("Sample Emails Dataset (First 4 rows):\n", df.head(4))

# Convert text into numbers using a bag-of-words matrix
# (each column is a word, each cell is how many times it appears)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["Text"])
y = df["Label"]

print("\nVocabulary Size:", len(vectorizer.get_feature_names_out()))
print("Feature matrix shape:", X.shape)

# ---------------------------------------------------------------
# PART 3: Train the Naive Bayes model
# ---------------------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 70% of the data for training, 30% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

# Predict the class of an unseen email
new_email = ["claim your free reward today"]
new_vec = vectorizer.transform(new_email)
prediction = model.predict(new_vec)
print("Prediction for 'claim your free reward today':", prediction[0])

# ---------------------------------------------------------------
# PART 4: Evaluate the model
# ---------------------------------------------------------------
y_pred = model.predict(X_test)
print(f"\nTest Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nConfusion Matrix [labels=['spam', 'ham']]:\n",
      confusion_matrix(y_test, y_pred, labels=["spam", "ham"]))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
