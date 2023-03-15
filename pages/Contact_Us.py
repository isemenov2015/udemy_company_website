import streamlit as st
from emails import send_email
import pandas as pd

st.header('Contact us')
topics = pd.read_csv('topics.csv')

with st.form(key='email_form'):
    user_email = st.text_input('Your email address')
    topic = st.selectbox(label='What topic do you wish to discuss?', options=topics)
    raw_message = st.text_area('Your message')

    message=f"""\
Subject: Company site email from {user_email}

From: {user_email}
Topic: {topic}
{raw_message}
    """
    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.info('Your email was sent successfully')
