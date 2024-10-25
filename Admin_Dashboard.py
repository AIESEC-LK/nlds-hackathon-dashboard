import streamlit as st
import components as comp
import constants as value


def admin_dashboard():
    comp.section_topic("Timer")

    col1, col2, col3 = st.columns([4, 4, 4])

    with col1:
        hours = st.number_input("Hours", min_value=0,
                                max_value=23, value=0, step=1)
    with col2:
        minutes = st.number_input("Minutes", min_value=0,
                                  max_value=59, value=0, step=1)

    with col3:
        seconds = st.number_input("Seconds", min_value=0,
                                  max_value=59, value=0, step=1)

    total_duration = hours * 3600 + minutes * 60 + seconds

    # Run the countdown timer with the specified duration
    if total_duration > 0:
        comp.countdown_timer(total_duration)
    else:
        st.write("Please enter a duration greater than 0.")
