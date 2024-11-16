import streamlit as st
import pandas as pd

# Sample data
data = {
    "Name": ["John Doe", "Jane Smith", "Emily Davis", "Michael Brown"],
    "Age": [34, 29, 42, 36],
    "Gender": ["Male", "Female", "Female", "Male"],
    "Last Visit": ["2024-10-15", "2024-10-10", "2024-11-01", "2024-10-20"],
    "Next Appointment": ["2024-11-20", "2024-11-25", "2024-11-30", "2024-11-22"],
    "Notes": [
        "Needs follow-up on test results",
        "Routine check-up",
        "Dietary consultation",
        "Blood pressure monitoring"
    ],
}

# Convert data to DataFrame
df = pd.DataFrame(data)

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
        last_visit = st.date_input("Last Visit")
        next_appointment = st.date_input("Next Appointment")
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
        st.success(f"Client {name} added successfully!")

elif choice == "Contact":
    st.subheader("Contact Information")
    st.markdown("""
    - **Phone**: +123 456 7890
    - **Email**: clinic@example.com
    - **Address**: 123 Health Street, Wellness City
    """)

