import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder 
import xgboost as xgb
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request

nltk.download('stopwords')
nltk.download('wordnet')
df = pd.read_csv('/home/anopsy/Code/hackher/data/all_comments.csv')
vectorizer = TfidfVectorizer()
vectorizer.fit_transform(df['Comment'])


loaded_model = joblib.load('/home/anopsy/Code/hackher/model/tunedXGB_model.joblib')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    dtext = data['text']
    dtext = re.sub('[^a-zA-Z]', ' ', dtext)
    dtext = dtext.lower()
    words = dtext.split()
    words = [word for word in words if word not in set(stopwords.words('english'))]

    vector_input = vectorizer.transform(words)
    pred = loaded_model.predict_proba(vector_input)
    anx, con, dep, mas = pred[0].tolist()
    prediction = f"The probability of this experience to be related to Anxiety : {anx:.2f}, Depression : {dep:.2f}, Autistic Masking : {mas:.2f}, unrelated to any of the earlier mentioned disorders : {con:.2f}"
    return {'prediction': prediction}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
