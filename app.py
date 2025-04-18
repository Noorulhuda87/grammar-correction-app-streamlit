import streamlit as st
import openai

# Load API key from file
# Load the key from Streamlit Secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
openai.api_key = st.secrets["OPENAI_API_KEY"]


# App layout
st.set_page_config(page_title="Grammar Correction by Noorulhuda", layout="centered")

st.title("📝 Grammar Correction by Noorulhuda")
st.markdown("Paste your sentence or paragraph below, and get instant grammar correction using OpenAI!")

# Input text
user_input = st.text_area("✍️ Insert Text:", height=200)

# Corrected text output placeholder
if st.button("✅ Correct Grammar"):
    if user_input.strip():
        with st.spinner("Correcting..."):
            try:
                client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that corrects grammar."},
        {"role": "user", "content": f"Correct the grammar: {user_input}"}
    ],
    temperature=0.2,
    max_tokens=200
)

corrected = response.choices[0].message.content.strip()

                st.success("Grammar Corrected:")
                st.text_area("📝 Corrected Text:", value=corrected, height=200)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text first.")
