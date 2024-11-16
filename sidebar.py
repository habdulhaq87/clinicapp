import streamlit as st

def sidebar_navigation():
    """Create and handle sidebar navigation with contact info and an image."""
    # App title in the sidebar
    st.sidebar.title("🏥 Clinic Dashboard")

    # Navigation menu
    menu = ["📊 Client Overview", "➕ Add Client", "📞 Contact Info"]
    choice = st.sidebar.radio("Navigate to:", menu)

    # Divider
    st.sidebar.markdown("---")

    # Contact Info
    st.sidebar.markdown("### 📞 Contact Info")
    st.sidebar.markdown("""
    - **Phone**: +123 456 7890  
    - **Email**: clinic@example.com  
    - **Address**: 123 Health Street, Wellness City  
    """)

    # Display Image
    st.sidebar.image("content/image.jpg", caption="Our Clinic", use_column_width=True)

    return choice
