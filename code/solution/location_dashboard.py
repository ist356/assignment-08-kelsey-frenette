'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide") # Set the page layout to wide


df = pd.read_csv('./cache/tickets_in_top_locations.csv') # Load the data


st.title('Top Locations for Parking Tickets within Syracuse') # Set the title of the dashboard
st.caption('This dashboard shows the parking tickets that were issued in the top locations with $1,000 or more in total aggregate violation amounts.')
# Add a caption to the dashboard

locations = df['location'].unique() # Get the unique locations

location = st.selectbox('Select a location:', locations) # Create a selectbox to choose a location
if location:
    filtered_df = df[df['location'] == location] # Filter the data based on the selected location

    col1, col2 = st.columns(2) # Create two columns

    with col1: 
        st.metric("Total tickets issued", filtered_df.shape[0]) # Display the total number of tickets issued
        fig1, ax1 = plt.subplots()
        ax1.set_title('Tickets Issued by Hour of Day') # Set the title of the plot
        sns.barplot(data=filtered_df, x="hourofday", y="count", estimator="sum", hue="hourofday", ax=ax1) # Create a barplot
        st.pyplot(fig1) # Display the plot

    with col2:
        st.metric("Total amount", f"$ {filtered_df['amount'].sum()}") # Display the total amount of tickets
        fig2, ax2 = plt.subplots() 
        ax2.set_title('Tickets Issued by Day of Week') # Set the title of the plot
        sns.barplot(data=filtered_df, x="dayofweek", y="count", estimator="sum", hue="dayofweek", ax=ax2) # Create a barplot
        st.pyplot(fig2) # Display the plot

    st.map(filtered_df[['lat', 'lon']]) # Display a map of the selected location