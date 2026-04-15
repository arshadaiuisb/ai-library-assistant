import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv("library.csv")

st.set_page_config(page_title="AI Library Assistant", layout="wide")

st.title("📚 AI Smart Library Assistant")
st.write("Search books in English or Urdu")

# User input
user_input = st.text_input("🔍 Enter topic (e.g., AI, Programming, کتاب):")

if user_input:
    # English search
    results = data[data['subject'].str.contains(user_input, case=False)]

    # Urdu support (basic)
    if "کتاب" in user_input:
        st.success("آپ کتاب تلاش کر رہے ہیں")

    if not results.empty:
        st.subheader("📖 Recommended Books:")
        st.dataframe(results)
    else:
        st.warning("No results found. Try another keyword.")

st.markdown("---")
st.caption("Developed for PSF Contest 2026 🚀")
