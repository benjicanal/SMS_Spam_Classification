import streamlit as st
import joblib
from utils import transform_text

tfid = joblib.load(open('vectorizer.pkl', 'rb'))
model = joblib.load(open('model.pkl', 'rb'))

input_sms = st.text_input("Enter the SMS/Email")
st.title("Email/SMS Spam Classifier")

if st.button("Predict"):
    # 1 Preprocess the input

    transform_sms = transform_text(input_sms)

    # 2 Vectorize the input

    vector_input = tfid.transform([transform_sms])

    # 3 Make predictions

    result = model.predict(vector_input)[0]

    # 4 Display the result

    if result == 1:
        st.header("Spam")

    else:
        st.header("Not Spam")

