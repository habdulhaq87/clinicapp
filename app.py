import streamlit as st
import pandas as pd
from client import add_client
from contact import show_contact_info
from style import apply_custom_style

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Clinic Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styles
apply_custom_style()

# Load data
def load_data():
    return pd.read_csv("database.csv")

# Save data
def save_data(df):
    df.to_csv("database.csv", index=False)

# Initialize data
df = load_data()

st.title("🏥 Clinic Data Dashboard")
st.sidebar.title("📋 Dashboard Navigation")

# Navigation
menu = ["📊 Client Overview", "➕ Add Client", "📞 Contact Info"]
choice = st.sidebar.radio("Navigate to:", menu)

if choice == "📊 Client Overview":
    st.subheader("Client Overview")
    st.dataframe(df, use_container_width=True)

    # Filter options
    st.markdown("### 🔍 Search Clients")
    with st.expander("Click to filter clients"):
        name_filter = st.text_input("Search by Name")
        if name_filter:
            filtered_data = df[df["Name"].str.contains(name_filter, case=False)]
            st.dataframe(filtered_data, use_container_width=True)
        else:
            st.info("No filter applied. Showing all clients.")

elif choice == "➕ Add Client":
    df = add_client(df, save_data)

elif choice == "📞 Contact Info":
    show_contact_info()
