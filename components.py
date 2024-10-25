import constants as value
import components as comp
import sys
import os
import streamlit as st
import time

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# This component can display a title with a content.
# You have to pass component title and captions as parameters.


def infomation_package(component_title, component_captions):
    st.markdown(f"""
        <div style="text-align: center;">
            <h1>{component_title}</h1>
            {''.join(
                [f"<p style='text-align:center; font-size:20px'>{caption}</p>" for caption in component_captions])}
        </div>
    """, unsafe_allow_html=True)


def infomation_package_description(component_captions):
    st.markdown(
        f"""
        <div style="text-align: center;">
            {''.join(
            [f"<p style='text-align:center; font-size:20px;'>{caption}</p>" for caption in component_captions])}
        </div>
        """,
        unsafe_allow_html=True
    )


def create_gap(number_of_lines):
    for i in range(number_of_lines):
        st.write("####")


def nav_button(inner_text, button_color, text_color, url):
    button_code = f"""
        <div style="display: flex; justify-content: center;">
        <button class="css-1cpxqw2 edgvbvh5" style="background-color: {button_color}; color: {text_color}; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;"><strong>{inner_text}</strong></button>
        </div>
    """
    st.markdown(button_code, unsafe_allow_html=True)


# This component is created to show a topic
# You have to pass the topic


def section_topic(heading):
    st.markdown(f"""
        <div style="text-align: center;">
            <h1>{heading}</h1>
        </div>
    """, unsafe_allow_html=True)


# This function is used to format the contact numbers

def contact_number_formatter(contact_number):

    contact_number = str(contact_number)
    formatted_number = contact_number[:3] + " " + \
        contact_number[3:6] + " " + contact_number[6:]

    return formatted_number

# Timeline Image Changer


def footer():

    create_gap(3)

  #  st.divider()

  #  col1, col2, col3 = st.columns([1, 20, 1])

  #  with col2:
   #     st.image(value.FOOTER)

    st.markdown(
        """
        <div style='text-align:center'>
            <p style='font-size: 15px; color: #FFFFFF;'>
                <b>Developed by :</b> National Dev Team - AIESEC in Sri Lanka
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def aiesec_stats():
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

    with col1:
        st.markdown(f"""
                <center>
                    <h5>Present in</h5>
                    <h2>20+</h2>
                    <h5>Universities</h5>
                </center>
                """,
                    unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
                <center>
                    <h5>Active Members</h5>
                    <h2>1.5K+</h2>
                    <h5>Nationally</h5>
                </center>
                """,
                    unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
                <center>
                    <h5>Exchange Experiances</h5>
                    <h2>1.5K</h2>
                    <h5>Annually</h5>
                </center>
                """,
                    unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
                <center>
                    <h5>Social Projects</h5>
                    <h2>100+</h2>
                    <h5>Annually</h5>
                </center>
                """,
                    unsafe_allow_html=True)

    with col5:
        st.markdown(f"""
                <center>
                    <h5>Digital Engagement</h5>
                    <h2>50K+</h2>
                    <h5>Outreach</h5>
                </center>
                """,
                    unsafe_allow_html=True)


def partner(logo, title):
    st.image(logo)
    st.markdown(f"""
                <center>
                    <p style = "font-size:20px";>{title}</p>
                </center>
                """,
                unsafe_allow_html=True)


def countdown_timer(duration_seconds: int):
    # Initialize timer-related session state variables
    if 'timer_start' not in st.session_state:
        st.session_state.timer_start = None
    if 'paused_time' not in st.session_state:
        st.session_state.paused_time = 0
    if 'is_paused' not in st.session_state:
        st.session_state.is_paused = False

    # Start button action
    def start_timer():
        if st.session_state.timer_start is None:  # Timer is not running
            st.session_state.timer_start = time.time()  # Set start time
            st.session_state.is_paused = False  # Timer is now running
            st.session_state.paused_time = 0  # Reset paused time

    # Pause button action
    def pause_timer():
        if not st.session_state.is_paused:  # Only pause if running
            st.session_state.paused_time += time.time() - \
                st.session_state.timer_start  # Update paused time
            st.session_state.is_paused = True  # Set paused state

    # Resume button action
    def resume_timer():
        if st.session_state.is_paused:  # Only resume if paused
            # Reset the timer start to current time
            st.session_state.timer_start = time.time()
            st.session_state.is_paused = False  # Set running state

    # Reset button action
    def reset_timer():
        st.session_state.timer_start = None
        st.session_state.paused_time = 0
        st.session_state.is_paused = False

    col4, col1, col2, col3, col5 = st.columns([3, 2, 2, 2, 3])
    with col1:
        if st.button("Start", on_click=start_timer):
            pass
    with col2:
        if st.session_state.is_paused:
            if st.button("Resume", on_click=resume_timer):
                pass
        else:
            if st.button("Pause", on_click=pause_timer):
                pass
    with col3:
        if st.button("Reset", on_click=reset_timer):
            pass

    # Countdown logic
    if st.session_state.timer_start is not None:
        elapsed_time = (time.time() - st.session_state.timer_start) + \
            st.session_state.paused_time
        remaining_time = duration_seconds - int(elapsed_time)

        if remaining_time > 0:
            st.title(f"""Time left: {
                remaining_time // 3600}h {(remaining_time % 3600) // 60}m {remaining_time % 60}s""")
            st.experimental_rerun()
        else:
            st.title("Time's up!")
            reset_timer()
    else:
        st.title("Click Start to begin the timer.")
