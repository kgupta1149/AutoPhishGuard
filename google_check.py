from dotenv import load_dotmv
import os
import requests  # used to send HTTP requests to the Google Safe Browsing API

def check_with_google(url):
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY") #pulls from env variable
    endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"

    # this is the body of the POST request we’re sending to Google
    body = {
        "client": {
            "clientId": "AutoPhishGuard",  # name of the app
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],  # what we want to check for
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]  # the URL the user entered
        }
    }

    try:
        # send the POST request
        res = requests.post(endpoint, json=body)

        # check if the request was successful
        if res.status_code == 200:
            # if Google flagged it as a threat, return phishing warning
            if res.json().get("matches"):
                return "Google says: Phishing"
            else:
                return None  # means probably safe
        else:
            return f"API error: {res.status_code}"
    except Exception as e:
        # if something went wrong with the request 
        return f"Exception: {e}"
