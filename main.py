from pydantic import BaseModel
from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = FastAPI()

@app.get('/')
async def index():
    return {'message': 'Welcome to the Spam Classifier API!'}

class SpamData(BaseModel) : 
    text : str
    
@app.post('/predict')
async def predict(data : SpamData) : 
    return {'prediction' : prediction}