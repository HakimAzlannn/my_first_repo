import streamlit as st
import pandas as pd
import numpy as np

st.title('Pokemon Database')

st.markdown("""
This app shows the stats of pokemon!
* **Pokemon database reference:** [Click here](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6)
""")

st.sidebar.header('Pokemon Attribute')

# Upload file
pkmndata = pd.read_csv('pokemon.csv')

## Drop column
newpkmndata = pkmndata.drop(['#', 'Total','Generation','Legendary','Type1','Type2'], axis = 1)

## Sidebar - Type 1 selection
Type_1 = ['Grass','Fire','Water','Bug','Normal','Poison','Electric','Ground','Fairy','Fighting','Psychic','Rock','Ice','Dragon','Dark','Ghost','Steel']
type_1_selection = st.sidebar.multiselect('Type', Type_1, Type_1)

# Sidebar - Legendary selection
Legendarytype = sorted(pkmndata.Legendary.unique())
selected_legendary = st.sidebar.multiselect('Legendary', Legendarytype, Legendarytype)

overallpkmndata = newpkmndata[(pkmndata.Legendary.isin(selected_legendary)) & (pkmndata.Type1.isin(type_1_selection))]
st.write('Data Dimension: ' + str(overallpkmndata.shape[0]) + ' rows and ' + str(overallpkmndata.shape[1]) + ' columns.')
st.dataframe(overallpkmndata)

st.markdown("""
You can use the sidebar button!
* Also you can search your pokemon here!
""")
pkmn_name = st.text_input('pokemon.csv')
