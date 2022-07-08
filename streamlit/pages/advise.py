# Import Libraries
import streamlit as st
import pandas as pd
from pathlib import Path
import yfinance as yf
import numpy as np
from MCForecastTools import MCSimulation
from yahoofinancials import YahooFinancials
from PIL import Image
import hvplot.pandas
import matplotlib.pyplot as plt
import holoviews as hv
import seaborn as sns


# import time
# from datetime import datetime
# from MCForecastTools2 import MCSimulation2

# Display image
image = Image.open('../Resources/images/RoboAdvisor.png')
st.image(image)
st.markdown("# Robo Advisor Lite ")
st.write('Welcome to New Way of Trading')

# Read master file to populate drop down for multi choice form
asx_file_path = Path('../Resources/master.csv')
asx_df = pd.read_csv(asx_file_path)
asx_df = asx_df[['Company', 'Code']]
asx_dict = dict(asx_df.values)
companyList = asx_dict.keys()

# If state is set
if 'close_df' in st.session_state:
     user_choice = st.multiselect('Your Choice', options = st.session_state.user_choice, default=st.session_state.user_choice)
     st.bokeh_chart(hv.render(st.session_state.my_df_plot)) 
     st.bokeh_chart(hv.render(st.session_state.sharpe_ratio_plot))
     user_amount_choice = st.number_input('How much would you like to invest',value = st.session_state.user_amount_choice)
     iterator = 0
     user_weight_choice = [0] * len(st.session_state.user_choice)
     for choice in st.session_state.user_choice:
          user_weight_choice[iterator] = st.number_input(choice, value = st.session_state.user_weight_choice[iterator -1])
          iterator = iterator + 1            

     st.write('Your Potfolio Return')
     st.write(st.session_state.output)

