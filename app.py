import streamlit as st
import pandas as pd
from datetime import datetime

# Load data
def load_data():
    return pd.read_csv("database.csv")

# Save data
def save_data(df):
    df.to_csv("database.csv", index=False)

# Initialize data
df = load_data()

# Streamlit App
st.set_page_config(
    page_title="Clinic Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏥 Clinic Data Dashboard")
st.sidebar.title("📋 Dashboard Navigation")

# Navigation
menu = ["📊 Client Overview", "➕ Add Client", "📞 Contact Info"]
choice = st.sidebar.radio("Navigate to:", menu)

if choice == "📊 Client Overview":
    st.subheader("Client Overview")
    st.markdown("### 👥 All Clients")

    # Display the data in an interactive table
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
    st.subheader("Add a New Client")
    st.markdown("### 📝 Client Registration Form")

    # Input form
    with st.form("add_client_form"):
        name = st.text_input("Name", placeholder="Enter full name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1, help="Enter the client's age")
        gender = st.selectbox("Gender", ["Male", "Female"], help="Select the client's gender")
        last_visit = st.date_input("Last Visit", datetime.now())
        next_appointment = st.date_input("Next Appointment", datetime.now())
        notes = st.text_area("Notes", placeholder="Enter any additional notes")
        submit_button = st.form_submit_button("Submit")

    # Handle form submission
    if submit_button:
        if name.strip() == "":
            st.error("⚠️ Name cannot be empty.")
        else:
            new_data = {
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Last Visit": last_visit.strftime("%Y-%m-%d"),
                "Next Appointment": next_appointment.strftime("%Y-%m-%d"),
                "Notes": notes,
            }
            df = df.append(new_data, ignore_index=True)
            save_data(df)  # Save to CSV
            st.success(f"✅ Client {name} has been added successfully!")
            st.balloons()

elif choice == "📞 Contact Info":
    st.subheader("Contact Information")
    st.markdown("""
    ### 🏢 Clinic Details
    - **📞 Phone**: +123 456 7890  
    - **📧 Email**: clinic@example.com  
    - **📍 Address**: 123 Health Street, Wellness City  
    """)
    st.image("content/image.jpg", caption="Our Clinic", use_column_width=True)


# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2024 Clinic Dashboard")
