import streamlit as st
import joblib
import re

def extract_features(url):
    features = []
    features.append(len(url))
    features.append(1 if "@" in url else 0)
    features.append(1 if re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url) else 0)
    features.append(url.count('.'))
    features.append(1 if url.startswith("https") else 0)
    features.append(1 if re.search(r"(bit\.ly|tinyurl\.com|goo\.gl)", url) else 0)
    return features

# Load model
model = joblib.load("phish_model.pkl")

# Streamlit UI
st.title("🔐 Phishing URL Detector")
st.write("Enter a URL to check if it's legitimate or phishing.")

url = st.text_input("URL:")

if st.button("Check"):
    features = extract_features(url)
    prediction = model.predict([features])[0]

    if prediction == 1:
        st.error("⚠️ Warning! This URL may be a Phishing site!")
    else:
        st.success("✅ This URL appears to be Safe.")
