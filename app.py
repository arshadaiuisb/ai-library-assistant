import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Library Assistant", layout="wide")

# Load data
data = pd.read_csv("library.csv")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #2c3e50;
}
.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
}
.card {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<div class='title'>📚 AI Smart Library Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Search, Filter & Discover Books 🚀</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------- SIDEBAR ----------
st.sidebar.header("🔎 Filters")

subjects = ["All"] + sorted(data["subject"].unique().tolist())
selected_subject = st.sidebar.selectbox("Select Subject", subjects)

search = st.text_input("🔍 Search books (English / Urdu):")

# ---------- FILTER LOGIC ----------
filtered_data = data.copy()

if selected_subject != "All":
    filtered_data = filtered_data[filtered_data["subject"] == selected_subject]

if search:
    filtered_data = filtered_data[
        filtered_data["title"].str.contains(search, case=False) |
        filtered_data["author"].str.contains(search, case=False) |
        filtered_data["subject"].str.contains(search, case=False)
    ]

# ---------- RESULTS ----------
st.subheader(f"📖 Showing {len(filtered_data)} Books")

# ---------- CARD VIEW ----------
for i, row in filtered_data.iterrows():
    st.markdown(f"""
    <div class="card">
        <h4>📘 {row['title']}</h4>
        <p><b>Author:</b> {row['author']}</p>
        <p><b>Subject:</b> {row['subject']}</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("🚀 Developed for PSF Contest 2026 | AI Powered Library System")
