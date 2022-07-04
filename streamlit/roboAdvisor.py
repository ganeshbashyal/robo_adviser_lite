import streamlit as st
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
from PIL import Image



#st.markdown('<img src="./Robo.png" alt="Robo Advisor Lite" height="200" width="300" />')
# This will set  the page layout to wode and sidebar to collasped by default
st.set_page_config(layout="wide",initial_sidebar_state='collapsed')

# Display image
image = Image.open('../Resources/images/RoboAdvisor.png')
st.image(image)
st.markdown("# Robo Advisor Lite ")

st.markdown("# Show current market  ❄️")
st.write("Top 5 performing companies")
st.write("Top 5 performing sectors")
