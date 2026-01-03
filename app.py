import streamlit as st

import joblib

import re

import string

import nltk

from nltk.corpus import stopwords



# --- 1. AYARLAR VE YÜKLEMELER ---

st.set_page_config(page_title="Twitter Duygu Analizi", page_icon="🐦")



# Cache kullanarak modelleri ve stopwords'ü hızlı yükle

@st.cache_resource

def load_resources():

    nltk.download('stopwords')

    stop_words = set(stopwords.words('turkish'))

    model = joblib.load('twitter_sentiment_model.pkl')

    vectorizer = joblib.load('vectorizer.pkl')

    return stop_words, model, vectorizer



try:

    stop_words, model, vectorizer = load_resources()

except FileNotFoundError:

    st.error("Dosyalar bulunamadı! .pkl dosyalarının aynı klasörde olduğundan emin olun.")

    st.stop()



# --- 2. TEMİZLİK FONKSİYONU ---

def clean_text(text):

    text = text.lower()

    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    text = re.sub(r'@\S+', '', text)

    text = text.translate(str.maketrans('', '', string.punctuation))

    text = re.sub(r'\d+', '', text)

    text = ' '.join([word for word in text.split() if word not in stop_words])

    return text



# --- 3. ARAYÜZ TASARIMI ---

st.title("🐦 TWITTER (X) DUYGU ANALİZİ")

st.markdown("Bu proje **Yapay Zeka** kullanarak Türkçe metinlerin duygu durumunu analiz eder.")



text_input = st.text_area("Analiz etmek istediğiniz cümleyi girin:", height=100)



if st.button("Analiz Et"):

    if text_input.strip() == "":

        st.warning("Lütfen bir şeyler yazın.")

    else:

        cleaned_text = clean_text(text_input)

        input_vec = vectorizer.transform([cleaned_text])

        prediction = model.predict(input_vec)[0]

        probability = model.predict_proba(input_vec).max()



        st.subheader("Sonuç:")

        if prediction == "Positive":

            st.success(f"😊 POZİTİF (Güven: %{probability*100:.1f})")

        elif prediction == "Negative":

            st.error(f"😠 NEGATİF (Güven: %{probability*100:.1f})")

        else:

            st.info(f"😐 NÖTR (Güven: %{probability*100:.1f})")