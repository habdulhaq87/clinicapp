import streamlit as st
import pandas as pd
import requests
from sidebar import sidebar_navigation
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
    """Load the database from a local file."""
    return pd.read_csv("database.csv")

# Save data locally
def save_data_local(df):
    """Save the database locally."""
    df.to_csv("database.csv", index=False)

# Save data to GitHub
def save_data_to_github(df, filename="database.csv"):
    """Save the updated DataFrame to GitHub using the token stored in Streamlit secrets."""
    # Load GitHub token and repository details
    token = st.secrets["GITHUB_TOKEN"]
    repo = st.secrets["GITHUB_REPO"]
    path = filename

    # Get the file SHA for updating the existing file
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        sha = response.json()["sha"]
    else:
        sha = None  # File does not exist

    # Encode the updated DataFrame as a string
    content = df.to_csv(index=False).encode("utf-8").decode("utf-8")
    data = {
        "message": "Update database.csv",
        "content": content.encode("utf-8").decode("utf-8"),
        "sha": sha,
    }

    # Push the updated content to GitHub
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 200:
        st.success("Database successfully updated on GitHub!")
    else:
        st.error("Failed to update the database on GitHub.")
        st.error(response.json())

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
