# Gemini Image Demo Application

Gemini Image Demo is a Streamlit-based web application that utilizes Google's Gemini AI model to analyze and interpret images, specifically invoices,
and generate relevant responses based on user input prompts.

## Features

- **User Input Prompt**: Enter custom text prompts to guide the AI's analysis.
- **Image Upload**: Upload images in JPG, JPEG, or PNG formats for analysis.
- **AI Analysis**: Utilizes the Gemini AI model to process images and generate detailed responses.
- **Responsive Interface**: Real-time feedback with displayed images and AI-generated responses.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gemini-image-demo.git
   cd gemini-image-demo
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```plaintext
     GOOGLE_API_KEY=your_google_api_key
     ```

## Usage

1. **Run the Streamlit app:**
   ->bash
   streamlit run app.py
   

2. **Open the app in your web browser:**
   - Navigate to `http://localhost:portnumber`.
   - Input a prompt and upload an image (invoice).
   - Click "Tell me about the image" to get an AI-generated response.

## Code Overview

- **Configuration:** Load environment variables and configure the Gemini AI model.
- **Function to Load Model:** Initialize the Gemini AI model and generate responses based on input.
- **Image Upload:** Handle uploaded images for AI analysis.
- **Streamlit Interface:** Setup user interface for prompt input and image upload.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
