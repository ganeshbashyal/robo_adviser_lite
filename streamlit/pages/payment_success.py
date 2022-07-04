import streamlit as st
from PIL import Image

st.set_page_config(layout="wide",initial_sidebar_state='collapsed')

image = Image.open('../Resources/images/RoboAdvisor.png')
st.image(image)
st.markdown("# Robo Advisor Lite ")

if len(st.experimental_get_query_params()) != 0:
    st.markdown('Congratulations on securing your future !!')