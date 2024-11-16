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
st.title("Clinic Data Dashboard")
st.sidebar.title("Dashboard Navigation")

# Navigation
menu = ["Overview", "Add Client", "Contact"]
choice = st.sidebar.radio("Go to", menu)

if choice == "Overview":
    st.subheader("Client Overview")
    st.dataframe(df)

    # Filter options
    st.markdown("### Filter Clients")
    name_filter = st.text_input("Search by Name")
    filtered_data = df[df["Name"].str.contains(name_filter, case=False)] if name_filter else df
    st.dataframe(filtered_data)

elif choice == "Add Client":
    st.subheader("Add a New Client")

    # Input fields
    with st.form("add_client_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        gender = st.selectbox("Gender", ["Male", "Female"])
        last_visit = st.date_input("Last Visit", datetime.now())
        next_appointment = st.date_input("Next Appointment", datetime.now())
        notes = st.text_area("Notes")
        submit_button = st.form_submit_button("Add Client")

    # Add data
    if submit_button:
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
        st.success(f"Client {name} added successfully!")

elif choice == "Contact":
    st.subheader("Contact Information")
    st.markdown("""
    - **Phone**: +123 456 7890
    - **Email**: clinic@example.com
    - **Address**: 123 Health Street, Wellness City
    """)
