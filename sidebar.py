import streamlit as st

def sidebar_navigation():
    """Create and handle sidebar navigation with buttons, contact info, and an image."""
    # App title in the sidebar
    st.sidebar.title("🏥 Clinic Dashboard")

    # Divider
    st.sidebar.markdown("---")

    # Navigation Buttons
    if st.sidebar.button("📊 Client Overview"):
        return "📊 Client Overview"
    if st.sidebar.button("➕ Add Client"):
        return "➕ Add Client"
    if st.sidebar.button("📞 Contact Info"):
        return "📞 Contact Info"

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

    return None
