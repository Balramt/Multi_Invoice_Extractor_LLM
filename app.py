from dotenv import load_dotenv


import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()


# Configure Google AI with API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Version
model = genai.GenerativeModel('gemini_pro_vision')

def get_gemini_response(input_text, image_parts, prompt):
    response = model.generate_content([input_text, image_parts[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.read()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # get the mime type of uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")



# Initialize the Streamlit app
st.set_page_config(page_title="Multi Language Invoice Extractor")
st.header("Multi Language Invoice Extractor")

# User input prompt
input_prompt = """
You are an expert in understanding invoices. Upload an image of an invoice and ask any questions based on the uploaded invoice image.
"""
# Input fields
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of invoice", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Submit button
submit = st.button("Tell me about the invoice")

# If submit button is clicked

if submit:
    try:
        image_data= input_image_details(uploaded_file)
        response = get_gemini_response(input_prompt,image_data, input)
        st.subheader("The response is")
        st.write(response)
    except FileNotFoundError as e:
        st.error(str(e))


