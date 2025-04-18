# 📝 Grammar Correction App by Noorulhuda

This is a simple, clean, and powerful AI-powered grammar correction web application developed using Python and Streamlit. The app leverages OpenAI’s GPT-3.5 model to instantly correct grammar in English sentences or paragraphs. Designed for clarity and ease of use, this project demonstrates how advanced language models can be integrated into accessible user interfaces.

🌐 Try it live: [https://noorulhuda-grammar-correction.streamlit.app](https://noorulhuda-grammar-correction.streamlit.app)

Key Features:
- Real-time grammar correction using GPT-3.5 Turbo
- Clean and intuitive user interface built with Streamlit
- Secure API key handling using Streamlit Secrets Manager
- Responsive layout suitable for desktop and mobile
- Perfect for students, writers, educators, and anyone looking to improve written English

How it works:
Users enter a sentence or paragraph into a text box and click "Correct Grammar." The app sends the text to OpenAI’s model via their official Python SDK. The model returns a grammatically corrected version of the text, which is then displayed in a second text area for easy comparison or copying.

To run locally:
1. Clone this repository:
   `git clone https://github.com/Noorulhuda87/grammar-correction-app-streamlit.git`

2. Install the required Python packages:
   `pip install -r requirements.txt`

3. Set up your OpenAI API key securely by creating a file named `.streamlit/secrets.toml` and adding:
   `OPENAI_API_KEY = "your_actual_openai_key_here"`

4. Run the app:
   `streamlit run app.py`

Folder Structure:
- `app.py`: Main Streamlit application
- `requirements.txt`: Dependencies for the app
- `.streamlit/secrets.toml`: Secure location for storing your API key (not pushed to GitHub)

Author:
**Noorulhuda Khamees** – Software Engineering Technician, Python Developer, and AI Enthusiast based in Canada. I’m passionate about creating smart, clean tools that solve real-world problems using modern technology.

🔗 [LinkedIn](https://www.linkedin.com/in/noorulhuda-khamees)

License:
This project is open-source and available under the MIT License. Feel free to use and modify it with credit.

