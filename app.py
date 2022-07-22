import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image

import helper
import preprocess

st.sidebar.header('   Loksabha Members 2019-2024',)
img1 = Image.open('IND.jpg')
st.sidebar.image(img1)
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Members of Parliament','Overall Analysis','Partywise Analysis')
)

df = pd.read_csv('loksabha_seats_statewise.csv')
d = preprocess.preprocessing(df)

if user_menu == 'Members of Parliament':
    img = Image.open('loksabha.jpg')
    st.image(img,caption='Parliament of India')
    st.sidebar.title('Member of Parliament')
    st.title('-----------------------------------------------')
    st.title('Members of Parliament')
    st.title('-----------------------------------------------')
    st.header('Number Game')

    states = d['State'].unique().tolist()
    states.insert(0,'Overall')
    first = ['Overall','Yes','No']
    party = d['Party Name'].unique().tolist()
    party.sort()
    party.insert(0,'Overall')
    selected_state = st.sidebar.selectbox('Select State', states)
    selected_party = st.sidebar.selectbox('Select Party', party)
    select_term = st.sidebar.selectbox('First Time or Not', first)
    tab = helper.mp(d,select_term,selected_party,selected_state)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader(selected_state+' total Number of MPs')
        st.text(tab.shape[0])
    with col2:
        st.subheader('Total Political Parties in '+selected_state)
        st.text(len(tab['Party Name'].unique()))
    with col3:
        st.subheader('Avg age of MP in '+selected_state)
        st.text(round(tab['Age of Member'].mean(),2))
    st.title('-----------------------------------------------')
    st.subheader('Details of MPs')
    st.table(tab)


if user_menu == 'Overall Analysis':
    img2 = Image.open('sansad.jpg')
    st.image(img2,caption='New Parliament Building (Central Vista Project)')
    st.sidebar.header('Overall Analysis')
    st.title('-----------------------------------------------')
    st.title('Overall Analysis')
    st.title('-----------------------------------------------')
    mps = d['Name of Member'].unique().shape[0]
    party = d['Party Name'].unique().shape[0]
    const = d['Constituency'].unique().shape[0]+3
    st.header('Overall Statastics')
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader('Total Number of MPs')
        st.subheader(mps)
    with col2:
        st.subheader('Total Political Parties')
        st.subheader(party)
    with col3:
        st.subheader('Number of Constituencies')
        st.subheader(const)
    st.title('-----------------------------------------------')
    st.header('Members of Parliament')
    states = d['State'].unique().tolist()
    states.insert(0,'Overall')
    tab1, tab2, tab3 = st.tabs(["Statewise", "Genderwise", "Categorywise"])
    with tab1:
        st.header('Number of MPs Statewise')
        state_mp =d['State'].value_counts().reset_index().rename(columns = {'index':'State','State':'No.of MPs'}).sort_values('State')
        fig = px.bar(state_mp, x='State',y='No.of MPs')
        st.plotly_chart(fig)
    with tab2:
        st.header('Number of MPs Genderwise')
        selected_state = st.selectbox('Select State/UT',states)
        if selected_state == 'Overall':
            st.subheader('Overall')
            fig = px.pie(d['Gender'].value_counts().reset_index().rename(columns={'index':'Gender','Gender':'No.of MPs'}),values='No.of MPs', names='Gender')
            st.plotly_chart(fig)
        else:
            st.subheader('State/UT : '+selected_state)
            fig = px.pie(d[d['State']==selected_state]['Gender'].value_counts().reset_index().rename(columns={'index':'Gender','Gender':'No.of MPs'}),values='No.of MPs', names='Gender')
            st.plotly_chart(fig)
    with tab3:
        st.header('Number of MPs Categorywise')
        selected_state = st.selectbox('Select State/UT',states,key=1)
        if selected_state == 'Overall':
            st.subheader('Overall')
            cat = d['Category'].value_counts().reset_index().rename(columns={'index':'Category','Category':'No.of MPs'})
            fig = px.pie(cat,names='Category',values='No.of MPs')
        else:
            st.subheader('State/UT : '+selected_state)
            cat = d[d['State']==selected_state]['Category'].value_counts().reset_index().rename(columns={'index':'Category','Category':'No.of MPs'})
            fig = px.pie(cat,names='Category',values='No.of MPs')
        st.plotly_chart(fig)


if user_menu == 'Partywise Analysis':
    img3 = Image.open('party.jpg')
    st.image(img3, caption='Political Parties in India')
    st.sidebar.header('Partwise Analysis')
    st.header('Top Three Parties')
    state = d[d['UT']=='No']['State'].unique().tolist()
    state.insert(0,'Overall')
    selected_states = st.selectbox('Select State',state)
    tab1 = helper.top_3(d,selected_states)
    st.table(tab1.head(3))
    st.subheader('Top 15 Parties')
    fig = px.bar(tab1.head(15),x='Party Name', y = 'No.of MPs')
    st.plotly_chart(fig)