import streamlit as st

def sidebar_navigation():
    """Create and handle sidebar navigation with buttons, contact info, and an image."""
    # Set default page if none is selected
    if "page" not in st.session_state:
        st.session_state.page = "📊 Client Overview"

    # App title in the sidebar
    st.sidebar.title("🏥 Clinic Dashboard")

    # Buttons for navigation
    if st.sidebar.button("📊 Client Overview"):
        st.session_state.page = "📊 Client Overview"
    if st.sidebar.button("➕ Add Client"):
        st.session_state.page = "➕ Add Client"
    if st.sidebar.button("📞 Contact Info"):
        st.session_state.page = "📞 Contact Info"

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

    # Return the current page stored in session state
    return st.session_state.page
