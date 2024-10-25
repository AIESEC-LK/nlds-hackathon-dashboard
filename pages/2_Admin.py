import streamlit as st
import components as comp
import constants as value
import Admin_Dashboard as admin_page

# Define a function to check login status


def login():
    # Create the login form only if not logged in
    comp.section_topic("Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Submit button
        submit_button = st.form_submit_button("Login")

    # Display result and redirect on successful login
    if submit_button:
        if username == "admin" and password == "admin":  # Example credentials
            st.success("Login successful!")
            st.session_state['logged_in'] = True  # Set login status to True
        else:
            st.error("Invalid username or password")


# Initialize session state for login status
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Display the appropriate page
if st.session_state['logged_in']:
    admin_page.admin_dashboard()  # Call the admin dashboard function
else:
    login()  # Show the login form if not logged in
