import streamlit as st
import joblib
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
import nltk

nltk.download('punkt')
nltk.download('stopwords')


tfid = joblib.load(open('vectorizer.pkl', 'rb'))
model = joblib.load(open('model.pkl', 'rb'))


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)


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

