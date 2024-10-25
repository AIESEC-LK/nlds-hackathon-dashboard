import streamlit as st
import components as comp
import constants as value


comp.section_topic("Login")
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Submit button
    submit_button = st.form_submit_button("Login")

# Display result
if submit_button:
    if username == "admin" and password == "password123":  # Example credentials
        st.success("Login successful!")
    else:
        st.error("Invalid username or password")

comp.footer()
