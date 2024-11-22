
import streamlit as st 
import numpy as np 
import pandas as pd 
import pickle

with open('final_model.pkl','rb') as file:
    model = pickle.load(file)

with open('pca.pkl','rb') as file:
    model = pickle.load(file)

with open('scaler.pkl','rb') as file:
    model = pickle.load(file)

def prediction (input_data): 

    scaled_data= scaler.transform(input_data)
    pca_data= pca.transform(scaled_data)

    pred = model.predict(pca_data)[0]

    if pred == 0:
        return 'Devoloping'
    elif pred == 1:
        return'Underdevoloped'
    else:
        return 'Devoloped'

def main():
    st.title('HELP INTERNATIONAL FOUNDATION')
    st.subheader('This application will give the status of the country based on socio-economic factors')
    ch_mort = st.text_import('enter the child mortality rate:')
    exp = st.text_input('enter exports (% gdp):')
    imp = st.text_input('enter imports (% gdp):')
    hel = st.text_input('enter expenditure on health (% gdp):')
    inc = st.text_input('enter average income:')
    inf = st.text_input('enter inflation:')
    life_exp = st.text_input('enter life expectency:')
    fer = st.text_input('Enter fertility rate:')
    gdp = st.text_input('Enter GDP per population:')

    input_list = [[ch_mort, exp, hel, imp, inc, inf, life_exp, fer, gdp]]

    if st.button('Predict'):
        response = prediction (input_list)
        st.success(response)

if __name__=='__main__':
        
