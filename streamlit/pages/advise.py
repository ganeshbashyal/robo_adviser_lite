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
#asx_df['Code']=asx_df['Code'].str.cat('AX', sep ='.')
asx_df = asx_df[['Company', 'Code']]

asx_dict = dict(asx_df.values)
companyList = asx_dict.keys()


with st.form("my_form",clear_on_submit=True):
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
        asx_list = []
        for company in user_choice:
            asx_list.append(asx_dict[company]+'.ax')
        ticker = yf.Tickers(asx_list)
        my_df = ticker.history(period="1y")
       
        
        # Your code from here
        my_df = my_df['Close']
        my_df.columns = user_choice
        my_df_plot = my_df.hvplot.line(title='Comparison', ylabel='Price in AUD', xlabel='Date')
        st.bokeh_chart(hv.render(my_df_plot))        
          
