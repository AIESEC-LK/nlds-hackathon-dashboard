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
        submit_button = st.form_submit_button("Login")

    if submit_button:
        if username == value.ADMIN_USERNAME and password == value.ADMIN_PASSWORD:  
            st.success("Login successful!")
            st.session_state['logged_in'] = True 
        else:
            st.error("Invalid username or password")


if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    admin_page.admin_dashboard() 
else:
    login() 
