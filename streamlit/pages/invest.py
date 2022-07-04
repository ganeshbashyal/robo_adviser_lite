import streamlit as st
import webbrowser
from PIL import Image

image = Image.open('../Resources/images/RoboAdvisor.png')
st.image(image)
st.markdown("# Robo Advisor Lite ")

if 'user_choice' in st.session_state:
    with st.form("payment_form",clear_on_submit=False):
        for ticker in st.session_state.user_choice:
            st.text_input(ticker,100)        
        buy = st.form_submit_button("Buy")
        if buy:            
            st.session_state.isBought = 'True'
            url = 'http://localhost:8501/payment_success?isBought=True'
            webbrowser.open_new_tab(url)