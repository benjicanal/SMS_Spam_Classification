from pydantic import BaseModel
from fastapi import FastAPI
import joblib
from utils import transform_text
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')


model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = FastAPI()

class SpamData(BaseModel) : 
    text : str
    
@app.post('/predict')
async def predict(data : SpamData) : 
    try : 
        transf_text = transform_text(data.text) 
        vector_input = vectorizer.transform([transf_text])
        result = model.predict(vector_input)[0]
        result = int(result)
        return {'prediction' : result}
    except Exception as e : 
        return {'error' : str(e)}
