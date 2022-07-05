import streamlit as st
import pandas as pd
from pathlib import Path
import yfinance as yf
from MCForecastTools import MCSimulation
from yahoofinancials import YahooFinancials
from PIL import Image
import hvplot.pandas
#import plotly.figure_factory as ff
import matplotlib.pyplot as plt
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
     st.bokeh_chart(hv.render(st.session_state.mc_plot))  
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
               ticker_list = []
          for company in user_choice:
               ticker_list.append(asx_dict[company]+'.ax')
          ticker = yf.Tickers(ticker_list)
          close_df = ticker.history(period="1y")
          st.session_state.close_df = close_df
          st.session_state.user_choice = user_choice
          

          # Comes Adam Code
          data = yf.download(ticker_list, start="2017-01-01", end="2017-04-30")
          MC_thirty_year = MCSimulation(
                                   portfolio_data = data,
                                   weights = [0.2,0.2,0.2,0.2,0.2],
                                   num_simulation = 300,
                                   num_trading_days = 252 * 5
                              )
          st.write(MC_thirty_year.calc_cumulative_return())
          mc_plot = MC_thirty_year.plot_distribution()
          #st.session_state.mc_plot = mc_plot
          #MC_thirty_year.plot_distribution()
          #st.pyplot(mc_plot)
          even_tbl = MC_thirty_year.summarize_cumulative_return()
          st.write(even_tbl)
          # Your code from here
          #close_df = close_df['Close'].dropna()
          # close_df.columns = user_choice
          # st.dataframe(close_df.head())
          # close_df_plot = close_df.hvplot.line(title='Comparison', ylabel='Price in AUD', xlabel='Date')
          # st.session_state.close_df_plot = close_df_plot
          # st.bokeh_chart(hv.render(close_df_plot))

          # Assigning information to variables
          # iterator = 1
          # for ticker in ticker_list:
          #      globals()[f'input{iterator}_info'] = yf.Ticker(ticker).info
          #      iterator += 1
          # #st.write(globals()[f'input1_info'])
          # iterator = 1
          # while iterator <= len(user_choice):
          #      info = globals()[f'input{iterator}_info']
          #      globals()[f'input{iterator}_name'] = info['longName']
          #      globals()[f'input{iterator}_shortName'] = info['shortName']
          #      globals()[f'input{iterator}_sector'] = info['sector']
          #      globals()[f'input{iterator}_industry'] = info['industry']
          #      globals()[f'input{iterator}_website'] = info['website']
          #      globals()[f'input{iterator}_city'] = info['city']
          #      globals()[f'input{iterator}_state'] = info['state']
          #      globals()[f'input{iterator}_logoUrl'] = info['logo_url']

          #      globals()[f'input{iterator}_dayHigh'] = info['dayHigh']
          #      globals()[f'input{iterator}_ebitda'] = info['ebitda']
          #      globals()[f'input{iterator}_forwardPE'] = info['forwardPE']
          #      globals()[f'input{iterator}_targetLowPrice'] = info['targetLowPrice']
          #      globals()[f'input{iterator}_recommendationKey'] = info['recommendationKey']
               
          #      globals()[f'input{iterator}_profitMargins'] = info['profitMargins']
          #      globals()[f'input{iterator}_quickRatio'] = info['quickRatio']
          #      globals()[f'input{iterator}_roa'] = info['returnOnAssets']
          #      globals()[f'input{iterator}_roe'] = info['returnOnEquity']   
          #      iterator += 1

          # # Display Selected Companies information
          # x = 1
          # for ticker in ticker_list:

          # # Form and display graph

          #      # General information
          #      st.write(
          #           f"{globals()[f'input{x}_name']} ({ticker}) is a {globals()[f'input{x}_sector']} company, apart of the {globals()[f'input{x}_industry']} industry, "
          #           f"located in {globals()[f'input{x}_city']}, {globals()[f'input{x}_state']}. "
          #           f"It traded at a high of ${globals()[f'input{x}_dayHigh']} today, its forward price-to-earnings ratio is {round(globals()[f'input{x}_forwardPE'],2)} "
          #           f"and its EBITDA is sitting at ${globals()[f'input{x}_ebitda']}. "
          #      )

          #      # Financial information
          #      st.write(
          #           f"{globals()[f'input{x}_shortName']}'s profit margins are currently at {round(globals()[f'input{x}_profitMargins']*100,2)}% "
          #           f"and quick ratio is {globals()[f'input{x}_quickRatio']}. "
          #           f"The return of assets ratio is {round(globals()[f'input{x}_roa'],5)}, while the return of equities ratio is {round(globals()[f'input{x}_roe'],5)}. "
          #           f"According to Yahoo Finance, the target low price is ${globals()[f'input{x}_targetLowPrice']}, so it's recommended to {globals()[f'input{x}_recommendationKey']}."
          #      )

          #      # Websites
          #      st.write(globals()[f'input{x}_website'])
          #      st.write(f'https://au.finance.yahoo.com/quote/{ticker}')
          #      st.write('----------------------------------------')
          #      x+=1
        
