import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.markdown("""
st.set_page_config(page_title="AI Library Assistant", layout="wide")

# 🔥 HERO SECTION
st.markdown("""
<div style='text-align:center; padding:25px; background: linear-gradient(90deg,#1f4e79,#4CAF50); border-radius:12px; color:white'>
<h1>🚀 AI Smart Library System</h1>
<p>Search • Discover • Learn with AI</p>
</div>
""", unsafe_allow_html=True)
""", unsafe_allow_html=True)
st.set_page_config(page_title="AI Library Assistant", layout="wide")
st.markdown("""
<div style='text-align:center; padding:25px; background: linear-gradient(90deg,#1f4e79,#4CAF50); border-radius:12px; color:white'>
<h1>🚀 AI Smart Library System</h1>
<p>Search • Discover • Learn with AI</p>
</div>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("library.csv")

data = load_data()

# ---------- STYLE ----------
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
}
.header {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1f4e79;
}
.sub {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}
.card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom: 10px;
}
.chat-box {
    background: #ffffff;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 8px;
}
.user {
    color: #0b5394;
    font-weight: bold;
}
.bot {
    color: #38761d;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<div class='header'>📚 AI Smart Library Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>AI Powered Search • Chat • Discovery 🚀</div>", unsafe_allow_html=True)

# ---------- TABS ----------
tab1, tab2 = st.tabs(["🔍 Search Books", "🤖 AI Chat"])

# ================= SEARCH TAB =================
with tab1:
    col1, col2 = st.columns([2,1])

    with col1:
        search = st.text_input("🔍 Search books:")

    with col2:
        subjects = ["All"] + sorted(data["subject"].unique().tolist())
        selected = st.selectbox("Filter by Subject", subjects)

    filtered = data.copy()

    if selected != "All":
        filtered = filtered[filtered["subject"] == selected]

    if search:
        filtered = filtered[
            filtered["title"].str.contains(search, case=False) |
            filtered["author"].str.contains(search, case=False)
        ]

    st.write(f"### 📖 {len(filtered)} Results Found")

    for _, row in filtered.iterrows():
        st.markdown(f"""
        <div class="card">
            <h4>📘 {row['title']}</h4>
            <p><b>Author:</b> {row['author']}</p>
            <p><b>Subject:</b> {row['subject']}</p>
        </div>
        """, unsafe_allow_html=True)

# ================= CHAT TAB =================
with tab2:
    st.subheader("🤖 AI Chat Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("Ask something...")

    if user_input:
        st.session_state.messages.append(("user", user_input))

        # Demo AI Logic
        if "ai" in user_input.lower():
            reply = "AI (Artificial Intelligence) helps machines think and learn 🤖"
        elif "library" in user_input.lower():
            reply = "A library provides access to books, journals and knowledge 📚"
        else:
            reply = "This is a smart AI demo. Full system can integrate real GPT."

        st.session_state.messages.append(("bot", reply))

    # Display chat
    for role, msg in st.session_state.messages:
        if role == "user":
            st.markdown(f"<div class='chat-box user'>You: {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-box bot'>AI: {msg}</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("🚀 AI Library System | PSF Contest Ready")
