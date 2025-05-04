import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='Indian Startup Funding Analysis')


df = pd.read_csv('Start_funding_cleaned.csv')

btn = st.button('Indian StartUp Funding Database')
if btn:
    st.dataframe(df)

def Load_overall_analysis():
    st.title('Overall Analysis')
    # Total Invested Amount
    total_amt = round(df['amount'].sum()) 
    # Max Amount Invested in Startup
    max_amt = df.groupby('startUp')['amount'].max().sort_values(ascending=False).head(1).values[0]
    # Top 10 Investors
    Top10_Investors = df.groupby('investors')['amount'].max().sort_values(ascending=False).head(10)
    st.dataframe(Top10_Investors)
    # Avg ticket size
    Avg_amt = df.groupby('startUp')['amount'].sum().mean()
    # Total Funded Startups
    Total_funded = df['startUp'].nunique()

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.metric('Total Amt Invested', str(total_amt) + ' Cr')
    with col2:
        st.metric('Max Amt Invested', str(max_amt) + ' Cr')
    with col3:
        st.metric('Avg Amt Invested',str(round(Avg_amt)) + ' Cr')
    with col4:
        st.metric('Total Funded Startups',str(Total_funded))

    st.header('M-on-M Investment Graph')
    option = st.selectbox('Select Type',['Total','Count'])
    if  option =='Total':
        temp1 = df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
        temp1 = df.groupby(['year','month'])['amount'].count().reset_index()

    temp1['x-axis' ] = temp1['month'].astype('str') + '-' + temp1['year'].astype('str')

    fig5, x5 = plt.subplots()
    x5.plot(temp1['x-axis'],temp1['amount'])
    st.pyplot(fig5) 
    

def Load_startup_details(startUp):
    st.title(startUp)
    # StartUp Details
    details = df[df['startUp'].str.contains(startUp)].head()[['startUp','vertical','subvertical','City','investors','amount']]
    st.title('Starup Details')
    st.dataframe(details)

    # Founding Round Details
    funding = df[df['startUp'].str.contains(startUp)].head()[['round','investors','amount','date']]
    st.title('Funding Rounds')
    st.dataframe(funding)


def Load_investor_details(investor):
    st.title(investor)
    # Recent 5 Investment of Investor
    last5_invest = df[df['investors'].str.contains(investor)].head()[['date','startUp','vertical','City','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_invest)

    col1, col2 = st.columns(2)
    with col1:
        # Biggest Investments
        big_invest = df[df['investors'].str.contains(investor)].groupby('startUp')['amount'].sum().sort_values(ascending =False).head()
        st.subheader('Biggest Investments')
        #st.dataframe(big_invest)
        fig, x = plt.subplots()
        x.bar(big_invest.index,big_invest.values)
        st.pyplot(fig)

    with col2:
        vertical = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested in')
        fig1, x1 = plt.subplots()
        x1.pie(vertical,labels=vertical.index,autopct='%0.01f%%')
        st.pyplot(fig1)

    
    col3, col4 = st.columns(2)
    with col3:
        round = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader('Investment In Stage')
        fig2, x2 = plt.subplots()
        x2.pie(round,labels=round.index,autopct='%0.01f%%')
        st.pyplot(fig2)

    with col4:
        city = df[df['investors'].str.contains(investor)].groupby('City')['amount'].sum()
        st.subheader('Investment In Cities')
        fig3, x3 = plt.subplots()
        x3.pie(city,labels=city.index,autopct='%0.01f%%')
        st.pyplot(fig3)

    col5, col6 = st.columns(2)   
    with col5:
        df['year'] = df['date'].dt.year
        year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader('Y-O-Y Investment')
        fig4, x4 = plt.subplots()
        x4.plot(year_series.index,year_series.values)
        st.pyplot(fig4)
    
df = pd.read_csv('Start_funding_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select Analysis you want',['Overall Analysis','StartUp','Investors'])

if option == 'Overall Analysis':
    Load_overall_analysis()

elif option == 'StartUp':
    st.title('Startup Analysis')
    selected_startup = st.sidebar.selectbox('Select StartUp',sorted(df['startUp'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    if btn1:
        Load_startup_details(selected_startup)    
else:
    st.title('Investor Analysis')
    selected_investor = st.sidebar.selectbox('Select Investor',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        Load_investor_details(selected_investor)

    


    
    
