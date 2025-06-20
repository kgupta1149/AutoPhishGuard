import joblib  # load the ML model and vectorizer
from google_check import check_with_google  # Google Safe Browsing check

# load trained model + vectorizer
model = joblib.load("phish_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def is_valid_url(url):
    # make sure the URL starts with http:// or https://
    return url.startswith("http://") or url.startswith("https://")

def scan_url(url):
    # check with Google's API first
    google_result = check_with_google(url)
    if google_result:
        return google_result  # if Google flags it, just return that

    # if Google says nothing, use the ML model
    url_vector = vectorizer.transform([url])  # turn URL into vector
    prediction = model.predict(url_vector)[0]  # 1 = phishing, 0 = safe
    return "ML says: Phishing" if prediction == 1 else "Safe"

def main():
    print("Welcome to AutoPhishGuard - Smart URL Scanner")
    while True:
        url = input("Enter a URL (or type 'exit' to quit): ").strip()
        
        if url.lower() == "exit":
            break
        if not url:
            print("Invalid input. Try again.")
            continue
        if not is_valid_url(url):
            print("URL must start with http:// or https://")
            continue

        result = scan_url(url)
        print("Result:", result)
        print()

if __name__ == "__main__":
    main()
