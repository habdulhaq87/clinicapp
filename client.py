import streamlit as st
from datetime import datetime
import pandas as pd
import requests
import base64

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
            new_data = pd.DataFrame([{
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Last Visit": last_visit.strftime("%Y-%m-%d"),
                "Next Appointment": next_appointment.strftime("%Y-%m-%d"),
                "Notes": notes,
            }])

            # Add the new row to the DataFrame
            df = pd.concat([df, new_data], ignore_index=True)
            save_data(df)  # Save to GitHub
            st.success(f"✅ Client {name} has been added successfully!")
            st.balloons()
    return df

def save_data_to_github(df, filename):
    """Save the updated DataFrame to GitHub."""
    # Load GitHub token from Streamlit secrets
    token = st.secrets["GITHUB_TOKEN"]
    repo = "habdulhaq87/clinicapp"  # Your GitHub repository
    path = filename  # e.g., "database.csv" or "data/database.csv" if in a subfolder

    # Get the file SHA for updating the existing file
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        sha = response.json()["sha"]
        st.info(f"File found in GitHub. SHA: {sha}")
    elif response.status_code == 404:
        sha = None  # If the file does not exist, prepare to create it
        st.warning("File not found in GitHub. It will be created.")
    else:
        st.error(f"Failed to retrieve file details. Response: {response.json()}")
        return

    # Encode the updated DataFrame as Base64
    content = df.to_csv(index=False).encode("utf-8")
    base64_content = base64.b64encode(content).decode("utf-8")

    # Prepare data for the PUT request
    data = {
        "message": "Update database.csv",
        "content": base64_content,
        "sha": sha,
    }

    # Push the updated content to GitHub
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 200:
        st.success("Database successfully updated on GitHub!")
    else:
        st.error("Failed to update the database on GitHub.")
        st.error(response.json())
