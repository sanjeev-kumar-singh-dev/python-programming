import streamlit as st
from transformers import pipeline

st.title("🇮🇳 स्वदेशी हिंदी चैट AI 🤖")

# Hindi-compatible model
chatbot = pipeline("text-generation", model="sberbank-ai/mGPT")

user_input = st.text_input("आप क्या पूछना चाहते हैं?")

if user_input:
    response = chatbot(user_input, max_length=100, do_sample=True, top_p=0.95, temperature=0.9)[0]['generated_text']
    st.markdown(f"**AI:** {response}")
