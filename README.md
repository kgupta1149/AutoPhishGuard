# AutoPhishGuard 
A smart phishing URL scanner that combines machine learning with Google Safe Browsing to flag suspicious links in real time.

##  What It Does
1. Checks a URL using the **Google Safe Browsing API**
2. If Google doesn't flag it, sends the URL to a **trained ML model**
3. Outputs whether it's **Safe** or **Phishing**

##  Built With
- **Language:** Python  
- **Libraries:** scikit-learn, pandas, joblib, requests  
- **ML Model:** Random Forest Classifier  
- **Dataset:** 50,000+ URLs from Kaggle  
- **API:** Google Safe Browsing

##  Setup
```bash
git clone https://github.com/kgupta1149/AutoPhishGuard.git
cd AutoPhishGuard
pip install -r requirements.txt
python3 main.py
