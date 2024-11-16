import streamlit as st
import pandas as pd
from sidebar import sidebar_navigation
from client import add_client, save_data_to_github
from contact import show_contact_info
from style import apply_custom_style

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="Clinic Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Instruction: Require Access Key
def require_access_key():
    """Prompt user to enter an access key to access the app."""
    st.title("🔒 Secure Access")
    st.markdown("""
    This application is secured. You need a valid access key to proceed.  
    If you don't have an access key, please contact the administrator.
    """)
    access_key = st.text_input("Enter your access key:", type="password")
    if st.button("Submit"):
        if access_key == st.secrets["ACCESS_KEY"]:
            st.session_state["authenticated"] = True
            st.success("Access granted!")
            st.experimental_rerun()
        else:
            st.error("Invalid access key. Please try again.")

# Apply custom styles
apply_custom_style()

# Check if the user is authenticated
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    require_access_key()
else:
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
        st.markdown("### 🔍 Search Clients")
        with st.expander("Click to filter clients"):
            name_filter = st.text_input("Search by Name")
            if name_filter:
                filtered_data = df[df["Name"].str.contains(name_filter, case=False)]
                st.dataframe(filtered_data, use_container_width=True)
            else:
                st.info("No filter applied. Showing all clients.")

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
