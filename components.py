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

    st.divider()

    col1, col2, col3 = st.columns([1, 20, 1])

    with col2:
        st.image(value.FOOTER)

    st.markdown(
        """
        <div style='text-align:center'>
            <p style='font-size: 15px; color: #FFFFFF;'>
                <b>Developed by :</b> Global Expansia Organizing Committee - AIESEC in University of Kelaniya
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
