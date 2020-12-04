import pandas as pd
import streamlit as st
import sklearn
import pickle

with open("iot_model.sav", "rb") as f:
    modelo = pickle.load(f)


st.header('Entrada de dados do usuário')
st.image('ai.jpg', width=300)
st.write('')
footfall = st.text_input("footfall", 0)
atemp = st.text_input("atemp", 0)
selfLR = st.text_input("selfLR", 0)
ClinLR = st.text_input("ClinLR", 0)
DoleLR = st.text_input("DoleLR", 0)
outpressure = st.text_input("outpressure", 0)
inpressure = st.text_input("inpressure", 0)
temp = st.text_input("temp", 24)

df = pd.DataFrame(columns=["footfall", "atemp", "selfLR", "ClinLR", "DoleLR", "outpressure", "inpressure", "temp"])
df.loc[0] = [footfall, atemp, selfLR, ClinLR, DoleLR, outpressure, inpressure, temp]
predicao = modelo.predict(df)

st.write("RESULTADO: ")
if predicao == '0':
    st.write("Dispositivo ok!")
    st.image('ok.png', width=100)
elif predicao == '1':
    st.write("Falha no dispositivo!")
    st.image('fail.png', width=100)



hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 