import streamlit as st

def sidebar_navigation():
    """Create and handle sidebar navigation."""
    st.sidebar.title("📋 Dashboard Navigation")
    menu = ["📊 Client Overview", "➕ Add Client", "📞 Contact Info"]
    choice = st.sidebar.radio("Navigate to:", menu)
    return choice
