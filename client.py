import streamlit as st
from datetime import datetime

def add_client(df, save_data):
    """Page for adding a new client to the database."""
    st.subheader("Add a New Client")
    st.markdown("### 📝 Client Registration Form")

    with st.form("add_client_form"):
        name = st.text_input("Name", placeholder="Enter full name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1, help="Enter the client's age")
        gender = st.selectbox("Gender", ["Male", "Female"], help="Select the client's gender")
        last_visit = st.date_input("Last Visit", datetime.now())
        next_appointment = st.date_input("Next Appointment", datetime.now())
        notes = st.text_area("Notes", placeholder="Enter any additional notes")
        submit_button = st.form_submit_button("Submit")

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
            save_data(df)
            st.success(f"✅ Client {name} has been added successfully!")
            st.balloons()
    return df
