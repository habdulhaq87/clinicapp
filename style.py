import streamlit as st

def apply_custom_style():
    """Inject custom CSS into the Streamlit app."""
    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
    }

    .css-18e3th9 {
        background-color: #f9f9f9;
    }

    .css-1d391kg {
        color: #333333;
    }

    .css-1cpxqw2 a {
        text-decoration: none;
        color: #ff4b4b;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #2a9d8f;
    }

    .css-1aumxhk {
        border-radius: 10px;
        padding: 15px;
        background-color: #ffffff;
        border: 1px solid #ccc;
    }

    .stButton button {
        background-color: #2a9d8f;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }

    .stButton button:hover {
        background-color: #21867a;
        cursor: pointer;
    }

    .stAlert {
        border-radius: 10px;
        border-left: 6px solid #e76f51;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