#Else - State is not set    
else:
     # 1st Form for user to select upto 5 companies
     with st.form("my_form",clear_on_submit=False):
          st.write("Select upto 5 companies to start with")
          user_choice = st.multiselect(
          'Your Choice',
          companyList)
          # Restrict user to select no more than 5 companies
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
               # Get the ASX tickers for user selected companies
               for company in user_choice:
                    ticker_list.append(asx_dict[company]+'.ax')

               # Get Last 5 years of data from yahoo finnance api for the user selected tickers and filter to get only the Closed proces
               ticker = yf.Tickers(ticker_list)
               my_df = ticker.history(period="5y")
               my_df = my_df['Close']
               my_df.columns = user_choice

               # Plot 5 years closing prices 
               my_df_plot = my_df.hvplot.line(title='How your selected companies are performing', ylabel='Price in AUD', xlabel='Date',height=500,
                                    width=1000)
               st.session_state.my_df_plot = my_df_plot
               st.bokeh_chart(hv.render(my_df_plot)) 


               # Plot correlation
               fig, ax = plt.subplots()
               sns.heatmap(my_df.corr(), ax=ax, vmax=1,vmin=-1)
               ax.set_title('How your selected companies are related')
               fig.set_figheight(10)
               fig.set_figwidth(10)
               st.session_state.fig = fig
               st.write(fig)


               # Plot Sharpe Ratio
               daily_std = my_df.std()
               annualized_std = daily_std*np.sqrt(252)
               sharpe_ratio = (my_df.mean()*252)/annualized_std
               sharpe_ratio_plot = sharpe_ratio.hvplot(kind='bar', title ='Sharpe Ratios')
               st.session_state.sharpe_ratio_plot = sharpe_ratio_plot            
               st.bokeh_chart(hv.render(sharpe_ratio_plot)) 


               # Initialize progress bar
               my_bar = st.progress(0)
               my_bar.progress(1)
               my_bar.progress(2)

               #Get stats for user selected companies
               x = 1
               for ticker in ticker_list:
                    globals()[f'input{x}_info'] = yf.Ticker(ticker).stats()
                    x += 1

               # Complete progress bar
               my_bar.progress(100)
               my_bar.progress(0)


               close_df = yf.download((ticker_list), period='1y')['Close'].dropna()

               # Assigning information to variables
               x = 1
               try:
                    while x <= len(user_choice):
                         info = globals()[f'input{x}_info']
                         globals()[f'input{x}_name'] = info['price']['longName']
                         globals()[f'input{x}_shortName'] = info['price']['shortName']
                         globals()[f'input{x}_sector'] = info['summaryProfile']['sector']
                         globals()[f'input{x}_industry'] = info['summaryProfile']['industry']
                         globals()[f'input{x}_website'] = info['summaryProfile']['website']
                         globals()[f'input{x}_city'] = info['summaryProfile']['city']
                         globals()[f'input{x}_state'] = info['summaryProfile']['state']

                         globals()[f'input{x}_close'] = info['summaryDetail']['previousClose']
                         globals()[f'input{x}_ebitda'] = info['financialData']['ebitda']
                         globals()[f'input{x}_forwardPE'] = info['summaryDetail']['forwardPE']
                         globals()[f'input{x}_targetLowPrice'] = info['financialData']['targetLowPrice']
                         globals()[f'input{x}_recommendationKey'] = info['financialData']['recommendationKey']
                         
                         globals()[f'input{x}_profitMargins'] = info['financialData']['profitMargins']
                         globals()[f'input{x}_quickRatio'] = info['financialData']['quickRatio']
                         globals()[f'input{x}_roa'] = info['financialData']['returnOnAssets']
                         globals()[f'input{x}_roe'] = info['financialData']['returnOnEquity']
                    
                         x += 1
               except:
                    pass

               # Write General and Financial Information for the companies

               x = 1
               for ticker in ticker_list:

                    # General information
                    try:

                         general_info = (
                              f"{x}. {globals()[f'input{x}_name']} ({ticker}) is a {globals()[f'input{x}_sector']} company, apart of the {globals()[f'input{x}_industry']} industry, "
                              f"located in {globals()[f'input{x}_city']}, {globals()[f'input{x}_state']}. "
                              f"It traded at a high of {globals()[f'input{x}_close']} AUD today, its forward price-to-earnings ratio is {round(globals()[f'input{x}_forwardPE'],2)} "
                              f"and its EBITDA is sitting at {globals()[f'input{x}_ebitda']} AUD. "
                         )
                         st.write(general_info)

                         # Financial information

                         financial_info = (
                              f"   {globals()[f'input{x}_shortName']}'s profit margins are currently at {round(globals()[f'input{x}_profitMargins']*100,2)}% "
                              f"and quick ratio is {globals()[f'input{x}_quickRatio']}. "
                              f"The return of assets ratio is {round(globals()[f'input{x}_roa'],5)}, while the return of equities ratio is {round(globals()[f'input{x}_roe'],5)}. "
                              f"According to Yahoo Finance, the target low price is {globals()[f'input{x}_targetLowPrice']} AUD, so it's recommended to {globals()[f'input{x}_recommendationKey']}."
                         )
                         st.write(financial_info)

                         # Websites
                         website = f"Website : {globals()[f'input{x}_website']}"
                         st.write(website)
                       
                    except:
                         pass
                    x+=1




     # 2nd Form for user to input weights and run monte carlo simulation

     st.write('Choose your portfolio')
     with st.form("weight_form",clear_on_submit=False):
          user_amount_choice = st.number_input('How much would you like to invest')
          st.session_state.user_amount_choice = user_amount_choice
          st.write("Choose your weights")
          iterator = 0
          user_weight_choice = [0] * len(user_choice)
          weight_sum = 0
          for choice in user_choice:
               #user_weight_choice[iterator] = st.text_input(choice, float(0.2))
               user_weight_choice[iterator] = st.number_input(choice)
               weight_sum = weight_sum + user_weight_choice[iterator]
               iterator = iterator + 1 
          if weight_sum == 1:
               pass
          else:
               st.error("Sum of all weights must equal 1")
               error = st.form_submit_button("Submit")   
               st.stop()   

     # Every form must have a submit button.
          submitted = st.form_submit_button("Submit")
          if submitted:
               st.session_state.user_weight_choice = user_weight_choice 
               ticker_list = []
               for company in user_choice:
                    ticker_list.append(asx_dict[company]+'.ax')
               ticker = yf.Tickers(ticker_list)
               close_df = ticker.history(period="1y")
               st.session_state.close_df = close_df
               st.session_state.user_choice = user_choice

               my_bar = st.progress(0)
               my_bar.progress(1)
               

               # Download 5 year data for selected tickers
               data = yf.download(ticker_list, period="5y", threads=True)

               # Run Monte Carlo Simulation
               MC_user_selected = MCSimulation(
                                        portfolio_data = data,
                                        weights=user_weight_choice,
                                        num_simulation = 50,
                                        num_trading_days = 252 * 5
                                   )
               MC_user_selected.calc_cumulative_return()
               st.session_state.MC_user_selected = MC_user_selected
              

               hvfig = MC_user_selected.simulated_return.hvplot(title = 'Simulation with user selected weights')
               st.bokeh_chart(hv.render(hvfig))

               my_bar.progress(100)
               my_bar.progress(0)

               
               custom_lower_line = hv.VLine(MC_user_selected.confidence_interval.iloc[0]).opts(color='red', line_width=10, title='Minimum Return')
               custom_upper_line = hv.VLine(MC_user_selected.confidence_interval.iloc[1]).opts(color='red', line_width=10, title='Maximum Return')
               custom_weight_hist = MC_user_selected.simulated_return.iloc[-1, :].hvplot(kind='hist', bins=20)
               st.bokeh_chart(
                         hv.render(
                                   (
                                        custom_weight_hist * custom_lower_line * custom_upper_line
                                   )
                                   .opts(xlabel='Final Cumulative Returns', ylabel='Frequency')
                         )
                         )

               return_tbl = MC_user_selected.summarize_cumulative_return()
               ci_lower = round(return_tbl.loc['95% CI Lower']*user_amount_choice,2)
               ci_upper = round(return_tbl.loc['95% CI Upper']*user_amount_choice ,2)
               output = (f"There is a 95% chance that an initial investment of {user_amount_choice} AUD in the portfolio over the next 30 years will end within in the range of {ci_lower} AUD and {ci_upper} AUD")
               st.session_state.output = output
               st.write(output)
   
              