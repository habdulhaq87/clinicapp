import streamlit as st

def show_contact_info():
    """Page for displaying clinic contact information."""
    st.subheader("Contact Information")
    st.markdown("""
    ### 🏢 Clinic Details
    - **📞 Phone**: +123 456 7890  
    - **📧 Email**: clinic@example.com  
    - **📍 Address**: 123 Health Street, Wellness City  
    """)
    st.image("content/image.jpg", caption="Our Clinic", use_column_width=True)
