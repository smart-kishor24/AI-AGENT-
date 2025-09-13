import streamlit as st
import google.generativeai as genai
import os

# Load API key from secrets or environment
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))

if not GOOGLE_API_KEY:
    st.error("❌ Google API key not found! Add it to secrets.toml or env variables.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

    # Create model (must come before using it!)
    model = genai.GenerativeModel("gemini-1.5-flash")

    st.title("Gemini AI Agent 🤖")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if user_input := st.chat_input("Ask me anything..."):
    # Save user input
    st.session_state["messages"].append(("user", user_input))
    st.chat_message("user").write(user_input)

    # Generate response from Gemini
    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    # Save AI reply
    st.session_state["messages"].append(("assistant", reply))
    st.chat_message("assistant").write(reply)
