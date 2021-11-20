import streamlit as st
import pandas as pd
import numpy as np

st.title('Pokemon Database')

st.markdown("""
This app shows the stats of pokemon!
* **Data source:** [Pokemon database](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6).
""")

st.sidebar.header('Pokemon Attribute')

# Upload file
pkmndata = pd.read_csv('pokemon.csv')

## Drop column
newpkmndata = pkmndata.drop(['#', 'Total','Generation','Legendary','Type1','Type2'], axis = 1)

## Sidebar - Type 1 selection
Type_1 = ['Grass','Fire','Water','Bug','Normal','Poison','Electric','Ground','Fairy','Fighting','Psychic','Rock','Ice','Dragon','Dark','Ghost','Steel']
type_1_selection = st.sidebar.multiselect('Type 1', Type_1, Type_1)

## Sidebar - Type 2 selection
Type_2 = ['Grass','Fire','Water','Bug','Normal','Poison','Electric','Ground','Fairy','Fighting','Psychic','Rock','Ice','Dragon','Dark','Ghost','Steel']
type_2_selection = st.sidebar.multiselect('Type 2', Type_2, Type_2)

# Sidebar - Legendary selection
Legendarytype = sorted(pkmndata.Legendary.unique())
selected_legendary = st.sidebar.multiselect('Legendary', Legendarytype, Legendarytype)

overallpkmndata = newpkmndata[(pkmndata.Legendary.isin(selected_legendary)) & (pkmndata.Type1.isin(type_1_selection)) & (pkmndata.Type2.isin(type_2_selection))]
st.write('Data Dimension: ' + str(overallpkmndata.shape[0]) + ' rows and ' + str(overallpkmndata.shape[1]) + ' columns.')
st.dataframe(overallpkmndata)