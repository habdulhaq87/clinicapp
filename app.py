import streamlit as st
import pandas as pd
from sidebar import sidebar_navigation
from client import add_client, save_data_to_github
from contact import show_contact_info
from style import apply_custom_style
from datetime import datetime

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Clinic Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styles
apply_custom_style()

# Access key for securing the app
ACCESS_KEY = "clinic2024"

def login():
    """Display login prompt and validate access key."""
    st.title("🔒 Secure Clinic Dashboard")
    st.markdown("""
    ## Welcome to the Clinic Dashboard!
    This application is secured. Please enter the access key to proceed.
    """)

    # Access key input
    password = st.text_input("Enter Access Key:", type="password")
    if st.button("Login"):
        if password == ACCESS_KEY:
            st.success("Access granted! Redirecting...")
            st.session_state["authenticated"] = True
        else:
            st.error("Invalid access key. Please try again.")

def main():
    # Load data
    def load_data():
        return pd.read_csv("database.csv")

    # Save data locally
    def save_data(df):
        df.to_csv("database.csv", index=False)

    # Initialize data
    df = load_data()

    # Sidebar Navigation
    choice = sidebar_navigation()

    # Main Content
    if choice == "📊 Client Overview":
        st.title("Client Overview")
        st.dataframe(df, use_container_width=True)

        # Filter options
        st.markdown("### 🔍 Search Filters")
        with st.expander("Click to filter clients"):
            # Name Filter
            name_filter = st.text_input("Search by Name")
            
            # Age Range Filter
            min_age, max_age = st.slider(
                "Select Age Range", 
                min_value=int(df["Age"].min()), 
                max_value=int(df["Age"].max()), 
                value=(int(df["Age"].min()), int(df["Age"].max()))
            )
            
            # Gender Filter
            gender_filter = st.multiselect(
                "Filter by Gender", 
                options=df["Gender"].unique(), 
                default=df["Gender"].unique()
            )

            # Last Visit Date Range Filter
            min_date = datetime.strptime(df["Last Visit"].min(), "%Y-%m-%d").date()
            max_date = datetime.strptime(df["Last Visit"].max(), "%Y-%m-%d").date()
            start_date, end_date = st.date_input(
                "Select Last Visit Date Range", 
                value=(min_date, max_date), 
                min_value=min_date, 
                max_value=max_date
            )

            # Apply filters to DataFrame
            filtered_data = df[
                (df["Name"].str.contains(name_filter, case=False, na=False)) &
                (df["Age"] >= min_age) & (df["Age"] <= max_age) &
                (df["Gender"].isin(gender_filter)) &
                (pd.to_datetime(df["Last Visit"]) >= pd.to_datetime(start_date)) &
                (pd.to_datetime(df["Last Visit"]) <= pd.to_datetime(end_date))
            ]

            # Display filtered data
            st.dataframe(filtered_data, use_container_width=True)

    elif choice == "➕ Add Client":
        # Update both local and GitHub-stored data
        df = add_client(df, lambda updated_df: save_data_to_github(updated_df, "database.csv"))

    elif choice == "📞 Contact Info":
        show_contact_info()

    # Default content if no button is clicked (optional)
    if not choice:
        st.title("Welcome to the Clinic Dashboard")
        st.markdown("""
        Use the sidebar to navigate between pages:
        - View and search client data
        - Add new clients
        - View contact information
        """)

# Check authentication status
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    main()
