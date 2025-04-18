# --------------------------------------------------------
# Grammar Correction App (Web Version)
# Author: Noorulhuda Khamees
# Date: April 18, 2025
# Description:
# A Streamlit app that uses OpenAI's GPT-3.5 to correct grammar
# --------------------------------------------------------

import streamlit as st
import openai

# Use OpenAI's new client-based interface
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit page settings
st.set_page_config(page_title="Grammar Correction by Noorulhuda", layout="centered")

# Title and intro
st.title("📝 Grammar Correction by Noorulhuda")
st.markdown("Paste your sentence or paragraph below, and get instant grammar correction using OpenAI!")

# Text input area
user_input = st.text_area("✍️ Insert Text:", height=200)

# Grammar correction trigger
if st.button("✅ Correct Grammar"):
    if user_input.strip():
        with st.spinner("Correcting..."):
            try:
                # Call OpenAI chat model
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that corrects grammar."},
                        {"role": "user", "content": f"Correct the grammar: {user_input}"}
                    ],
                    temperature=0.2,
                    max_tokens=200
                )

                # Extract corrected text
                corrected = response.choices[0].message.content.strip()

                # Show output
                st.success("Grammar Corrected:")
                st.text_area("📝 Corrected Text:", value=corrected, height=200)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("Please enter some text first.")
