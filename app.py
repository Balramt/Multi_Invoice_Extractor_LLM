from dotenv import load_dotenv

load_dotenv() ## load all the environment variables from .env
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro Version
model = genai.GenerativeModel('gemini_pro_version')

def get_gemini_response(input,image,propmpt):
    response = model.generate_content([input,image[0],prompt])
    return response.text



## Intiallize our streamlit app

st.set_page_config(page_title= "Multi Language Invoice Extractor)
st.


