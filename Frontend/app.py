import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/generate"

st.title("AI Chatbot")

prompt = st.text_area("Enter your prompt")

if st.button("Generate Response"):

    if prompt.strip():

        try:

            response = requests.post(
                API_URL,
                json={"prompt": prompt}
            )

            data = response.json()

            st.subheader("Response")
            st.write(data["response"])

        except Exception as e:
            st.error(f"Connection Error: {e}")