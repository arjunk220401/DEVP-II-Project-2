#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, clear_output
import time

# Read the dataset
data = pd.read_excel('Kevin Cookie Company Financial Analysis.xlsx')
data.head(1001)


# In[2]:


# Import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Kevin Cookie financial data
data = pd.read_excel('Kevin Cookie Company Financial Analysis.xlsx')

# Sidebar widgets
st.sidebar.header('Filter Data')
product = st.sidebar.selectbox('Select Product:', data['Product'].unique())
start_date = st.sidebar.date_input('Start Date:', data['Date'].min())
end_date = st.sidebar.date_input('End Date:', data['Date'].max())


# Convert date inputs to pandas Timestamp
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data based on user input
filtered_data = data[(data['Product'] == product) & (data['Date'] >= start_date) & (data['Date'] <= end_date)]

# Set background color using HTML styling
background_color = """
    <style>
        body {
            background-color: #f0f0f0;  /* Set your desired background color */
        }
    </style>
"""
st.markdown(background_color, unsafe_allow_html=True)

# Dashboard title
st.title(f'Kevin Cookie Financial Analysis - {product}')

# Graphs
st.header('Total Revenue Over Time')
fig1 = px.line(filtered_data, x='Date', y='Revenue')
st.plotly_chart(fig1)

st.header('Units Sold Over Time')
fig2 = px.bar(filtered_data, x='Date', y='Units Sold')
st.plotly_chart(fig2)

st.header('Profit vs. Revenue')
fig3 = px.scatter(filtered_data, x='Revenue', y='Profit')
st.plotly_chart(fig3)

st.header('Revenue Distribution by Product')
fig4 = px.box(filtered_data, x='Product', y='Revenue')
st.plotly_chart(fig4)

st.header('Country Wise Profit Distribution')
fig5 = px.pie(filtered_data, values='Profit', names='Country', title='Country Wise Profit Distribution')
st.plotly_chart(fig5)

# Histogram for Cost Distribution with black boundaries
st.header('Cost Distribution')
fig6 = px.histogram(filtered_data, x='Cost', nbins=30, title='Cost Distribution', 
                    opacity=0.7, # Set the opacity of bars
                    barmode='overlay', # Overlay histograms
                    barnorm='percent', # Normalize to percentage
                    histnorm='probability density') # Normalize to probability density

# Update trace to add black boundaries
fig6.update_traces(marker=dict(color='blue', line=dict(color='black', width=1.5)))

st.plotly_chart(fig6)

# Bubble Chart
st.header('Bubble Chart - Revenue, Profit, and Cost')
fig7 = px.scatter(filtered_data, x='Revenue', y='Profit', size='Cost', color='Cost', hover_name='Date',
                  title='Bubble Chart - Revenue, Profit, and Cost')
st.plotly_chart(fig7)


# Heatmap
st.header('Correlation Heatmap')
heatmap_data = filtered_data[['Revenue', 'Profit', 'Units Sold', 'Cost']]
correlation_matrix = heatmap_data.corr()
fig8 = px.imshow(correlation_matrix, labels=dict(color="Correlation"), x=heatmap_data.columns, y=heatmap_data.columns)
st.plotly_chart(fig8)


# In[ ]:




