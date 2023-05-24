from email.policy import default
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

#covid dataframe
df = pd.read_csv("/mnt/c/Users/Minh Tran/Documents/python_projects/streamlit_sample/VDH-COVID-19-PublicUseDataset-EventDate.csv")
df['Event Date'] = pd.to_datetime(df['Event Date'])

#main page
st.title('COVID Data Analysis')

#Create different tabs to filter by data shown
tab1, tab2, tab3 = st.tabs(["All Data", "Health Planning Region Data", 'Event Date'])

#all data
with tab1:
    #load df
    st.dataframe(df)

#health planning region
with tab2: 
    #group by Health Planning Region
    grouped_num_cases_df = df.groupby(['Health Planning Region']).sum().sort_values('Number of Cases')
    st.header('Grouped by Health Planning Region')
    st.dataframe(grouped_num_cases_df)

    #Health Planning Region vs. Number of Cases
    st.plotly_chart(px.bar(grouped_num_cases_df, y = 'Number of Cases', title = 'Health Planning Region vs. Number of Cases'))


    #Health Planning Region vs. Number of Deaths
    grouped_num_deaths_df = df.groupby(['Health Planning Region']).sum().sort_values('Number of Deaths')
    st.plotly_chart(px.bar(grouped_num_deaths_df, y = 'Number of Deaths', title = 'Health Planning Region vs. Number of Deaths'))

    #Health Planning Region vs. Number of Hospitalizations
    grouped_num_deaths_df = df.groupby(['Health Planning Region']).sum().sort_values('Number of Hospitalizations')
    st.plotly_chart(px.bar(grouped_num_deaths_df, y = 'Number of Hospitalizations', title = 'Health Planning Region vs. Number of Hospitalizations'))

#event date
with tab3:
    st.header('Grouped by Event Date')
    grouped_event_date_df = df.groupby(df['Event Date'].astype('datetime64')).sum().sort_values('Event Date')
    st.dataframe(grouped_event_date_df)

    #event date vs number of Cases
    st.plotly_chart(px.line(grouped_event_date_df, y = 'Number of Cases', title = 'Event Date vs. Number of Cases'))

    #event date vs number of Deaths
    st.plotly_chart(px.line(grouped_event_date_df, y = 'Number of Deaths', title = 'Event Date vs. Number of Deaths'))

    #event date vs number of Hospitalizations
    st.plotly_chart(px.line(grouped_event_date_df, y = 'Number of Hospitalizations', title = 'Event Date vs. Number of Hospitalizations'))









