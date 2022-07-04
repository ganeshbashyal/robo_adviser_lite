import streamlit as st
import pandas as pd
from pathlib import Path
import yfinance as yf
from yahoofinancials import YahooFinancials
from PIL import Image
import hvplot.pandas
import holoviews as hv


# Display image
image = Image.open('../Resources/images/RoboAdvisor.png')
st.image(image)
st.markdown("# Robo Advisor Lite ")
st.write('Welcome to New Way of Trading')

asx_file_path = Path('../Resources/master.csv')
asx_df = pd.read_csv(asx_file_path)
asx_df = asx_df[['Company', 'Code']]

asx_dict = dict(asx_df.values)
companyList = asx_dict.keys()

if 'close_df' in st.session_state:
     st.write('Loading from Cache')
     user_choice = st.multiselect('Your Choice', options = st.session_state.user_choice, default=st.session_state.user_choice)
     st.bokeh_chart(hv.render(st.session_state.close_df_plot))  
else:
     with st.form("my_form",clear_on_submit=False):
          st.write("Select upto 5 companies to start with")
          user_choice = st.multiselect(
          'Your Choice',
          companyList)
          if len(user_choice) <= 5 and len(user_choice)>1:
               pass
          else:
               st.error("You can select maximum 5 companies")
               error = st.form_submit_button("Submit")   
               st.stop()
               
     # Every form must have a submit button.
          submitted = st.form_submit_button("Submit")    
          if submitted:
               tickers = []
          for company in user_choice:
               tickers.append(asx_dict[company]+'.ax')
          st.write(tickers)
          ticker = yf.Tickers(tickers)
          close_df = ticker.history(period="1y")
          st.session_state.close_df = close_df
          st.session_state.user_choice = user_choice
          
          # Your code from here
          close_df = close_df['Close']
          close_df.columns = user_choice
          st.dataframe(close_df.head())
          close_df_plot = close_df.hvplot.line(title='Comparison', ylabel='Price in AUD', xlabel='Date')
          st.session_state.close_df_plot = close_df_plot
          st.bokeh_chart(hv.render(close_df_plot))      
        
