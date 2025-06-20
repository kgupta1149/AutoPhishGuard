# train.py — trains the phishing detection model using a URL dataset
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Loads the dataset

print("Loading dataset...")
data = pd.read_csv("dataset.csv")
data = data.sample(50000, random_state=42)  # Limits at 50,000

# Cleans the data
print("Cleaning dataset...")
data = data.dropna()
data["label"] = data["type"].apply(lambda x: 1 if x.lower() == "phishing" else 0)

# Extract features and labels
X = data["url"]
y = data["label"]

# Convert URLs into numerical vectors via CountVectorizer() function
print("Vectorizing the URLs...")
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split dataset into train/test
print("Splitting the dataset...")
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

#Train the Random Forest model consisting of decision trees
print("Training the model...")
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
print("Evaluating the model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Saves model and vectorizer in pkl files
joblib.dump(model, "phish_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model and vectorizer saved.")
