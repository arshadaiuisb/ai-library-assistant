import streamlit as st

# =========================
# Page Configuration (MUST be first Streamlit command)
# =========================
st.set_page_config(page_title="AI Library Assistant", layout="wide")

# =========================
# App Title
# =========================
st.title("📚 AI Smart Library Assistant")
st.write("Welcome! Ask anything about library services, books, or research help.")

# =========================
# Session State Initialization
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# Simple Response Generator (Replace with LLM / Koha API later)
# =========================
def generate_response(user_input: str) -> str:
    user_input = user_input.lower()

    if "book" in user_input:
        return "📖 You can search books using the library catalog or ask for recommendations by subject."
    elif "library" in user_input:
        return "🏛️ Our library provides reference services, digital resources, and research support."
    elif "help" in user_input:
        return "🤖 I can help you find books, journals, and research guidance. What do you need?"
    else:
        return "I understand your query. Please provide more details so I can assist you better."

# =========================
# Display Chat History
# =========================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# User Input
# =========================
user_input = st.chat_input("Ask your question...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate assistant response
    response = generate_response(user_input)

    # Store assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Rerun to refresh UI
    st.rerun()

# =========================
# Sidebar (Optional Settings)
# =========================
with st.sidebar:
    st.header("⚙️ Settings")
    st.write("AI Library Assistant Prototype")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.info("You can later connect this app with Koha API or OpenAI API for advanced answers.")
