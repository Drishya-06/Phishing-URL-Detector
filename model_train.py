import re
from sklearn.ensemble import RandomForestClassifier
import joblib

def extract_features(url):
    features = []
    features.append(len(url))  # URL length
    features.append(1 if "@" in url else 0)
    features.append(1 if re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url) else 0)
    features.append(url.count('.'))
    features.append(1 if url.startswith("https") else 0)
    features.append(1 if re.search(r"(bit\.ly|tinyurl\.com|goo\.gl)", url) else 0)
    return features

# Sample dataset (0 = Legit, 1 = Phishing)
X = [
    extract_features("https://www.google.com"),
    extract_features("http://bit.ly/hacked"),
    extract_features("https://mail.yahoo.com"),
    extract_features("http://192.168.0.1/login"),
    extract_features("http://phishingsite.com/@login"),
    extract_features("https://tinyurl.com/bad")
]
y = [0, 1, 0, 1, 1, 1]

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, "phish_model.pkl")
print("✅ Model trained and saved as 'phish_model.pkl'")
