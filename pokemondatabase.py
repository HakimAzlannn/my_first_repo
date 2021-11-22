import streamlit as st
import pandas as pd
import numpy as np

[
theme
]

# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#273346'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "sans serif"

## Set title
st.title('Pokemon Database')

## Commenting on apps
st.markdown("""
This app shows pokemon stats!
* Feel free to look for your suitable pokemon!
* **Pokemon database reference:** [Click here](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6)
""")

## Upload file
pkmndata = pd.read_csv('pokemon.csv')

## Drop column
newpkmndata = pkmndata.drop(['#', 'Total','Generation','Legendary','Type1','Type2'], axis = 1)

## Sidebar - box selection
option = st.sidebar.selectbox(
    'Select your choice',
     ['Attribute','Status'])

if option=='Attribute':
    ## Sidebar - Type 1 selection
    Type_1 = ['Grass','Fire','Water','Bug','Normal','Poison','Electric','Ground','Fairy','Fighting','Psychic','Rock','Ice','Dragon','Dark','Ghost','Steel']
    type_1_selection = st.sidebar.multiselect('Type', Type_1, Type_1)

    # Sidebar - Legendary selection
    Legendarytype = sorted(pkmndata.Legendary.unique())
    selected_legendary = st.sidebar.multiselect('Legendary', Legendarytype, Legendarytype)

    overallpkmndata = newpkmndata[(pkmndata.Legendary.isin(selected_legendary)) & (pkmndata.Type1.isin(type_1_selection))]
    st.write('Data Dimension: ' + str(overallpkmndata.shape[0]) + ' rows and ' + str(overallpkmndata.shape[1]) + ' columns.')
    st.dataframe(overallpkmndata)

else:
    ## Declare
    min_speed = int(newpkmndata['Speed'].min())
    max_speed = int(newpkmndata['Speed'].max())
    min_hp = int(newpkmndata['HP'].min())
    max_hp = int(newpkmndata['HP'].max())
 
    Hp = st.sidebar.slider('HP', min_hp, max_hp)
    speed = st.sidebar.slider('Speed', min_speed, max_speed)
    
    ## Display
    'By HP'
    data = newpkmndata[newpkmndata['HP'] == Hp]
    st.write('Data Dimension: ' + str(data.shape[0]) + ' rows and ' + str(data.shape[1]) + ' columns.')
    st.dataframe(data)
    
    'By Speed'
    data2 = newpkmndata[newpkmndata['Speed'] == speed]
    st.write('Data Dimension: ' + str(data2.shape[0]) + ' rows and ' + str(data2.shape[1]) + ' columns.')
    st.dataframe(data2)
