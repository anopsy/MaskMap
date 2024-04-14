import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder 
import xgboost as xgb
import nltk
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request
from flask_cors import CORS

nltk.download('stopwords')
nltk.download('wordnet')
df = pd.read_csv(r'D:\coding\hakkaton\all_comments.csv')
vectorizer = TfidfVectorizer()
vectorizer.fit_transform(df['Comment'])


# This is your model inference module
loaded_model = joblib.load(r'D:\coding\hakkaton\tunedXGB_model.joblib')

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    dtext = data['text']
    dtext = re.sub('[^a-zA-Z]', ' ', dtext)
    dtext = dtext.lower()
    words = dtext.split()
    words = [word for word in words if word not in set(stopwords.words('english'))]

    vector_input = vectorizer.transform(words)
    pred = loaded_model.predict_proba(vector_input)
    anx, con, dep, mas = pred[0].tolist()
    prediction = str(f"The probability of this experience to be related to Anxiety : {anx:.2f}, Depression : {dep:.2f}, Autistic Masking : {mas:.2f}, unrelated to any of the earlier mentioned disorders : {con:.2f}")

    return {'prediction': prediction}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 