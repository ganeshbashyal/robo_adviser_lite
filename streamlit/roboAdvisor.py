# Import Libraries
import streamlit as st
import pandas as pd
from pathlib import Path
import numpy as np 
from numpy import nan
import hvplot.pandas
import holoviews as hv
from PIL import Image


# Set default page configuration
st.set_page_config(layout="wide",initial_sidebar_state='collapsed')

# Display RoboAvsior image
image = Image.open('../Resources/images/RoboAdvisor.png')
st.image(image)
st.markdown("# Robo Advisor Lite ")

# Load from Session
if 'loadImages' in st.session_state:
    
    st.bokeh_chart(hv.render(st.session_state.monthly_plot))
    st.bokeh_chart(hv.render(st.session_state.annual_plot))
    st.bokeh_chart(hv.render(st.session_state.visual_comparison))


# Else
else :

    # Initialize Dataframes
    asx_complete_df = pd.read_csv(Path('../Resources/master.csv')) 
    visual_comparison_df = pd.read_csv(Path('../Resources/visual_comparison.csv')) 

    # Concat .AX to each ticker
    asx_complete_df.loc[:,'asx_code'] = '.AX' 
    asx_complete_df['Code_asx'] = asx_complete_df['Code'].str.cat(asx_complete_df['asx_code'])
    asx_tickers = asx_complete_df['Code_asx'].tolist()

    # Cleaning data
    asx_list = []
    for element in asx_tickers:
        if str(element) != "nan":
            asx_list.append(element)

    # sorting by annual % increase after converting '1 Year' column to sortable value
    copied_asx = asx_complete_df.copy()
    copied_asx['Annual % increase'] = copied_asx['1 Year'].str.strip('%').astype(float)
    sorted_asx = copied_asx.sort_values('Annual % increase', ascending=False)

    # Composing dataframe for monthly graph
    basic_monhly = asx_complete_df.copy()
    basic_monhly['Monthly % increase'] = basic_monhly['1 Month'].str.strip('%').astype(float)
    sorted_monthly = basic_monhly.sort_values('Monthly % increase', ascending=False)

    # Plotting monthly graph
    monthly_plot = sorted_monthly.hvplot.bar(
        title = 'Last months Performance by Sector  ',
        stacked=True,
        x='Sector', 
        rot = 45,
        y='Monthly % increase',
        legend = 'top',
    
        ylim = (0,210),
        height=400, 
        width=800,
        alpha = 0.6,
        
    )
    st.session_state.monthly_plot = monthly_plot
    st.bokeh_chart(hv.render(monthly_plot))

    # Plotting annual graph
    annual_plot = sorted_asx.hvplot.bar(
        title = 'Past years Performance by Sector  ',
        stacked=True,
        x='Sector', 
        rot = 45,
        y='Annual % increase',
        ylabel = 'Annual % increase',    
        legend='top',
        ylim = (0,3600),
        height=400, 
        width=800,
        alpha = 0.6,
    )
    st.session_state.annual_plot = annual_plot
    st.bokeh_chart(hv.render(annual_plot))


    # A visual representation of the market showing profitability against risk factor by Sectors
    visual_comparison = visual_comparison_df.hvplot.scatter(
        title = 'Comparison of ASX listed companies ',
        x='Volatility',  
        range=(-5, 120), 
        y='Annual % increase',  
        legend='right',
        ylim = (-50,100),
        xlim = (0,2),
        height=400, 
        width=800,
        hover_cols = ['Code', 'Mkt Cap' , 'Company'],
        alpha = .6,
        by = 'Sector'
        )
    st.session_state.visual_comparison = visual_comparison
    st.bokeh_chart(hv.render(visual_comparison))
    st.session_state.loadImages = True